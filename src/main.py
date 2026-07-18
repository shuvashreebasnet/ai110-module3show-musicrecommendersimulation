"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"Loaded songs: {len(songs)}")
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


if __name__ == "__main__":
    main()
