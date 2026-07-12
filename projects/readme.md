# 🎬 Content-Based Movie Recommender System

A content-based movie recommendation system built using the TMDB 5000 Movie Dataset. Given a movie title, the system recommends the top 5 most similar movies based on genre, plot overview, keywords, cast, and director.

🔗 **Kaggle Notebook:** [content-wise-movie-reccomendations](https://www.kaggle.com/code/superviseddeep/content-wise-movie-reccomendations)

---

## 📌 Overview

This project uses **Content-Based Filtering** — recommendations are generated purely from movie metadata (no user ratings or behavior data involved). It falls under **Unsupervised Learning**, since there are no labels to predict; instead, similarity between movies is calculated mathematically.

---

## 🗂️ Dataset

- **tmdb_5000_movies.csv**
- **tmdb_5000_credits.csv**

Merged on the `id` column to combine movie metadata with cast and crew information.

---

## 🛠️ What Was Done

### 1. Data Cleaning & Feature Selection
- Selected relevant columns: `id`, `title`, `genres`, `overview`, `keywords`, `cast`, `crew`
- Parsed stringified JSON columns (`genres`, `keywords`, `cast`, `crew`) using `ast.literal_eval`
- Extracted only the **top 3 cast members** and the **director** from crew
- Dropped rows with missing values (minor — only a few rows affected)

### 2. Text Preprocessing
- Removed spaces within multi-word names (e.g. `"Sam Worthington"` → `"SamWorthington"`) to prevent incorrect token overlap during vectorization
- Cleaned punctuation from the `overview` column before splitting into words
- Combined `genres`, `keywords`, `overview`, `cast`, and `crew` into a single `tags` column per movie
- Applied **stemming** (via NLTK's `PorterStemmer`) to reduce words to their root form

### 3. Vectorization
- Converted the `tags` column into numerical vectors using **TF-IDF** (`TfidfVectorizer`, `stop_words='english'`, `max_features=5000`)

### 4. Similarity Calculation
- Computed a **cosine similarity matrix** across all movies using `sklearn.metrics.pairwise.cosine_similarity`

### 5. Recommendation Function
- Built a `recommend(movie)` function that:
  1. Locates the given movie's index
  2. Retrieves its similarity scores against all other movies
  3. Sorts and returns the top 5 most similar titles (excluding the movie itself)

### 6. Testing / Validation
- Since this is unsupervised (no ground-truth labels), results were validated manually by checking whether recommendations made sense (e.g. *The Dark Knight Rises* → other Batman movies, *Toy Story* → Toy Story 2 & 3)

---

## ⚙️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn (`TfidfVectorizer`, `cosine_similarity`)
- NLTK (`PorterStemmer`)

---

## 🚧 Next Steps (In Progress)

- [ ] Fetch movie posters using the TMDB API
- [ ] Save processed data using `pickle` for reuse
- [ ] Build an interactive **Streamlit** web app
- [ ] Deploy on **Streamlit Community Cloud** for a live, shareable link

---

## 📁 Files

- `content-wise-movie-recommendations.ipynb` — Full notebook with data cleaning, TF-IDF, and recommendation logic
