# Project Title : 
IPL winning probability

## Description

This is the data of IPL from 2008 to 2019 and we have to find the probability of winning and loosing between two teams, this is the problem of classification but we want the probability so we are using only Logistic regression algorithm
I started this project by importing data, further i droped thus rows who have teams that are not planning in current IPL, then i created different column from existing columns, after getting required columns done some EDA and preprocessing where i removed some null rows and some unnecessary rows from dataset, then splitted data in Train and Test for model prediction and i have used Logistic Regression algorithm for model probability prediction.

## Table of Content
* Dataset Information
* Tools and Libraries Used
* Files
* Results
* Deployment
* Feedback

## Dataset Information
This is the data of IPL from 2008 to 2019 and we have to find the probability of winning and loosing between two teams.


## Tools and Libraries Used
* Pandas
* numpy
* Matplotlib
* Seaborn
* sklearn
* pickle
* json

## Files
This repository contain files as mentioned below:

* IPL_win_probability.ipynb : .ipynb file contains all the python code, documentation and visualization.

* deliveries.csv : Our dataset 

* project_data.json : Encoded data and columns names

* requirements.txt :contains required libraries 

* utils.py : Functions required for model Prediction

* config.py : Path of .pkl and .json file

* interface.py : Flask code 

## Results

* logistic Regression            : 0.7988

## Trial Dataset

batting_team = 'Delhi Capitals'

bowling_team =	'Chennai Super Kings'

city =	'Delhi'

runs_left = 10	

balls_left = 81	

wickets = 6

total_runs_x = 169	

crr	= 5.07

rrr	= 10.07

## Feedback

If you have any feedback, please reach out to us at trburade@gmail.com