#!/bin/bash

################################################################################
# Description:
#
# This script extracts relevant motion data from OpenFOAM log files. It
# utilizes commands to extract the center of mass, linear and angular velocities,
# orientation, spring length, and courant number data, along with forces and
# moments data in separate files. The script organizes the data by time steps
# and performs error-checking, dependency verification, and automatic deletion of
# intermediate files. It also provides progress updates to the terminal. The code
# is written in Bash, a common shell language for Unix-based systems, making it
# compatible with various environments. This script is a powerful tool for
# efficiently extracting accurate and error-free motion data from OpenFOAM log
# files.
#
# Dependencies:
#
# This script requires the following dependencies to be installed: grep, cut, tr,
# paste, and rm.
#
# Usage:
#
# This script can be run with the following command:
#
#     $ ./Motion_Extraction.sh
#
# Author:
#
# Author: Shuijin Li
# Email: skli@dundee.ac.uk
#
# Date:
#
# 11 Mar 2023
#
################################################################################

echo "#########################  Motion_Extraction.sh  #########################"

# Define constants
# readonly LOG_FILE_PATH="$1"
# readonly OUT_DIR_PATH="$2"
readonly LOG_FILE_PATH="log"
readonly OUT_DIR_PATH="output"

# Check if the output directory exists, create it if not
if [ ! -d "$OUT_DIR_PATH" ]; then
    mkdir -p "$OUT_DIR_PATH"
    echo "Output directory created successfully"
else
    echo "Output directory already exists"
fi

# Check that required dependencies are installed
check_dependencies() {
    local dependencies=("grep" "cut" "tr" "paste" "rm")
    for dependency in "${dependencies[@]}"; do
        if ! command -v "$dependency" > /dev/null; then
            echo "Error: $dependency command not found!"
            exit 1
        fi
    done
}

# Check that the input log file exists
check_log_file() {
    if [[ ! -f "$LOG_FILE_PATH" ]]; then
        echo "Error: log file not found!"
        exit 1
    else 
        echo "Reading $LOG_FILE_PATH ..."
    fi
}

# Extract the required parameters from the log file
extract_parameters() {
    # Centre of mass
    echo "Extracting centre of mass ..."
    grep "Centre of mass" "$LOG_FILE_PATH" | cut -d ":" -f 2 | tr -d "()" | awk 'NR%4==0' > "$OUT_DIR_PATH/temp_cM.txt"

    # Linear velocity
    echo "Extracting linear velocity ..."
    grep "Linear velocity" "$LOG_FILE_PATH" | cut -d ":" -f 2 | tr -d "()" | awk 'NR%4==0' > "$OUT_DIR_PATH/temp_lV.txt"

    # Angular velocity
    echo "Extracting angular velocity ..."
    grep "Angular velocity" "$LOG_FILE_PATH" | cut -d ":" -f 2 | tr -d "()" | awk 'NR%4==0' > "$OUT_DIR_PATH/temp_aV.txt"

    # Orientation
    echo "Extracting orientation ..."
    grep "Orientation" "$LOG_FILE_PATH" | cut -d ":" -f 2 | tr -d "()" | awk 'NR%4==0' > "$OUT_DIR_PATH/temp_orientation.txt"

    # Spring length
    echo "Extracting spring length ..."
    grep "spring length" "$LOG_FILE_PATH" | cut -d ":" -f 2 | awk 'NR%4==0' > "$OUT_DIR_PATH/temp_fO.txt"

    # Courant number
    echo "Extracting courant number ..."
    grep "max" "$LOG_FILE_PATH" | cut -d ":" -f 3 | awk 'NR%4==0' > "$OUT_DIR_PATH/temp_coNumber.txt"

    # Time
    echo "Extracting time steps ..."
    grep -e "^Time = " "$LOG_FILE_PATH" | cut -d " " -f 3 > "$OUT_DIR_PATH/temp_times.txt"
}

