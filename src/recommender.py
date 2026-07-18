import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file, returning a list of dicts with numeric fields typed."""
    print(f"Loading songs from {csv_path}...")

    int_fields = {"id"}
    float_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
    }

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song: Dict = {}
            for key, value in row.items():
                if key in int_fields:
                    song[key] = int(value)
                elif key in float_fields:
                    song[key] = float(value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user prefs, returning (score, list of reasons)."""
    score = 0.0
    reasons: List[str] = []

    # Genre: exact match earns 3 points
    if song["genre"] == user_prefs["genre"]:
        score += 3
        reasons.append(f"Genre matches ({song['genre']})")

    # Mood: exact match earns 2 points
    if song["mood"] == user_prefs["mood"]:
        score += 2
        reasons.append(f"Mood matches ({song['mood']})")

    # Energy: reward closeness, up to 2 points
    closeness = 1 - abs(song["energy"] - user_prefs["energy"])
    energy_points = closeness * 2
    score += energy_points
    reasons.append(
        f"Energy is {closeness:.2f} close to your target ({energy_points:.2f} pts)"
    )

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs as (song, score, explanation) tuples, ranked high to low."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in ranked[:k]
    ]
