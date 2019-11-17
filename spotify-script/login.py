import pprint
import sys
import spotipy
import spotipy.util as util


client_id = 'd02535ac05c14639beceb6d302177372'
client_secret = '87b07a1e938f4a76a2c2affe86a47e22'
redirect_uri = 'http://localhost:8080'
#
username = "johntyro"
playlist_id = {};
track_ids = ["5G8l9egOs7B3sYC6JT7bEL"]

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
playlist_id = {};
if token:
    sp = spotipy.Spotify(auth=token)
    playlist_id = sp.user_playlist_create(username, "Agapame Voss", True) ['id']
else:
    print ("Can't get token for", username)

sp.user_playlist_add_tracks(username, playlist_id, track_ids)
