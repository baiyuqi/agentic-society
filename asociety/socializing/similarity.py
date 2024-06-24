import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

# Define a User class with additional attributes
class User:
    def __init__(self, name, age, sex, education, traits):
        self.name = name
        self.age = age
        self.sex = sex
        self.education = education
        self.traits = np.array(traits)

# Function to calculate similarity between users
def calculate_similarity(user1, user2, weights):
    # Normalize age difference
    age_diff = np.abs(user1.age - user2.age)
    age_similarity = np.exp(-age_diff / weights['age'])
    
    # Sex similarity (1 if same, 0 if different)
    sex_similarity = 1 if user1.sex == user2.sex else 0
    
    # Education level similarity (1 if same, 0 if different)
    education_similarity = 1 if user1.education == user2.education else 0
    
    # Cosine similarity for personality traits
    trait_similarity = cosine_similarity([user1.traits], [user2.traits])[0][0]
    
    # Weighted sum of similarities
    total_similarity = (weights['age'] * age_similarity + 
                        weights['sex'] * sex_similarity + 
                        weights['education'] * education_similarity + 
                        weights['traits'] * trait_similarity)
    return total_similarity

# Function to recommend friends for a given user
def recommend_friends(target_user, all_users, weights, top_n=3):
    similarities = []
    for user in all_users:
        if user.name != target_user.name:
            similarity = calculate_similarity(target_user, user, weights)
            similarities.append((user.name, similarity))
    
    # Sort users by similarity in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Return top N recommendations
    return similarities[:top_n]

# Example usage
if __name__ == "__main__":
    users = [
        User("Alice", 25, "F", "Bachelor", [0.8, 0.7, 0.6, 0.9, 0.75]),
        User("Bob", 24, "M", "Master", [0.65, 0.8, 0.7, 0.6, 0.85]),
        User("Charlie", 25, "M", "Bachelor", [0.6, 0.6, 0.8, 0.75, 0.7]),
        User("David", 26, "M", "PhD", [0.9, 0.5, 0.6, 0.8, 0.6]),
        User("Eve", 25, "F", "Bachelor", [0.7, 0.7, 0.7, 0.7, 0.7])
    ]
    
    weights = {
        'age': 0.2,
        'sex': 0.2,
        'education': 0.2,
        'traits': 0.4
    }
    
    target_user = users[0]  # Let's say we want to find friends for Alice
    recommendations = recommend_friends(target_user, users, weights)
    
    print(f"Friend recommendations for {target_user.name}:")
    for name, similarity in recommendations:
        print(f"{name} with similarity score: {similarity:.2f}")
