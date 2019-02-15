# Docker_Graydon
Experiment with Docker for Graydon Data

This project has the python code and 2017 decision tree model file for producing the probability that a company moves, given the features. 

The WebAPI directory has the python script, model file, Dockerfile for creating the docker container for running a Web API.  
To build the image and run an the container, execute the following:

> sudo docker build -t web_api:latest .

> sudo docker run -d -p 5000:5000 web_api

Then open a browser and navigate to
http://127.0.0.1:5000/

In the "company features" input box, paste one line of features to get the probability.  
Features values can be taken from one row of the file PythonCommandLine/companies_with_features.csv.
