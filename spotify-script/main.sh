#!/bin/bash

plid="5kOan1EgvpdFnI6Q15vWwd"
token="BQCSkzBJRwYK1oCoEczHntsdqJEifClaEnUhBO88spJIr-n_VPEMALSTG_MnH3QmF3bbC1i-L6FA8nj-Yn1QyrtGI2oDKe4wc-sUWRr5_-EcE3d-NmVzj6V15r4bsaTQGVpP9LTwrk_e"
targ="https://api.spotify.com/v1/playlists/"$plid"/tracks?fields=items(track.id)"
curl -X "GET" $targ -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer "$token > playlistIDs.txt
grep -oE '[[:alnum:]]{22}' playlistIDs.txt > trackIDs.txt

while read p; do
	curl -X "GET" "https://api.spotify.com/v1/audio-features/"$p -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer "$token >> features.txt
done <trackIDs.txt
