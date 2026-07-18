"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# Edge-case profiles used to stress-test the recommender.
PROFILES = [
    # Happy Pop
    {"genre": "pop", "mood": "happy", "energy": 0.8},
    # The Metal Romantic - Edge case 1. Impossible combo: no song is both metal and romantic.
    {"genre": "metal", "mood": "romantic", "energy": 0.5},
    # High-Energy Classical Lover - Edge case 2. Genre exists, but never with that mood (classical is only melancholy).
    {"genre": "classical", "mood": "happy", "energy": 0.9},
    # The Chill Guy - Edge case 3. Extreme energy boundary (energy = 0.0).
    {"genre": "ambient", "mood": "chill", "energy": 0.0},
]


def run_profile(user_prefs: dict, songs: list) -> None:
    """Run the recommender for one profile and print its top recommendations."""
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(
        f"Your taste: genre = {user_prefs['genre']} / mood = {user_prefs['mood']} "
        f"/ energy = {user_prefs['energy']}"
    )

    print("\n" + "=" * 48)
    print("TOP RECOMMENDATIONS")
    print("=" * 48)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n{rank}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f} / 7.00")
        print("   Why:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")

    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile in PROFILES:
        print("\n" + "#" * 48)
        run_profile(profile, songs)


if __name__ == "__main__":
    main()
