import pandas as pd
import random

# Better book titles
titles = [
    "The Silent Forest", "Dreams of Tomorrow", "Hidden Truths", "Beyond the Stars",
    "Love & Loss", "The Last Kingdom", "Mindset Mastery", "Rich Life Secrets",
    "Dark Horizon", "The Unknown Path"
]

# Authors
authors = [
    "Ravi Kumar", "Ananya Sharma", "John Smith", "Emily Clark", "Arjun Mehta"
]

# Genres
genres = [
    "Fantasy", "Sci-Fi", "Romance", "Self-Help", "Finance", "Fiction"
]

# Descriptions
descriptions = [
    "A thrilling and engaging story",
    "A must-read for everyone",
    "Inspiring and thought-provoking",
    "A journey full of twists",
    "Life-changing insights"
]

# Different images (you can add more)
images = [
    "https://covers.openlibrary.org/b/id/8231996-L.jpg",
    "https://covers.openlibrary.org/b/id/8226191-L.jpg",
    "https://covers.openlibrary.org/b/id/8231856-L.jpg",
    "https://covers.openlibrary.org/b/id/8235116-L.jpg"
]

data = []

# Generate 100 books
for i in range(100):
    data.append({
        "title": random.choice(titles) + " " + str(i),  # makes titles unique
        "author": random.choice(authors),
        "genre": random.choice(genres),
        "rating": round(random.uniform(3.5, 5.0), 1),
        "image": random.choice(images),
        "description": random.choice(descriptions)
    })

df = pd.DataFrame(data)

# Save CSV
df.to_csv("books.csv", index=False)

print("✅ Dataset generated successfully!")