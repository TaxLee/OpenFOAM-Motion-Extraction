% DESCRIPTION OF THE CODE
% This MATLAB script calculates wave drift forces from total forces obtained from OpenFOAM simulations.
% The wave drift forces are derived by applying a Fast Fourier Transform (FFT) to the time series of total forces
% and extracting the component at twice the wave frequency. The wave drift forces are then calculated by averaging
% these forces over a wave period. The script assumes that the wave frequency is known.

% The script also includes a resampling function that resamples the force data to a new uniform sampling frequency.
% The new sampling frequency is defined by the variable `Fs_new`. The resampled force data is then used to calculate
% the FFT and the wave drift forces. The results are saved to a .txt file.

% Author: Shuijin Li
% Date: 27 Jul 2023
% Email: skli@dundee.ac.uk

% Clear all
clear all; clc;
close all;

% Stop execution on error
dbstop if error

% Start timer
tic

%% Jump to code folder path
mfile_name = mfilename('fullpath');
[pathstr, name, ext] = fileparts(mfile_name);

% Change to the folder containing the code
cd(pathstr);
addpath(pathstr);

%% INPUT
files = dir(['output_summary/*.mat']);
results = cell(length(files), 4);  % Add columns for f_d_2 and f_d_6
analysis_range = [4 10]; % Define the range of analysis

for fileIndex = 1
    % for fileIndex = 1 : length(files)
    nameOfFile = files(fileIndex).name;
    % remove everything after the last underscore
    nameOfFile_short = nameOfFile(1:find(nameOfFile=='_',1,'last')-1);
    results{fileIndex, 1} = nameOfFile_short;

    % Extract the wave period from the file name
    expression = 'T(?<WavePeriod>\d+\.\d+)H';
    tokenNames = regexp(nameOfFile,expression,'names');
    wave_period = str2double(tokenNames.WavePeriod);

    % Calculate the wave frequency
    wave_freq = 1/wave_period;

    % Load the forces data
    load(fullfile('output_summary', nameOfFile));

    % Extract the time and force components
    t = forces.t;
    F = [forces.f1, forces.f2, forces.f3, forces.f4, forces.f5, forces.f6];

    % Determine the indices for the range of analysis
    index_analysis = find(analysis_range(1) <= t & analysis_range(2) >= t);

    % Limit the time and force arrays to the range of analysis
    t = t(index_analysis);
    F = F(index_analysis,:);

    % Resample the data to a new uniform sampling frequency
    Fs_new = 100;  % New sampling frequency
    min_t_forces = min(t);
    max_t_forces = max(t);
    t_new = min_t_forces:1/Fs_new:max_t_forces;
    F_new = zeros(length(t_new), size(F,2));
    for ii = 1:size(F,2)
        % Resample the data to a new sampling frequency using a function
        disp([nameOfFile ': Resampling forces ' num2str(ii) '/' num2str(size(F,2)) '...'])
        F_new(:,ii) = resampleData(F(:,ii), t, t_new);
    end

    % Calculate the FFT of the forces
    N = length(F_new); % length of the signal
    F_fft = fft(F_new);

    % Calculate the single-sided amplitude spectrum based on FFT results
    F_fft_amp = abs(F_fft/N);
    F_fft_amp = F_fft_amp(1:N/2+1,:);
    F_fft_amp(2:end-1,:) = 2*F_fft_amp(2:end-1,:);

    % Calculate the phase spectrum based on FFT results
    F_fft_phase = angle(F_fft);
    F_fft_phase = F_fft_phase(1:N/2+1,:);

    % Calculate the frequency corresponding to each FFT component
    f = Fs_new*(0:(N/2))/N;  % Correct frequency calculation

    % Find the index for the second-order wave forces
    [~,freq_sec_index] = min(abs(f - 2*wave_freq));

    % Extract the magnitude and phase of the second-order wave forces
    F2_wave_amp = F_fft_amp(freq_sec_index,:);
    F2_wave_phase = F_fft_phase(freq_sec_index,:);

    % Convert magnitude and phase to the time domain
    F2_wave_real = F2_wave_amp .* cos(2*pi*2*wave_freq*t_new' + F2_wave_phase);

    % Find the mean (DC component) of the original forces
    F_mean = mean(F_new, 1);

    % Subtract the DC component from the second-order wave forces
    F2_wave_real = bsxfun(@minus, F2_wave_real, F_mean);

    % Calculate the wave drift forces
    FWD = mean(F2_wave_real, 1);  % Mean for each DOF

    % Store the results
    results{fileIndex, 2} = FWD(1); % surge
    results{fileIndex, 3} = FWD(2); % heave
    results{fileIndex, 4} = FWD(6); % pitch

    % Plot the wave drift forces (surge, heave, pitch) in time domain within analysis range
    figure;
    subplot(3,1,1);
    plot(t_new, real(F2_wave_real(:,1)));
    hold on;
    plot([min(t_new) max(t_new)], [FWD(1) FWD(1)], 'r--');  % Mean value as a dashed line
    text(mean(t_new), FWD(1), num2str(FWD(1)));
    ylabel('Surge Force [N]');
    title(['Wave Drift Force for ' nameOfFile_short]);
    grid on;

    subplot(3,1,2);
    plot(t_new, real(F2_wave_real(:,2)));
    hold on;
    plot([min(t_new) max(t_new)], [FWD(2) FWD(2)], 'r--');  % Mean value as a dashed line
    text(mean(t_new), FWD(2), num2str(FWD(2)));
    ylabel('Heave Force [N]');
    grid on;

    subplot(3,1,3);
    plot(t_new, real(F2_wave_real(:,6)));
    hold on;
    plot([min(t_new) max(t_new)], [FWD(6) FWD(6)], 'r--');  % Mean value as a dashed line
    text(mean(t_new), FWD(6), num2str(FWD(6)));
    xlabel('Time [s]');
    ylabel('Pitch Moment [Nm]');
    grid on;

    % Save the figure to a file
    FigureName = ['Wave_Drift_Force_' nameOfFile_short];
    FigureWidth = 10;  % in inches
    FigureHeight = 9;  % in inches
    PlotToFileColor(gcf,FigureName,FigureWidth,FigureHeight);

    % Clear unnecessary variables to save space
    clear t F t_new F_new F_fft freq F2_wave F2_wave_real FWD
end

% Save the results to a .txt file
fid = fopen('wave_drift_forces.txt', 'w');
fprintf(fid, 'Name of Case\tf_d_1\tf_d_2\tf_d_6\n');
for i = 1:size(results, 1)
    fprintf(fid, '%s\t%f\t%f\t%f\n', results{i, 1}, results{i, 2}, results{i, 3}, results{i, 4});
end
fclose(fid);

% Print the results
fprintf('Wave drift forces have been saved to wave_drift_forces.txt\n');

%% Move plots
current_date = date;
new_date = datestr(current_date, 'yyyy-mm-dd');
resultFolderName = 'output_summary';

status1 = movefile('*.png',fullfile(resultFolderName,new_date));
status2 = movefile('*.pdf',fullfile(resultFolderName,new_date));
status3 = movefile('*.eps',fullfile(resultFolderName,new_date));

%% END OF THE CODE
toc

%% Local function
function resampledData = resampleData(originalData, originalTime, newTime)
ts_in = timeseries(originalData, originalTime);
ts_out = resample(ts_in, newTime);
resampledData = squeeze(ts_out.Data(~isnan(ts_out.Data)));
end