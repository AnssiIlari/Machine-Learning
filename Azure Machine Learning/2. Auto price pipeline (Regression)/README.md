# Created a pipeline

Azure's sample dataset "Automobile price data"

### Data preprocessing

-removed one column with too much missing values

-missing values removed from ("bore", "stroke" and "horsepower")

-data normalized

## Model build

-Split the data

-Linear regression

-Train Model (Label column: price)

Score Model & Evaluate model

![model](https://github.com/AnssiIlari/Azure-Machine-Learning/assets/127083657/758fd5b8-052b-44d3-a842-6bbc3e453759)

![modelmetrics](https://github.com/AnssiIlari/Azure-Machine-Learning/assets/127083657/66b1af61-22d8-4dff-98f3-bd4915628fd3)

# Infrerence Pipeline

![InferencePipeline](https://github.com/AnssiIlari/Azure-Machine-Learning/assets/127083657/4aa7d0a8-6d46-41bc-b2cf-48f3f413e580)

-Replaced Automobile price data (RAW) with Enter Data manually, withouth price column

-Removed references to price column from Select Columns in Dataset

-Removed Evaluate model

-Added Excecute Python Script (selects only the Scored Labels column and renames it to predicted_price)

-Data transformations made in a different way

-Deployed inference model to endpoint

-Tested out the inference with a code where I sent car details to the inference and returned me the prediction.

![dataforprediction](https://github.com/AnssiIlari/Azure-Machine-Learning/assets/127083657/b1abfc34-8899-4b35-a963-e4a5854e83e0)


![prediction](https://github.com/AnssiIlari/Azure-Machine-Learning/assets/127083657/c64c28c8-d924-4e63-9679-371f842dbc24)

