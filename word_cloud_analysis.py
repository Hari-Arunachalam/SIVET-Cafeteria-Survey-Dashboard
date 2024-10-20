# word cloud analysis 


import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Load the dataset
df = pd.read_excel("/Users/hariarunachalam/Documents/Code/Data Cleaning/Canteentest_cleaned.xlsx")

# Extract the relevant feedback column
canteen_changes_feedback = df['What changes do you want to upgrade our canteen to everyones satiisfaction , suggest practically possible and genuine suggestions ?']

# Clean the data: remove NaN values, convert to string, strip spaces, and lowercase
canteen_changes_cleaned = canteen_changes_feedback.dropna().astype(str).str.strip().str.lower()

# Combine the cleaned feedback into a single string
feedback_text = " ".join(canteen_changes_cleaned)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Blues').generate(feedback_text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.title('Canteen Upgrade Suggestions Word Cloud', fontsize=16)
plt.show()