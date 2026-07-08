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

Real-world streaming platforms like Spotify and Youtube use both collaborative and content-based filtering to recommend content to users. 

Collaborative filtering is done by assessing engagement patterns. For Spotify, this would be patterns in what users are listening to. For YouTube, this would be patterns found in watch history.

Content-based filtering organizes features of the platform's content to find what features are similar to the content users are engaging with. For Spotify, that would mean checking for similarity in song attributes like genre, mood, and energy. For YouTube, that would be video topics or visual/audio features.

This system will prioritize user preferences in genres, moods, and energy. 

- Each `Song` in the system has a title, artist, genre, mood, and energy, tempo in beats per minute, valence, danceability, and acousticness.

- `UserProfile` will store genre, mood, and energy preferences. Optionally, it will also store favorite artists.

- The `Recommender` will compute a score of each song by calculating the linear falloff (1 - |x - p|) for each numerical, normalized feature on a 0 to 1 scale. The closer the feature is to 1, the better aligned the song is with the user preferences. 

- The system will choose which songs to recommend mainly by genre, then mood, and energy. If the user inputs a specific artist they like, It will also recommend songs from that artist, even more so if the songs are aligned with the main recommending features.


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



