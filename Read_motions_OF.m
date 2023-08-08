%-------------------------------------------------------------------------
% Description: This MATLAB code reads data from multiple files representing
% the wave-induced motion of a floating object. The data includes
% translations, rotations, velocity, acceleration, angular momentum, and
% torque. The code extracts the desired parameters from each file and saves
% them to separate output files.
%
% Author: Shuijin Li
% Date: 25 May 2023
% Email: skli@dundee.ac.uk
%
% Usage: 
% 1. Ensure that the input files are located in the specified directory
%    structure.
% 2. Modify the 'time_steps' array to match the desired time steps.
% 3. Run the code in MATLAB.
%
% Inputs: None
%
% Outputs: 
% - Output files containing the extracted data for translations, rotations,
%   velocity, acceleration, angular momentum, and torque.
%
%-------------------------------------------------------------------------

% Define the time step array
time_steps = 0.05:0.05:12;

% Initialize the output data matrices
translations = [];
rotations = [];
velocity = [];
acceleration = [];
angularMomentum = [];
torque = [];

% Loop through each time step directory
for t = time_steps
    % Construct the file path
    file_path = sprintf('%g/uniform/sixDoFRigidBodyMotionState', t);

    % Open the file
    fileID = fopen(file_path, 'r');

    % Read the file line by line
    while ~feof(fileID)
        line = fgetl(fileID);

        % Extract the desired parameters
        if contains(line, 'centreOfRotation')
            translations = [translations; sscanf(line, 'centreOfRotation ( %g %g %g )')'];
        end
        if contains(line, 'orientation')
            rotations = [rotations; sscanf(line, 'orientation ( %g %g %g %g %g %g %g %g %g )')'];
        end
        if contains(line, 'velocity')
            velocity = [velocity; sscanf(line, 'velocity ( %g %g %g )')'];
        end
        if contains(line, 'acceleration')
            acceleration = [acceleration; sscanf(line, 'acceleration ( %g %g %g )')'];
        end
        if contains(line, 'angularMomentum')
            angularMomentum = [angularMomentum; sscanf(line, 'angularMomentum ( %g %g %g )')'];
        end
        if contains(line, 'torque')
            torque = [torque; sscanf(line, 'torque ( %g %g %g )')'];
        end
    end

    % Close the file
    fclose(fileID);
end

% Save the data to files if the strings exist
if exist('translations', 'var')
    t_vs_cm = [time_steps' translations];
    dlmwrite('t_vs_cm.txt', t_vs_cm, 'delimiter', ' ', 'precision', '%g');
end

if exist('rotations', 'var')
    t_vs_orientation = [time_steps' rotations];
    dlmwrite('t_vs_orientation.txt', t_vs_orientation, 'delimiter', ' ', 'precision', '%g');
end

if exist('velocity', 'var')
    t_vs_lv = [time_steps' velocity];
    dlmwrite('t_vs_lv.txt', t_vs_lv, 'delimiter', ' ', 'precision', '%g');
end

if exist('acceleration', 'var')
    t_vs_a = [time_steps' acceleration];
    dlmwrite('t_vs_a.txt', t_vs_a, 'delimiter', ' ', 'precision', '%g');
end

if exist('angularMomentum', 'var')
    t_vs_aM = [time_steps' angularMomentum];
    dlmwrite('t_vs_aM.txt', t_vs_aM, 'delimiter', ' ', 'precision', '%g');
end

if exist('torque', 'var')
    t_vs_torque = [time_steps' torque];
    dlmwrite('t_vs_torque.txt', t_vs_torque, 'delimiter', ' ', 'precision', '%g');
end


