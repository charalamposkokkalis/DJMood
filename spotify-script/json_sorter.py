# This script sorts the json data and returns a list of the ids of the top-n songs
# according to the function suit in fit_function.py

import json
import pprint
from fit_function import suit

def bestFit(parameters):
	with open('dataset.txt') as json_file:
	    data = json.load(json_file)

	data = data[11:]
	songs = []

	# these are to be imported (they are the output of sentiment_analysis)
	parameters = [1, 1, 0, 0, 0, 0]

	for i in range(0,len(data)):
	    data[i] = data[i][0] # getting rid of the extra arrays
	    data[i]['fit'] = suit(data[i],parameters)
	    songs.append([data[i]['fit'], data[i]['id']])

	songs = sorted(songs)

	top_songs = songs[-50:] # gets 50 songs with highest fitness function
	top_songs = [tup[1] for tup in top_songs] # keeps just their id
	return top_songs

