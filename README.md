# 🎵 Music Recommender Simulation

## Project Summary

This music recommender system considers user preferences in music genre, mood, and energy levels to recommend the top 5 songs in the dataset that align the most with these preferences.

---

## How The System Works

1. Research: Real-World Streaming Platforms
Real-world streaming platforms like Spotify and Youtube use both collaborative and content-based filtering to recommend content to users. 

Collaborative filtering is done by assessing engagement patterns. For Spotify, this would be patterns in what users are listening to. For YouTube, this would be patterns found in watch history.

Content-based filtering organizes features of the platform's content to find what features are similar to the content users are engaging with. For Spotify, that would mean checking for similarity in song attributes like genre, mood, and energy. For YouTube, that would be video topics or visual/audio features.

2. This System

This system will prioritize user preferences in genres, moods, and energy. 

- Each `Song` in the system has a title, artist, genre, mood, and energy, tempo in beats per minute, valence, danceability, and acousticness.

- `UserProfile` will store genre, mood, and energy. 

- The `Recommender` will compute the sum of points earned based on each matching or closely-aligned attribute in user preferences. If genre is an exact match, 3 points will be added. If mood is an exact match, 2 points will be added. The numeric value in the energy attriute will be rewarded more the smaller the difference is between song and user-selected energy. Closeness in energy (calculated by 1 - |difference|) can earn up to 2 points (closeness*2). Therefore, the total possible points in a song score is 7.

- The system will choose which songs to recommend based on user preferences in genre, mood, and energy. Since genre is more specific, it has the highest weight of 3 points. Mood is secondary with a weight of 2 points. Energy is rewarded up to 2 points based on closeness to user-selected energy preference.

- Note for Bias: The system may prioritize songs that match genre input and do not match mood and energy, much more than songs that match mood and energy preferences but not the genre input. As a result, the system may ignore songs that match the less-weighted user preferences, even if the user prioritizes those preferences more than genre. In addition, the system checks for an exact match in genre, so it may ignore songs of similar genres like "Rock" and "Alternative Rock".

*Available but unused attributes to add in Model Card: tempo_bpm, valence, danceability.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output
Profile: Happy Pop
```python
Loaded songs: 19
Your taste: genre = pop / mood = happy / energy = 0.8

================================================
TOP RECOMMENDATIONS
================================================

1. Sunrise City - Neon Echo
   Score: 6.96 / 7.00
   Why:
     - Genre matches (pop)
     - Mood matches (happy)
     - Energy is 0.98 close to your target (1.96 pts)

2. Gym Hero - Max Pulse
   Score: 4.74 / 7.00
   Why:
     - Genre matches (pop)
     - Energy is 0.87 close to your target (1.74 pts)

3. Rooftop Lights - Indigo Parade
   Score: 3.92 / 7.00
   Why:
     - Mood matches (happy)
     - Energy is 0.96 close to your target (1.92 pts)

4. Concrete Rhythm - Blockprint
   Score: 2.00 / 7.00
   Why:
     - Energy is 1.00 close to your target (2.00 pts)

5. Night Drive Loop - Neon Echo
   Score: 1.90 / 7.00
   Why:
     - Energy is 0.95 close to your target (1.90 pts)
```
The Happy Pop profile prefers high-energy, low acoustic songs.

Checking Edge Cases:
- #1: Profile: The Metal Romantic, no song matches both
```python
################################################
Your taste: genre = metal / mood = romantic / energy = 0.5

================================================
TOP RECOMMENDATIONS
================================================

1. Iron Verdict - Ashfall
   Score: 4.04 / 7.00
   Why:
     - Genre matches (metal)
     - Energy is 0.52 close to your target (1.04 pts)

2. Velvet Hours - Mara Skye
   Score: 3.96 / 7.00
   Why:
     - Mood matches (romantic)
     - Energy is 0.98 close to your target (1.96 pts)

3. Paper Airplanes - Cloudline
   Score: 1.96 / 7.00
   Why:
     - Energy is 0.98 close to your target (1.96 pts)

4. Island Time - Sun Cadence
   Score: 1.84 / 7.00
   Why:
     - Energy is 0.92 close to your target (1.84 pts)

5. Midnight Coding - LoRoom
   Score: 1.84 / 7.00
   Why:
     - Energy is 0.92 close to your target (1.84 pts)
```
"Iron Verdict" wins based on the genre alone, barely above "Velvet Hours" which matches the mood preference. Overall, the recommedner degrades to genre and energy as intended. For this profile, there is no consistent pattern. There are some moderate-energy and acoustic songs, and some high-energy low acoustic songs.

