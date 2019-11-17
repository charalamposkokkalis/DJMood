# Better solutions have higher suit value returned
def suit(song, happy, angry, excited, sad, scared, bored):
    h1  = happy*(song['loudness'] + song['energy'] + song['speechiness']*0.5 + song['danceability'] + 3*song['valence'] + song['tempo']/150)
    e1  = excited*(song['loudness'] + 3*song['energy'] + song['speechiness']/2 + 2*song['danceability'] + song['valence'] + song['tempo']/50 )
    a1  = angry*(-song['loudness']/2 + 2*song['instrumentalness'] + 2*song['valence'] + 200/(song['tempo']+1))
    sa1 = sad*(song['energy'] + 2*song['instrumentalness'] + 3*song['valence'] + song['danceability']/2 + song['tempo']/150)
    sc1 = scared*(1/song['loudness'] + song['instrumentalness'] + 2*song['valence'] + 200/(song['tempo']+1))
    b1  = bored*(3*song['energy'] + 1.5*song['loudness'] + song['speechiness'] + song['valence'] + song['tempo']/50) 
    return(h1+e1+a1+sa1+sc1+b1)

