## Table of contents
- 1 Installation
- 2 Project Motivation
- 3 File descriptions
- 4 Licensing, Authors, Acknowledgements

## 1 Installation
All libraries used in this code should be used in the standard Anaconda distribution of Python.
The Python version used writing the code was 3.9, therefore there should be no issues with running the code
using Python version 3.*.

## 2 Project Motivation
This data transformation pipeline was built during the [MHP mobility hackathon](https://www.mhp.com/de/mobility-hack-2022).
It was used to read in the output of the urban traffic simulation software [SUMO](https://www.eclipse.org/sumo/). The output of the code is a well-structured .csv file
that might be easily reusable for e.g. training of Machine Learning Models. In the hackathon we used it for training a
Reinforcement Learning Model.

## 3 File descriptions

- `data_pipeline.py`: Contains the Python code for data tranformation
- `sample_input_emissions.xml`: Contains the emissions data of a SUMO simulation
- `sample_input_full.xml`: Contains the full data output of a SUMO simulation

## 4 Licensing, Authors, Acknowledgements
Feel free to use the code in this repository as you would like.

