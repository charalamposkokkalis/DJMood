# This is the script used to get the json data for the popular playlists - TODO: make sure it works properly
# so that we don't lose any data.

import spotipy
import sys
import json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

scope = 'user-library-read'
username = "johntyro"

SPOTIPY_CLIENT_ID = 'd02535ac05c14639beceb6d302177372'
SPOTIPY_CLIENT_SECRET = '87b07a1e938f4a76a2c2affe86a47e22'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'

#very dangerous to leave secret information here
client_credentials_manager = SpotifyClientCredentials(client_id='d02535ac05c14639beceb6d302177372',
                                                      client_secret='87b07a1e938f4a76a2c2affe86a47e22')

scope = 'user-library-read'
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#list of Library playlists

lib = [("spotifycharts","37i9dQZEVXbMDoHDwVN2tF")]

# 	danceability: 0.0 to 1.0
# 	loudness: 0.0 to 1.0
#	energy: 0.0 to 1.0
#	instrumentalness: 0.0 to 1.0 confidence it is instrumental
#	speechiness: 0.0 to 1.0 chance there are vocals
#	liveness: 0.0 to 1.0 performed live
#	valence: 0.0 to 1.0 happiness
# 	tempo: 
#	acousticness: acoustic
#  (happy, angry, excited, sad, scared, bored) each in [0,1]

#  happy -> loudness, energy, speechiness, danceability, valence (!!)
#  excited -> loudness, energy(!!), speechiness, danceability(!), valence, tempo
#  angry -> loudness, instrumentalness(!), valence, tempo (slow)
#  sad -> energy, instrumentalness (!), liveness (?), valence(!!)
#  scared -> loudness (low), instrumentalness, valence, tempo (low)
#  bored -> energy(!!), loudness, speechiness, valence, tempo (high)

features = ["danceability", "energy", "key", "loudness", "mode", "speechiness", 
					"acousticness", "instrumentalness", "liveness", "valence", "tempo"]


def download(usr, id):
	results = sp.user_playlist(usr, id, fields="tracks")
	return results['tracks']

def extractFeat(tr = []):
	# trackIDs = []
	feats = []
	for i,item in enumerate(tr['items']):
	   track = item['track']
	   #optimize 50
	   feats.append(sp.audio_features(track['id']))
	return feats

playlists = sp.user_playlists('spotify')
#print(playlists['items'][1]);

for playlist in playlists['items']:
	print("\n\n\n\n\n\n" + playlist['id'])
	tracks = download(playlist['owner']['id'], playlist['id'])
		
	for i in range(0, len(tracks['items'])):
		#print(tracks['items'][i]['track'])
		if(tracks['items'][i]['track'] is not None):
			features.append(sp.audio_features(tracks['items'][i]['track']['id']))

with open('features.txt', 'w') as outfile:
    json.dump(features, outfile)

