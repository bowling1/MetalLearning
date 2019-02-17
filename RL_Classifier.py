import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from numpy import mean
import matplotlib.pyplot as plt 
import seaborn as sns

'''
This code creates a model of the Metal spreadsheet I have slowly filled. It's output is how likely I'd relisten to an album,
which is based on my own relistening stats from a 2-week period of only relistening.

The Good: Fast, executes in just a few seconds. Decently accurate on this dataset.

The Bad: Maybe subject to overfitting due to not including a maximum node count in the RandomForest (too low may make it too
		 heavy on few variables). Judges crappy albums pretty fairly, usually around 0 (some maybe too high, but good albums 
		 are definitely rated lower than I'd like (~10%)

Possible changes: Adjust model to include test data after MAE is looked at. Possibly limit nodes in RandomForest to prevent overfitting.
				  Filter warnings just for output clarity. Adjust weighting of the input variables if possible.
'''

# The csv is turned into a pandas dataframe called "df"
df = pd.read_csv('C:\\git\\MetalRater\\Metal Sheet 2 - Sheet1 - TEST.csv', encoding="ISO-8859-1")

# The x and y are defined (x = features, y = y)
features = ["Emotion", "Solid", "Variety", "Length (mins)"]
y = df["RL"]

# Splits data into 4 data groups. In the future, maybe include this in a function to try multiple seeds to reduce overfitting to test data (if adjusting by MAE)
train_X, test_X, train_y, test_y = train_test_split(df[features], y, test_size=0.2, random_state=1)

# Tests the Mean Absolute Error to judge quality of the training model vs the test set
def get_mae(train_x, train_y, val_x, val_y):
	model1 = RandomForestRegressor()
	model1.fit(train_x, train_y)
	predict = model1.predict(val_x)
	val_mae = mean_absolute_error(predict, val_y)
	return val_mae

 # Input: Training data (train_X, train_y), Predictor values of the album you want to predict (target_X), How mnay iterations of the forest to run through (randomness)
 # Output: The y to the predictors that were inputted
 # Purpose: Get more precise output from multiple random seeds in a Random Forest
 # Notes: Only use one x input at a time
def super_random_forest(target_X, train_X, train_y, randomness):
	outputs = []
	for i in range(randomness):
		model = RandomForestRegressor(random_state=i)
		model.fit(train_X, train_y)
		outputs.append(model.predict(target_X))
	return mean(outputs)

# Plots data using seaborn, with line of best fit on a scatterplot
def plot_data(x, y):
	sns.regplot(x, y)
	plt.show()

# Input: Rating stats of the album
# Output: How likely you are to relisten, and estimated times you will relisten
# Notes: Bread and butter of this program. Seems to aim too low (Esoteric Malacology got 71%, should be in the high 80%)
#		 Also seems to output a lot of FutureErrors, which is annoying. Tried removing them with error filtering but that caused other issues
def album_stats(Emotion, Solid, Variety, Length):
	target_X = df[features].iloc[[1]]
	target_X["Emotion"][1] = Emotion
	target_X["Solid"][1] = Solid
	target_X["Variety"][1] = Variety
	target_X["Length (mins)"][1] = Length
	print(target_X)
	#print("The amount of times I'll relisten to this is: " + str(super_random_forest(target_X, train_X, train_y, 20)))
	print("The chance of me relistening to this is: " + str((0.5**(super_random_forest(target_X, train_X, train_y, 20)**-1))*100))

# Test input
#album_stats(4,5,3,40)