# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

SongSenser

---

## 2. Intended Use  

Generates song recommendations based on genre, mood, and energy preferences, assuming the user has preferences for each category. This is can be for real users.

---

## 3. How the Model Works  

The recommender consideres the user's preferences in genre, mood, and energy. It is then compared with each song's genre, mood, and energy to calculate a score. The model checks for an exact genre (3pts) and mood match (2pts). For energy, it calculates the song's closeness to user's energy preference and adds the appropriate number of points to the score (up to 2pts). The recommender then sort the songs from highest score to lowest.

The starter logic was initially going to consider all song features such as acousticness and tempo_bpm. I decided to narrow down the features to these 3 for simplicity, and because these preferences are the most popular when deciding on songs.

---

## 4. Data  
 
There are 19 songs in the catalog.

Genres: includes pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, classical, edm, reggae, metal, folk, r&b, dream pop. funk

Moods: includes chill, intense, relaxed, moody, focused, happy, energetic, melancholy, euphoric, uplifting, aggressive, nostalgic, romantic, dreamy, playful

I did not remove any data in songs.csv. However, the recommender only uses 3 of the song features. Some features missing in the dataset are dates the song was released, song length, and other credits for composer, lyricist, etc.

---

## 5. Strengths  

Where does your system seem to work well  
The recommender works well for users who are looking for high-energy, pop songs. The scoring captures genre and mood matches correctly. For instance, a user who prefers pop genre, happy mood, and high energy (e.g. Happy Pop profile) will get songs that have a high match in genre, mood, then energy such as Sunrise City, Gym Hero, and Rooftop Lights.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

While experimenting (doubling weight of energy and halving weight of genre), one weakness I discovered was that low-energy/calm users were underrepresented. Becuase the quietest song in the dataset has an energy level of 0.22, a calm/sleep/ambient/study user cannot get a near-perfect match like a high-energy user can. Since energy is the dominant factor with 4 points, the entire recommendation quality for users who do not prioritize energy is not as good of a match compared to those who do.

Another issue is that the exact match check for genre penalizes users whose genre preferences are near the genres of certain songs. For instance, if a user likes pop, the recommender will skip over "Paper Airplanes" in which the genre is dream pop because it is not an exact match. This makes the recommender inflexible. 

Another limitation is the small dataset. There are not enough songs to recommend for certain genres/moods that are underrepresented in the dataset.

---

## 7. Evaluation  

How I checked whether the recommender behaved as expected (after changing the weights back to genre: 3pts, mood: 2pts, energy: <=2 pts).

- I tested the following user profiles:
The Metal Romantic vs the Chill Guy, and the Happy Pop vs High-Energy Classical Lover
- What I looked for in the recommendations:  
For the Metal Romantic, I looked for metal genres and romantic moods. I was expecting moderate energy levels in some songs.
For the Chill Guy, I looked for ambient genre matches and chill mood matches. 
-  I was surprised to see "Paper Airplanes" ranked 3rd (higher than expected)because it is a dream pop song. While the recommender does not consider how dreamy and romantic can be similar moods, it manages to recommend the song because of energy closeness.
-  Similarly when looking at recommendations for the Chill Guy, I was surprised to see "Winter Nocturne" (classical, melancholy) and "Coffee Shop Stories" (jazz, relaxed) because although relaxed is not the user's mood preference, it is still similar to chill.
- For Happy Pop vs High-Energy Classical Lover, they both preferred high-energy low acoustic songs, which was expected based on their inputs.

While high-energy profiles (Happy Pop and High-Energy Classical Lover) prefer less acoustic songs and more energy, calmer, low-energy profiles prefer more acoustic songs and less energy. 

Overall, the recommender prioritizes genre matches, then mood, then energy as expected. While I was concerned that the recommender would fail to suggest songs of similar genres/moods, it seems that it is able to do so based on energy closeness alone.

Also as intended, "Rooftop Lights" keeps showing up for happy, high energy users because it matches the happy mood and is close to the high-energy preference despite different genre preferences. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  
- multiple genres and moods: users can select multiple genres they like instead of just one
- ranking options: ranking recommended songs based on genre, mood, and energy closeness, changing the weight for each feature as needed
- adding artist and acousticness as an attribute: many users like to listen to songs by certain artists or acoustic songs, adding that as an option offers more diversity in recommendations
- diversify and add more songs in the data set
- consider similar genres and moods: ex. if pop is the user preference and the song's genre is dreamy pop, add 2 instead of 3 points so there is still some consideration for similarity

---

## 9. Personal Reflection  

I learned recommenders turn data into predictions by content features such as song attributes. Recommenders also collaborative filtering through listening pattens. Adding weights to different attributes(e.g. genre with the highest weight) influence how songs are recommended (e.g. songs that match genre are recommended first).

I noticed there may be bias in how the recommender will ignore similar genres like pop and dreamy pop due to checking for an exact match. However, when I tested with various profiles, songs of similar genres were still recommended because of the closeness in energy levels.

This changed the way I think about music recommendation apps in how even if there isn't a conditional to check for similarity in certain song attributes, it can be correlated with an attribute that is checked, leading to accurate recommendations regardless. 