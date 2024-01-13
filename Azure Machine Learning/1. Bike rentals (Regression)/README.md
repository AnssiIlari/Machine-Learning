# This was a task done with Automated ML. The task was to predict bike rentals based on given criteria.

##### Material for training the model was in a basic and small .csv file. (Included)

### Few run settings: Target column: rentals, Task type: Regression, Primary metric: Normalized root mean square error, Explain best model
### Exit criterion: Training job time (hours): 0.25
### Metric score threshold: 0.08
### Enable featurization: selected

##### Next I ran the submitted the ran and after I while run ended when hitting the metric score threshold.

### Best model summary: MaxAbsScaler, LightGBM

##### Next I deployed the model to a endpoint with Azure container instance.
##### I tested the end point in the notebooks section. (notebook included)

![modelprint](https://github.com/AnssiIlari/Azure-Machine-Learning/assets/127083657/4112dc31-b223-4859-9c21-28916c9a5803)

#Works fine!