#2: Profile: High-Energy Classical Lover, genre exists, but none with the mood 
```python
################################################
Your taste: genre = classical / mood = happy / energy = 0.9

================================================
TOP RECOMMENDATIONS
================================================

1. Sunrise City - Neon Echo
   Score: 3.84 / 7.00
   Why:
     - Mood matches (happy)
     - Energy is 0.92 close to your target (1.84 pts)

2. Rooftop Lights - Indigo Parade
   Score: 3.72 / 7.00
   Why:
     - Mood matches (happy)
     - Energy is 0.86 close to your target (1.72 pts)

3. Winter Nocturne - Elise Moreau
   Score: 3.64 / 7.00
   Why:
     - Genre matches (classical)
     - Energy is 0.32 close to your target (0.64 pts)

4. Storm Runner - Voltline
   Score: 1.98 / 7.00
   Why:
     - Energy is 0.99 close to your target (1.98 pts)

5. Gym Hero - Max Pulse
   Score: 1.94 / 7.00
   Why:
     - Energy is 0.97 close to your target (1.94 pts)
```
The only classical song "Winter Nocturne" ranks 3rd, below the two happy pop songs. In this case, the recommender ranked the songs matching mood and energy higher than the genre match. This profile generally prefers high energy, low-acoustic songs.

#3: Profile: The Chill Guy, extreme energy boundaries
```python
################################################
Your taste: genre = ambient / mood = chill / energy = 0.0

================================================
TOP RECOMMENDATIONS
================================================

1. Spacewalk Thoughts - Orbit Bloom
   Score: 6.44 / 7.00
   Why:
     - Genre matches (ambient)
     - Mood matches (chill)
     - Energy is 0.72 close to your target (1.44 pts)

2. Library Rain - Paper Lanterns
   Score: 3.30 / 7.00
   Why:
     - Mood matches (chill)
     - Energy is 0.65 close to your target (1.30 pts)

3. Midnight Coding - LoRoom
   Score: 3.16 / 7.00
   Why:
     - Mood matches (chill)
     - Energy is 0.58 close to your target (1.16 pts)

4. Winter Nocturne - Elise Moreau
   Score: 1.56 / 7.00
   Why:
     - Energy is 0.78 close to your target (1.56 pts)

5. Coffee Shop Stories - Slow Stereo
   Score: 1.26 / 7.00
   Why:
     - Energy is 0.63 close to your target (1.26 pts)
```
"SpaceWalk Thoughts" ranks highest because of the genre and mood match, showing energy is valued less as intended. This ambient, chill profile prefers low energy guitars.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

- When I halved the weight on genre and doubled the weight on energy for the first sample (genre = pop / mood = happy / energy = 0.8), "Rooftop Lights" jumped to #2 because it matched in energy and mood, while "Gym Hero" dropped to #3 despite matching genre. As a result, it changed the recommendations slightly. Whether it made the recommendations more accurate depends on the user's priorities in genre and energy.

---

## Limitations and Risks
- might favor high-energy genres and moods (e.g. pop, happy)
- small dataset (19 songs)
- values genre matches the most
---

## Reflection

I learned real-world recommender systems use collaborative-based filtering (e.g. patterns in listening history) and content-based filtering (e.g. song attributes user engages with).

I also learned bias can show up in small datasets that lack diversity and enough data for adaptive decisions. To resolve this, adding more songs with different attribute values in genre, mood and others will give more representation. As a result, recommending will be more aligned with user preferences. 

AI helped my process by identifying edge cases and potential biases in my recommendation algorithm. It also helped in adding more songs to the dataset and figuring out algorithm options for recommending songs. I needed to double check its suggestions when it came to implementation. 

more on:
[**Model Card**](model_card.md)



