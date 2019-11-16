import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials


#very dangerous to leave secret information here
client_credentials_manager = SpotifyClientCredentials(client_id='d02535ac05c14639beceb6d302177372',
                                                      client_secret='87b07a1e938f4a76a2c2affe86a47e22')
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


features = ["danceability", "energy", "key", "loudness", "mode", "speechiness", 
					"acousticness", "instrumentalness", "liveness", "valence", "tempo"]

tracks = []


def download():
	results = sp.user_playlist("spotifycharts", "37i9dQZEVXbMDoHDwVN2tF", fields="tracks")
	return results['tracks']

def extractFeat(tr):
	trackIDs = []
	feats = []
	for i,item in enumerate(tr['items']):
	   track = item['track']
	   #optimize 50
	   feats.append(sp.audio_features(track['id']))
	return feats;


tracks = download();
features = extractFeat(download());
features = sorted(features, key = lambda i: i[0]['valence'])

for i in range(0,len(features)):
	print(features[i][0]['id'])