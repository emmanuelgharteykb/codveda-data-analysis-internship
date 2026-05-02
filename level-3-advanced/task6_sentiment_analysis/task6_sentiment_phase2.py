import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 1. Load the processed data from Phase 1
df = pd.read_csv('sentiment-dataset-processed.csv')

# 2. Categorize the scores
df['AI_Sentiment'] = df['AI_Score'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

# --- VISUALIZATION 1: Sentiment Distribution ---
plt.figure(figsize=(8, 5))
df['AI_Sentiment'].value_counts().plot(kind='bar', color=['green', 'gray', 'red'])
plt.title('Overall Sentiment Distribution')
plt.show()

# --- VISUALIZATION 2: Word Cloud ---
# Note: we use 'Cleaned_Text' so the cloud stays professional
all_text = " ".join(df['Cleaned_Text'].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Most Common Words in Reviews')
plt.show()