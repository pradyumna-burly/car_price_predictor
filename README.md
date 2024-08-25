# Car Price Predictor
Welcome to the Car Price Prediction project! This repository contains the code and resources for a machine learning application designed to predict car prices based on various features. Below you'll find an overview of the project, its components, and how to get started.
![](https://github.com/pradyumna-burly/car_price_predictor/blob/main/static/images/web%20interface.png)

# Project Overview
The Car Price Prediction project leverages a linear regression model to estimate the price of cars. It includes a web interface for users to input car features and receive price predictions. The model has been trained using historical car data and is packaged for deployment in a Python web application.

# Project Structure
Here's a breakdown of the files and directories included in this repository:

# HTML/CSS:

1. index.html: The main HTML file that provides the structure of the web interface.
2. styles.css: The CSS file used to style the web interface.

# Application Code: 
application.py: The main Python script that runs the web application using Flask. It handles user inputs, interacts with the linear regression model, and renders predictions.

# Model:
linearregressionmodel.pkl: The serialized linear regression model used for making predictions. This file is loaded by application.py to provide car price estimates.

# Data:
cleaned_data.csv: The cleaned dataset used for training the linear regression model. This file contains historical data on car features and prices.

# Notebook:
notebook.ipynb: A Jupyter Notebook that details the data analysis and model training process. This notebook includes code for data preprocessing, feature selection, model training, and evaluation.

# Final Outcome:
Now our model is fully ready to display predicted price. Based on the features selected by the user, the regression model make a API call to the pickle file of the model and in return the file gives the predicted output, the same will be displayed on the html webpage. Here is a small demo
![](https://github.com/pradyumna-burly/car_price_predictor/blob/main/static/images/price_prediction.png)

# Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes and commit them (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a pull request.
