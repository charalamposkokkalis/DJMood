# DJ Mood

#### Charalampos Kokkalis, Giannis Tyrovolas, Ioannis Stamoulis
 
### Overview
Our hack is an ambitious way of connecting moods with songs. As people who enjoy music we found it very common that algorithms entrench our pre-existing preferences when it comes to music. We wanted to create a new way to explore new music. That's why we created DJ Mood. We use natural language processing to identify the user's emotions and create a personalized playlist for each user.

Creating this hack was great fun and we learned a lot of new things in the process.

### Methodology
The high-level plan was the following:

- Analyze features of a large dataset of songs
- Create a website and a simple interface for the user
- Use input data to create a mood vector
- Associate our mood vector with each song by training appropriate weights
- Create a link with the user's new playlist

We chose as our dataset Spotify's top 100 playlists. We did this because it includes a diverse set of musical genres and moods. With playlists from RapCaviar to Mellow Piano we believe a huge range was covered.

We used Python's Spotipy API to gather this data.

### Build with
- azure
- gcp
- python
- SpotifyAPI
