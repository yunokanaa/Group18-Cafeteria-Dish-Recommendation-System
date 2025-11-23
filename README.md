# Group18-Cafeteria-Dish-Recommendation-System

# Group18 - Cafeteria Dish Recommendation System 🍽️

A simple cafeteria dish recommendation system for CPE111 (Discrete Mathematics).  
This project applies:

- Sets and Functions
- Relations
- Counting and Discrete Probability

## 🔍 Idea

For each user, the system recommends dishes based on:

1. **Taste Preference Matching**  
   Using the intersection between user preference set \( f(u) \) and dish attribute set \( g(d) \).

2. **Order History (Counting & Probability)**  
   Using the frequency of past orders \( \text{Count}(u, d) \) to adjust the probability.

## 📐 Math Formulas

- Taste score:  
  \( S_{\text{taste}}(u,d) = \dfrac{|f(u) \cap g(d)|}{|f(u)|} \)

- Final probability:  
  \( P(u,d) = \dfrac{\text{Score}(u,d)}{\sum_{d'} \text{Score}(u,d')} \)

where  
\( \text{Score}(u,d) = \alpha \cdot S_{\text{taste}}(u,d) + \beta \cdot W_{\text{hist}}(u,d) \).

## 💻 How to Run (Example)

```bash
python src/recommendation_system.py
