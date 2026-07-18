# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

While experimenting (doubling weight of energy and halving weight of genre), one weakness I discovered was that low-energy/calm users were underrepresented. Becuase the quietest song in the dataset has an energy level of 0.22, a calm/sleep/ambient/study user cannot get a near-perfect match like a high-energy user can. Since energy is the dominant factor with 4 points, the entire recommendation quality for users who do not prioritize energy is not as good of a match compared to those who do.

Another issue is that the exact match check for genre penalizes users whose genre preferences are near the genres of certain songs. For instance, if a user likes pop, the recommender will skip over "Paper Airplanes" in which the genre is dream pop because it is not an exact match. This makes the recommender inflexible. 

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

For Happy Pop vs High-Energy Classical Lover, they both preferred high-energy low acoustic songs, which was expected based on their inputs.

Overall, the recommender prioritizes genre matches, then mood, then energy as expected. While I was concerned that the recommender would fail to suggest songs of similar genres/moods, it seems that it is able to do so based on energy closeness alone.

Also as intended, "Rooftop Lights" keeps showing up for happy, high energy users because it matches the happy mood and is close to the high-energy preference despite different genre preferences. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