# Extract the forces and moments data from the log file
extract_forces_moments() {
    local forces_temp_name=("pressure" "viscous" "porous")
    for force in "${forces_temp_name[@]}"; do
        # Extract raw data
        echo "Extracting $force forces and moments..."
        grep "$force" "$LOG_FILE_PATH" | cut -d ":" -f 2 | tr -d '()' > "$OUT_DIR_PATH/temp_${force}.txt"

        # Save even and odd lines to separate files
        awk 'NR%2==1' "$OUT_DIR_PATH/temp_${force}.txt" > "$OUT_DIR_PATH/temp_forces_${force}.txt"
        awk 'NR%2==0' "$OUT_DIR_PATH/temp_${force}.txt" > "$OUT_DIR_PATH/temp_moments_${force}.txt"

        # Print variables for debugging
        # printf "forces_%s: %s\n" "$OUT_DIR_PATH/$force" "$(cat "$OUT_DIR_PATH/temp_forces_${force}.txt")"
        # printf "moments_%s: %s\n" "$OUT_DIR_PATH/$force" "$(cat "$OUT_DIR_PATH/temp_moments_${force}.txt")"
    done
}

paste_forces_moments() {
    # Paste times and forces/moments into separate files
    local contributions=("pressure" "viscous" "porous")
    for force in "${contributions[@]}"; do
        # Use loop to create files with pasted data
        echo "Saving time-series file of $force forces ..."
        eval "paste \"$OUT_DIR_PATH/temp_times.txt\" \"\$OUT_DIR_PATH/temp_forces_$force.txt\" > \"\$OUT_DIR_PATH/t_vs_forces_${force}.txt\""
        echo "Saving time-series file of $force moments ..."
        eval "paste \"$OUT_DIR_PATH/temp_times.txt\" \"\$OUT_DIR_PATH/temp_moments_$force.txt\" > \"\$OUT_DIR_PATH/t_vs_moments_${force}.txt\""
    done
}

paste_parameters() {
    # Paste times and parameters into separate files
    echo "Saving time-series file of centre of mass as "t_vs_cm.txt" ..."
    paste "$OUT_DIR_PATH/temp_times.txt" "$OUT_DIR_PATH/temp_cM.txt" > "$OUT_DIR_PATH/t_vs_cm.txt"
    echo "Saving time-series file of linear velocity as "t_vs_lv.txt" ..."
    paste "$OUT_DIR_PATH/temp_times.txt" "$OUT_DIR_PATH/temp_lV.txt" > "$OUT_DIR_PATH/t_vs_lv.txt"
    echo "Saving time-series file of angular velocity as "t_vs_aV.txt" ..."
    paste "$OUT_DIR_PATH/temp_times.txt" "$OUT_DIR_PATH/temp_aV.txt" > "$OUT_DIR_PATH/t_vs_aV.txt"
    echo "Saving time-series file of orientation as "t_vs_orientation.txt" ..."
    paste "$OUT_DIR_PATH/temp_times.txt" "$OUT_DIR_PATH/temp_orientation.txt" > "$OUT_DIR_PATH/t_vs_orientation.txt"
    echo "Saving time-series file of spring length as "t_vs_fO.txt" ..."
    paste "$OUT_DIR_PATH/temp_times.txt" "$OUT_DIR_PATH/temp_fO.txt" > "$OUT_DIR_PATH/t_vs_fO.txt"
    echo "Saving time-series file of courant number as "t_vs_coNumber.txt" ..."
    paste "$OUT_DIR_PATH/temp_times.txt" "$OUT_DIR_PATH/temp_coNumber.txt" > "$OUT_DIR_PATH/t_vs_coNumber.txt"
}

clean_up() {
    # Remove temporary files
    rm "$OUT_DIR_PATH"/temp_*.txt
    echo "###############################################################################"
    echo "#    Finish extract data from $LOG_FILE_PATH file. Results are save in "$OUT_DIR_PATH" folder.    #"
    echo "#    🎉🎉🎉 Congratulations! The script has completed successfully! 🎉🎉🎉    #"
    echo "###############################################################################"
}

# Main script

check_dependencies
check_log_file
extract_parameters
extract_forces_moments
paste_parameters
paste_forces_moments
clean_up