import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Book Recommender", layout="wide")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("books.csv")

df = load_data()

# ---------------- FAVORITES FILE ----------------
FAV_FILE = "favorites.csv"

if os.path.exists(FAV_FILE):
    fav_df = pd.read_csv(FAV_FILE)
else:
    fav_df = pd.DataFrame(columns=df.columns)

# ---------------- SESSION STATE ----------------
if "favorites" not in st.session_state:
    st.session_state.favorites = set(fav_df["title"].values)

# ---------------- TITLE ----------------
st.title("📚 Book Recommendation System")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔍 Filters")

genres = sorted(df["genre"].unique())
selected_genre = st.sidebar.selectbox("Choose Genre", ["All"] + genres)

search_query = st.sidebar.text_input("Search Book")
min_rating = st.sidebar.slider("Minimum Rating", 3.5, 5.0, 4.0)

show_favorites = st.sidebar.checkbox("❤️ Show Favorites Only")

# ---------------- FILTER ----------------
filtered_books = df.copy()

if selected_genre != "All":
    filtered_books = filtered_books[filtered_books["genre"] == selected_genre]

if search_query:
    filtered_books = filtered_books[
        filtered_books["title"].str.contains(search_query, case=False)
    ]

filtered_books = filtered_books[filtered_books["rating"] >= min_rating]
filtered_books = filtered_books.sort_values(by="rating", ascending=False)

# Show only favorites
if show_favorites:
    filtered_books = df[df["title"].isin(st.session_state.favorites)]

# ---------------- DISPLAY ----------------
st.subheader("📖 Recommended Books")

if filtered_books.empty:
    st.warning("No books found 😢 Try changing filters.")
else:
    cols = st.columns(4)

    for i, (_, row) in enumerate(filtered_books.iterrows()):
        title = row["title"]

        with cols[i % 4]:
            st.image(row["image"], use_container_width=True)
            st.markdown(f"**{title}**")
            st.write(f"⭐ {row['rating']}")
            st.write(f"✍️ {row['author']}")
            st.caption(row["description"])

            # ---------- LIKE TOGGLE ----------
            is_fav = title in st.session_state.favorites

            if is_fav:
                if st.button(f"💔 Remove", key=f"rem_{i}"):
                    st.session_state.favorites.remove(title)
            else:
                if st.button(f"❤️ Like", key=f"like_{i}"):
                    st.session_state.favorites.add(title)

# ---------------- SAVE FAVORITES ----------------
fav_books = df[df["title"].isin(st.session_state.favorites)]
fav_books.to_csv(FAV_FILE, index=False)