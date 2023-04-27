% DESCRIPTION OF THE CODE:
% This code processes motion data from .txt and .txt files in all folders.
% The user can choose which data files to import and process through the
% flags at the beginning of the script.
% It reads the data, calculates the Euler angles and water surface
% elevation, and saves the output in .mat files.

% Flags:
% 1. import_trans_orient: Whether to import translation and orientation
% data. Set to 1 to import, 0 otherwise. Default: 1.
% 2. import_forces_moments: Whether to import forces and moments data. Set
% to 1 to import, 0 otherwise. Default: 1.
% 3. import_waveGauges: Whether to import water surface elevation data
% from wave gauges. Set to 1 to import, 0 otherwise. Default: 1.
%
% Author: Shuijin Li
% Date: 30 Jan 2023
% Email: skli@dundee.ac.uk

%% Clear all
clear all; clc;
close all;

% Stop execution on error
dbstop if error

% Start timer
tic

%% Jump to code folder path
% Get the path of the current file
mfile_name = mfilename('fullpath');
[pathstr, name, ext] = fileparts(mfile_name);

% Change to the folder containing the code
cd(pathstr);
addpath(pathstr);

%% Flags
% Set the flags to indicate which files should be imported and processed
import_motions = 1;
import_forces_moments = 1;
import_waveGauges = 1;

%% Input
% Define which folders should be excluded from processing
% exclude_folders: List of folders to exclude from processing. Must be
% a cell array of strings. Default: {'output_summary', 'script'}
exclude_folders = {'output_summary', 'script','originFiles','test_cases'};

% Define the output folder name
% output_folder: Name of the output folder. Default: 'output_summary'
output_folder = 'output_summary';

% Define the folder names for the time series data and water surface
% elevation data
subfolder_data = 'output';
subfolder_se = 'output';

% Define the file names for the time series data
fileName_translations = "t_vs_cm";
fileName_rotations = "t_vs_orientation";

% Define the file names for the forces and moments data
fileName_forces = ["t_vs_forces_pressure","t_vs_forces_viscous","t_vs_forces_porous"];
fileName_moments = ["t_vs_moments_pressure","t_vs_moments_viscous","t_vs_moments_porous"];

% Define the file names for the water surface elevation data
fileName_waveGauges = ["waveGauge1.txt","waveGauge2.txt","waveGauge3.txt","waveGauge4.txt"];

% Get the list of folders in the current directory
folders = dir(pwd);
folders = folders([folders.isdir]);

% exclude specified folders
folders = folders(~ismember({folders.name},[exclude_folders, '.', '..']));

