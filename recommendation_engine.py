from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Load synthetic data
data = pd.read_csv("synthetic_grocery_data.csv")

# Create a customer-product matrix
customer_product_matrix = data.pivot_table(index='CustomerID', columns='Product', aggfunc='size', fill_value=0)

# Compute similarity between products
product_similarity = cosine_similarity(customer_product_matrix.T)
product_similarity_df = pd.DataFrame(product_similarity, index=customer_product_matrix.columns, columns=customer_product_matrix.columns)

# Recommend products
def recommend_products(product_name, similarity_matrix, top_n=5):
    if product_name not in similarity_matrix.columns:
        return f"Product '{product_name}' not found."
    similar_products = similarity_matrix[product_name].sort_values(ascending=False)[1:top_n + 1]
    return similar_products

# Example usage
product_to_recommend = "Product_1"
recommendations = recommend_products(product_to_recommend, product_similarity_df)
print(f"Top recommendations for '{product_to_recommend}':")
print(recommendations)
