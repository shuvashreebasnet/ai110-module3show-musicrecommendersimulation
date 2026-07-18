# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```
```python
Loaded songs: 19
Your taste: pop / happy / energy 0.8

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

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



