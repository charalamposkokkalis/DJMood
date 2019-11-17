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
#  (happy, angry, excited, sad, scared, bored) each in [0,1]

#  happy -> loudness, energy, speechiness, danceability, valence (!!)
#  excited -> loudness, energy(!!), speechiness, danceability(!), valence, tempo
#  angry -> loudness, instrumentalness(!), valence, tempo (slow)
#  sad -> energy, instrumentalness (!), liveness (?), valence(!!)
#  scared -> loudness (low), instrumentalness, valence, tempo (low)
#  bored -> energy(!!), loudness, speechiness, valence, tempo (high)

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

def suit(song, happy, angry, excited, sad, scared, bored):
		h1  = happy*(song['loudness'] + song['energy'] + song['speechiness']*0.5 + song['danceability'] + 3*song['valence'] + song['tempo']/150)
		e1  = excited*(song['loudness'] + 3*song['energy'] + song['speechiness']/2 + 2*song['danceability'] + song['valence'] + song['tempo']/50 )
		a1  = angry*(-song['loudness']/2 + 2*song['instrumentalness'] + 2*song['valence'] + 200/song['tempo'])
		sa1 = sad*(song['energy'] + 2*song['instrumentalness'] + 3*song['valence'] + song['danceability']/2 + song['tempo']/150)
		sc1 = scared*(1/song['loudness'] + song['instrumentalness'] + 2*song['valence'] + 200/song['tempo'])
		b1  = bored*(3*song['energy'] + 1.5*song['loudness'] + song['speechiness'] + song['valence'] + song['tempo']/50) 
		return(h1+e1+a1+sa1+sc1+b1)


tracks = download();
features = extractFeat(download());
ratings = []
ids_sorted=[]
for i in range(0,len(features)):
	ratings.append(suit(features[i][0], 0.251, 0.177, 0.246, 0.138, 0.158, 0.0287))
	ids_sorted.append((features[i][0])['id'])
ratings, ids_sorted = (list(x) for x in zip(*sorted(zip(ratings, ids_sorted), key=lambda pair: pair[0])))
ids_sorted.reverse()
print(ids_sorted)


'''
features = sorted(features, key = lambda i: i[0]['valence'])

for i in range(0,len(features)):
	print(features[i][0]['id'])
'''