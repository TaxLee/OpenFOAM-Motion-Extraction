# OpenFOAM-Motion-Extraction

This repository contains a collection of scripts for extracting motion data from OpenFOAM log files. The main script, `run_post_SL.sh`, automates the process of running the other scripts and should be the only one that needs to be executed.

## Usage

To use these scripts, simply run `run_post_SL.sh` in your terminal. This will call the other scripts in the correct order to extract motion data from your OpenFOAM log files.

If you encounter an error when running `createWGs_T150.py`, you can uncomment line 44 of the code: `# casefoam.CaseType = 'Decomposed Case'` to let the program read the decomposed files instead of the reconstructed files.

## Scripts

Here is a brief overview of each script in this repository:

- `run_post_SL.sh`: This is the main script that automates the process of running all other scripts. Simply execute this script to extract motion data from your OpenFOAM log files.
- `Motion_Extraction.sh`: This script extracts relevant motion data from OpenFOAM log files.
- `createWGs_T150.py`: This Python script creates wave gauges for cases with a wave period of 1.50 s.
- `extractSE.py`: This Python script extracts stress equilibrium data from OpenFOAM log files.

Each script includes comments and documentation within its code to explain its functions and how to use it.

## License

This repository is licensed under [MIT License](https://github.com/github/choosealicense.com/blob/gh-pages/LICENSE.md).

## Contributions

Contributions are welcome! If you have any suggestions or improvements for these scripts, please feel free to submit a pull request or open an issue on Github.