%% Calculation
% for ii = 5:9
for ii = 1:length(folders)
    %% Initialize 
    clear t_vs_cm t_vs_orientation f index temp t xi_4 xi_5 xi_6 data_forces_temp data_SE motions SE resultsFolder_final
    
    % Set the path of the results folder
    resultsFolder_final = fullfile(output_folder,folders(ii).name);
    
    % Create the results folder if it doesn't exist and let the user know
    if exist(resultsFolder_final, 'dir') == 0 
        mkdir(resultsFolder_final); 
        disp(['Folder created: ' resultsFolder_final]);
    end
    
    % Set the path of the data subfolder within the results folder
    resultsFolder_case = fullfile(folders(ii).name,subfolder_data);
    
    % Copy the data from the subfolder to the results folder
    status_cp = copyfile(resultsFolder_case,resultsFolder_final);
    
    % Let the user know that files have been copied to the new destination
    if status_cp == 1
        disp(['Files from ' resultsFolder_case ' have been copied to ' resultsFolder_final]);
    else
        error(['Error copying files from ' resultsFolder_case ' to ' resultsFolder_final]);
    end

    %% Enter folders
    originFolder = cd(folders(ii).name);
    disp(['Loading: ' folders(ii).name]);
    %% Process motions
    if import_motions
        % Read the translation and orientation data from the input files
        t_vs_cm = readtable(fullfile(subfolder_data,fileName_translations),'Format','%f %f %f %f');
        t_vs_orientation = readtable(fullfile(subfolder_data,fileName_rotations),'Format','%f %f %f %f %f %f %f %f %f %f');
        
        for jj = 1:3
            t_vs_cm = t_vs_cm(~isnan(table2array(t_vs_cm(:,jj+1))),:);
            t_vs_orientation = t_vs_orientation(~isnan(table2array(t_vs_cm(:,jj+1))),:);
        end

        index = (t_vs_cm.Var1 >= 4 & t_vs_cm.Var1 <= 10);

        orientation = t_vs_orientation(:,2:end);
        % Calculate the Euler angles
        [xi_4, xi_5, xi_6] = getEulerAngles(table2array(orientation));

        % Create table for motions data
        motions = table(t_vs_cm.Var1, ...
            t_vs_cm.Var2 - t_vs_cm.Var2(1), ... % minus the initial possition
            t_vs_cm.Var3 - mean(t_vs_cm.Var3(index)), ...
            t_vs_cm.Var4 - mean(t_vs_cm.Var4(index)), ...
            xi_4, xi_5, xi_6, ...
            'VariableNames', {'t', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'});
    end

    %% Process forces and Moments
    % Process forces and moments data if import_forces_moments flag is set to 1
    if import_forces_moments

        % Initialize temporary forces data structure
        data_forces_temp = struct;

        % Loop through the force and moment data files
        for jj = 1:length(fileName_forces)

            % Read in the data from the force file and store it in a temporary table
            file_path = fullfile(subfolder_data, fileName_forces(jj));
            temp_data = readtable(file_path, 'Format', '%f %f %f %f');

            % Create dynamic field name and store the force data in the temporary structure
            field_name = matlab.lang.makeValidName(fileName_forces(jj));
            data_forces_temp.(field_name) = temp_data;
            clear file_path temp_data field_name

            % Read in the data from the moment file and store it in a temporary table
            file_path = fullfile(subfolder_data, fileName_moments(jj));
            temp_data = readtable(file_path, 'Format', '%f %f %f %f');

            % Create dynamic field name and store the moment data in the temporary structure
            field_name = matlab.lang.makeValidName(fileName_moments(jj));
            data_forces_temp.(field_name) = temp_data;
            clear file_path temp_data field_name
        end
        % Calculate the forces by summing the pressure, viscous, and porous forces
        % from the temporary data structure for each of the six components
        t = data_forces_temp.t_vs_forces_porous.Var1;
        forces_moments = ["forces", "moments"];
        f = zeros(size(data_forces_temp.t_vs_forces_porous, 1), 6);
        for jj = 1:6
            index = mod(jj,3) + 1;
            index(index==1) = 4;
            f(:, jj) = sum(table2array(data_forces_temp.(strcat('t_vs_', forces_moments(ceil(jj/3)), '_porous'))(:, index)) ...
                + table2array(data_forces_temp.(strcat('t_vs_', forces_moments(ceil(jj/3)), '_pressure'))(:, index)) ...
                + table2array(data_forces_temp.(strcat('t_vs_', forces_moments(ceil(jj/3)), '_viscous'))(:, index)), 2);
        end
        forces = table(data_forces_temp.t_vs_forces_porous.Var1, f(:,1), f(:,2), f(:,3), f(:,4), f(:,5), f(:,6), ...
            'VariableNames', {'t', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6'});

        % If import_forces_moments flag is set to 0, set the temporary data
        % structure to empty
    else
        data_forces_temp = [];
    end

    %% Process water surface elevation
    if import_waveGauges
        % Read in data from file
        for jj = 1:length(fileName_waveGauges)
            file_path(jj) = fullfile(subfolder_se, fileName_waveGauges(jj));
            data_SE{jj} = readtable(file_path(jj),'Format', '%f %f');
        end
        % Create a new table with the desired columns and rename them
        SE = table(data_SE{1}.Var1, ...
            data_SE{1}.Var2, ...
            data_SE{2}.Var2, ...
            data_SE{3}.Var2, ...
            data_SE{4}.Var2, ...
            'VariableNames', {'Time', 'WG1','WG2','WG3','WG4'});
    else
        SE = [];
    end

    %% Save the output data to a .mat file
    save(fullfile('..',output_folder, [folders(ii).name '.mat']), 'motions', 'forces', 'SE');
    disp([folders(ii).name '.mat file has been save in directory: ' fullfile('..',output_folder)]);

    %% Change back to the original folder
    cd(originFolder);
end
%% End of the file
toc