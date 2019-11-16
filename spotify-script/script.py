import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials


#very dangerous to leave secret information here
client_credentials_manager = SpotifyClientCredentials(client_id='d02535ac05c14639beceb6d302177372',
                                                      client_secret='87b07a1e938f4a76a2c2affe86a47e22')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#list of Library playlists
lib = [("spotifycharts","37i9dQZEVXbMDoHDwVN2tF")]
features = ["danceability", "energy", "key", "loudness", "mode", "speechiness", 
					"acousticness", "instrumentalness", "liveness", "valence", "tempo"]
tracks = []


def download():
	results = sp.user_playlist("spotifycharts", "37i9dQZEVXbMDoHDwVN2tF", fields="tracks")
	return results['tracks']

def extractFeat(tr):
	trackIDs = []
	for i,item in enumerate(tr['items']):
	   track = item['track']
	   trackIDs.append(track['id']);
	return sp.audio_features(trackIDs);





tracks = download();
print(extractFeat(download()))