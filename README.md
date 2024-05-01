# [Rent Price prediction around UCSD](http://sunwoo10604.pythonanywhere.com/)

## Data Collection
- Used rapid API for data collection
[Check the API for data collection](https://rapidapi.com/ntd119/api/zillow-com4/)

> [!NOTE]  
> If you want to duplicate the process, please create a .env file and paste the API key that you created after subscribing API

## Model Development
- Please refer to model_dev/model_development.ipynb to follow through the process of model choice, variable decision, hyperparameter fine-tuning, and final development.

> [!NOTE]  
> Currently using SKLearn's Random Forest Regressor with the version of 1.3.0. It is important to use the same version in order to load the model. If not, please run model_dev/model_save.py to recreate the model with the intended version.
  

## Limitation
Model performance is not optimal when the given number of bedroom is lower than bathroom(though it is unlikely to happen in real life)
