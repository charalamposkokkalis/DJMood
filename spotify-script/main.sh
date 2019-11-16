#!/bin/bash

plid="5kOan1EgvpdFnI6Q15vWwd";
targ="https://api.spotify.com/v1/playlists/"$plid"/tracks?fields=items(track.id)"
curl -X "GET" $targ -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQA7q-pU25GZmyIbvE3t_9jLPk1un7_-prAYSXJ5BHp_NlYZvTjIevlxlr5ZnxBDrYvG06oM2skfuAI6PR7V3RXCKEbaiqLcnR1AQDftWt5mHKfZiss2qVoVzEXaV-sxW_PQOdHDWUMh" > playlistIDs.txt
