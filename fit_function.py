# This is a fitness function, showing how suitable a song is for the current emotion_vector
# Better solutions have higher suit value returned

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


def idealSong(emotion_vector):
    hap, ang, exc, sad, sca, bor = emotion_vector
    song = {}
    song['valence'] = (hap - sad)/2 + 0.5
    song['loudness'] = (max(ang, exc) - max(sad,bor))/2 + 0.5
    song['danceability'] = (exc - bor)/2 + 0.5
    song['energy'] = song['loudness']
    song['instrumentalness'] = bor
    song['speechiness'] = 1 - song['instrumentalness']
    return song


def suit(song, emotion_vector):
    happy, angry, excited, sad, scared, bored = emotion_vector
    h1  = happy*(song['loudness'] + song['energy'] + song['speechiness']*0.5 + song['danceability'] + 3*song['valence'] + song['tempo']/150)
    e1  = excited*(song['loudness'] + 3*song['energy'] + song['speechiness']/2 + 2*song['danceability'] + song['valence'] + song['tempo']/50 )
    a1  = angry*(-song['loudness']/2 + 2*song['instrumentalness'] + 2*song['valence'] + 200/(song['tempo']+1))
    sa1 = sad*(-song['energy']/3 + 2*song['instrumentalness'] + -song['valence']/3 - song['loudness']/4 + song['tempo']/150)
    sc1 = scared*(1/song['loudness'] + song['instrumentalness'] + 2*song['valence'] + 200/(song['tempo']+1))
    b1  = bored*(3*song['energy'] + 1.5*song['loudness'] + song['speechiness'] + song['valence'] + song['tempo']/50) 
    return(h1+e1+a1+sa1+sc1+b1)

