#!/bin/bash


#create a virtual environment
python3 -m venv translatoor

# activate the virtual environment
source translatoo/bin/activate  

# install necessary packages
pip install -r requirements.txt

# to turn off the virtual environment, run `deactivate`
# if pip brings about issues, its the dotenv package, just run `pip install python-dotenv`

# run the main python file
python3 main.py 
