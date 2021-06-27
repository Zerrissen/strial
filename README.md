# STrial - Statistical Trial ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Zerrissen/strial?style=flat-square) ![Tested Python Version (latest by date)](https://img.shields.io/badge/python-3.8-blue?style=flat-square) [![GitHub license](https://img.shields.io/github/license/Zerrissen/strial?style=flat-square)](https://github.com/Zerrissen/strial/blob/main/LICENSE)
###### This is a tool developed for a school assessment and is not made for use in real statistical simulations. Use at your own risk.

If you are here for help with running the program, please continue reading.

## Installation
Tested on Python 3.8.10, Windows 10

This tool requires a small number of external modules to be installed.
```
pip install -r requirements.txt
```
If the above doesn't work, indivdually install the following modules:
```
pip install numpy
pip install matplotlib
pip install pyfiglet
pip install colorama
```

## Usage
Upon running the program, you will be notified of the following:
- Current version
- Author
- Trial Completion Criteria
- Quick disclaimer

The trial completion criteria is currently limited until future releases.

You will be prompted with "How many trials do you want to run?"
This can be any number above 0, however for statistical purposes you should use a minimum of 50.
Note that any number over 10,000 will likely take an excess of 10 minutes (tested with max freq of 12, using 5 possible outcomes). A higher maximum frequency or higher outcome count will take longer to simulate.

You will now be prompted with "What is the maximum outcome frequency?"
This is the maximum number of times an integer can be generated PER TRIAL.

You will now be prompted with "How many outcomes are there?"
These are the possible outcomes that can occur, and are each assigned numbers after probabilities for each outcome are given. A tally will be kept of how many times each outcome has occurred.

You will now be asked to label your outcomes. Please seperate each label with spaces, as this uses the split() method and will see each space as a seperator. There is currently no input validation; what you enter is final.

For each outcome label you will be asked to give a probability. This must be between 0-1 (there is input validation on this). The final outcome will automatically be given the remaining possible probability to reduce human error.

Once all inputs have been given, the program will begin the simulation and each trial will run and be recorded. After the simulation is complete, three graphs will be drawn and displayed, and the mean count of generated numbers (frequency) before trial completion will be displayed in the command-line.

## Still confused?
If you are still confused, it is likely because you are not a target user or because you are unaware of how statistical simulations work. For reference, please see the following document: [Level 2 simulation workbook.docx](https://github.com/Zerrissen/strial/files/6721437/Level.2.simulation.workbook.docx)
