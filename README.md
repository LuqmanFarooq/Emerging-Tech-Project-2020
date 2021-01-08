# Emerging-Tech-Project-2020

## Description
A web service that uses machine learning to make predictions based on the data set powerproduction and respond with predicted power values based on speed values sent as HTTP requests. it uses a model trained with keras that accurately predicts wind turbine power output from wind speed values, as in the data set. 

## Repository Contents
* Jupyter notebook that trains a model using the data set.
* Python script "web-service.py" that runs a web service based on the model, as above.
* static folder that contains css stylesheet used in index.html and java script for predictions.
* template folder which contains index.html that is rendered by web-service.py
* Dockerfile to build and run the web service in a container.

## How to Run

* Clone the git repository.
* Open a terminal or command prompt and navigate to model folder in the cloned repository folder.
* Run command: python install -r requirements.txt
```bash
set FLASK_APP=web-service.py
python -m flask run
```
* Open a browser and navigate to: http://127.0.0.1:5000
* Use the app to get predictions.

## How to Run in Docker
* docker build -t predict-image
docker run --name predict-container -d -p 5000:5000 predict-image
* Open a browser and navigate to: http://127.0.0.1:5000
* Use the app to get predictions.
