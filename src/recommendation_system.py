# Cafeteria Dish Recommendation System (Discrete Math Implementation)

from collections import Counter

# --- 1. Sets: Users, Dishes -----------------

users = {"u1", "u2", "u3"}  # U
dishes = {"omelet", "pad_kra_pao", "salad", "fried_chicken"}  # D

# --- 2. Functions f, g -----------------------

# f: U -> Taste Preferences
f = {
    "u1": {"spicy", "fried", "rice_based"},
    "u2": {"healthy", "vegan"},
    "u3": {"mild", "fried", "rice_based"},
}

# g: D -> Properties of dishes
g = {
    "omelet": {"mild", "fried", "rice_based"},
    "pad_kra_pao": {"spicy", "fried", "rice_based"},
    "salad": {"healthy", "vegan"},
    "fried_chicken": {"fried"},
}

# --- 3. Order history (Counting) -------------

order_history = [
    ("u1", "pad_kra_pao"), ("u1", "pad_kra_pao"), ("u1", "omelet"),
    ("u2", "salad"), ("u2", "salad"), ("u2", "omelet"),
    ("u3", "omelet"), ("u3", "fried_chicken"), ("u3", "fried_chicken")
]

# Count(u,d)
count_history = Counter(order_history)

# --- 4. Taste score from Sets & Functions ----

def taste_score(u, d):
    """
    S_taste(u, d) = |f(u) ∩ g(d)| / |f(u)|
    """
    user_pref = f.get(u, set())
    dish_tags = g.get(d, set())
    if not user_pref:
        return 0.0
    return len(user_pref & dish_tags) / len(user_pref)

# --- 5. History score from Counting ----------

def history_score(u, d):
    """
    Normalize Count(u, d) by max count for that user
    """
    counts = [c for (user, dish), c in count_history.items() if user == u]
    if not counts:
        return 0.0
    max_count = max(counts)
    return count_history.get((u, d), 0) / max_count

# --- 6. Combined score + Probability ---------

def combined_score(u, d, alpha=0.6, beta=0.4):
    """
    Score(u, d) = alpha * S_taste + beta * W_hist
    """
    return alpha * taste_score(u, d) + beta * history_score(u, d)

def recommendation_distribution(u, alpha=0.6, beta=0.4):
    """
    P(u, d) = Score(u, d) / sum_d'(Score(u, d'))
    """
    scores = {d: combined_score(u, d, alpha, beta) for d in dishes}
    total = sum(scores.values())
    if total == 0:
        return {d: 1/len(dishes) for d in dishes}
    return {d: s / total for d, s in scores.items()}

def recommend_top_k(u, k=3):
    """
    Return Top-k dishes for user u
    """
    probs = recommendation_distribution(u)
    return sorted(probs.items(), key=lambda x: x[1], reverse=True)[:k]

# --- 7. Demo ---------------------------------

if __name__ == "__main__":
    for u in users:
        print(f"\n=== Recommendations for {u} ===")
        for dish, p in recommend_top_k(u):
            print(f"{dish:15s} -> P(u,d) ≈ {p:.3f}")
