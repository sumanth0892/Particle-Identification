import os 
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

def getData():
	path = '/Users/computer/Documents/particleIdentification/pid-5M.csv'
	data = pd.read_csv(path)
	targets = data['id']
	data = data.drop(columns = ['id'])
	return data,targets


