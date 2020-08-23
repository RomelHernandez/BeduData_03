import requests
# CONSTANTS
DATASET_URL = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
response = requests.get(DATASET_URL)