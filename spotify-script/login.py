# This script logs in to spotify and creates a specific playlist so far - TODO: extend this

import pprint
import sys
import spotipy
import spotipy.util as util
from json_sorter import bestFit

client_id = 'd02535ac05c14639beceb6d302177372'
client_secret = '87b07a1e938f4a76a2c2affe86a47e22'
redirect_uri = 'http://localhost:8080'

def createPlaylist(username, moods):

	scope = 'playlist-modify-public'
	playlist_id = {};
	track_ids = bestFit(moods)

	token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

	playlist_id = {};
	if token:
	    sp = spotipy.Spotify(auth=token)
	    playlist_id = sp.user_playlist_create(username, "Your current mood", True) ['id']
	else:
	    print ("Can't get token for", username)

	sp.user_playlist_add_tracks(username, playlist_id, track_ids)

createPlaylist("johntyro",[])