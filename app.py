from flask import Flask, request, jsonify, render_template
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import re

# Download necessary NLTK data files
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')


app = Flask(__name__)

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    feedback = data.get('feedback', '')

    # Split the feedback into individual lines
    # lines = feedback.split('\n')
    lines = re.split('[\n\.]+', feedback)

    # Initialize sentiment counters
    positive_lines = 0
    negative_lines = 0
    neutral_lines = 0

    # Initialize word frequency counters
    positive_word_freq = Counter()
    negative_word_freq = Counter()
    neutral_word_freq = Counter()

    # Perform sentiment analysis for each line
    for line in lines:
        # Perform sentiment analysis
        sentiment_scores = sid.polarity_scores(line)
        sentiment = 'positive' if sentiment_scores['compound'] >= 0.05 else 'negative' if sentiment_scores['compound'] <= -0.05 else 'neutral'

        # Update sentiment counters
        if sentiment == 'positive':
            positive_lines += 1
        elif sentiment == 'negative':
            negative_lines += 1
        elif sentiment == 'neutral' and line != "":
            neutral_lines += 1

        # Tokenize the line and remove stopwords
        tokens = word_tokenize(line.lower())
        stop_words = set(stopwords.words('english')) 
        with open('stopwords.txt', 'r') as f:
            custom_stopwords = [line.strip() for line in f.readlines()]
        stop_words = stop_words.union(custom_stopwords)
        tokens = [word for word in tokens if word.isalpha() and word.lower() not in stop_words]
        
        # Update word frequency counters
        if sentiment == 'positive':
            positive_word_freq.update(tokens)
        elif sentiment == 'negative':
            negative_word_freq.update(tokens)
        else:
            neutral_word_freq.update(tokens)

    # Prepare the response
    response = {
        'cumulative_sentiment': 'positive' if positive_lines > negative_lines else 'negative' if negative_lines > positive_lines else 'neutral',
        'positive_lines': positive_lines,
        'negative_lines': negative_lines,
        'neutral_lines': neutral_lines,
        'positive_word_freq': positive_word_freq.most_common(10),
        'negative_word_freq': negative_word_freq.most_common(10),
        'neutral_word_freq': neutral_word_freq.most_common(10)
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)