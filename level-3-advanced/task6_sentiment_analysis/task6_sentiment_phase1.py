import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import re

# Downloading necessary NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# 1. Loading my dataset
df = pd.read_csv('sentiment-dataset.csv')

# 2. Setup cleaning tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Removing special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', str(text).lower())
    # Tokenize and remove stopwords
    tokens = text.split()
    cleaned_tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(cleaned_tokens)

# 3. Apply cleaning to the "Text" column
df['Cleaned_Text'] = df['Text'].apply(clean_text)
df['AI_Score'] = df['Cleaned_Text'].apply(lambda x: TextBlob(x).sentiment.polarity)

# 4. Get Sentiment Score
df['AI_Score'] = df['Cleaned_Text'].apply(lambda x: TextBlob(x).sentiment.polarity)

print("--- Data Cleaned and Scored ---")
print(df[['Text', 'AI_Score']].head())

# Saving to a temporary file for Phase 2
df.to_csv('sentiment-dataset-processed.csv', index=False)
print("--- Phase 1 Complete: Data saved to sentiment-dataset-processed.csv ---")