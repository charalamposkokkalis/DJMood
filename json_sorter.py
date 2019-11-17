import json
import pprint
from fit_function import suit

with open('spotify-script/dataset.txt') as json_file:
    data = json.load(json_file)

data = data[11:]
songs = []

# these are to be imported (they are the output of sentiment_analysis)
# TODO - Turn into a vector
parameters = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

for i in range(0,len(data)):
    data[i] = data[i][0] # getting rid of the extra arrays
    data[i]['fit'] = suit(data[i],parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5])
    songs.append([data[i]['fit'], data[i]['id']])

songs = sorted(songs)

top_songs = songs[-50:] # gets 50 songs with highest fitness function
top_songs = [tup[1] for tup in top_songs] # keeps just their id
pprint.pprint(top_songs)

