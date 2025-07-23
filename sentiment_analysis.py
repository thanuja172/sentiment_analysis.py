from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


analyzer = SentimentIntensityAnalyzer()


tweets = [
    "I love this product!",
    "This is the worst service ever.",
    "It was okay, nothing special.",
    "Absolutely fantastic experience!",
    "Not happy with the quality.",
    "Very good support team!",
    "Terrible and slow service.",
    "Neutral feeling about this."
]


positive, neutral, negative = 0, 0, 0

for tweet in tweets:
    score = analyzer.polarity_scores(tweet)['compound']
    if score >= 0.05:
        positive += 1
    elif score <= -0.05:
        negative += 1
    else:
        neutral += 1


print(f"Positive: {positive}")
print(f"Neutral : {neutral}")
print(f"Negative: {negative}")


labels = ['Positive', 'Neutral', 'Negative']
counts = [positive, neutral, negative]
colors = ['lightgreen', 'lightblue', 'lightcoral']

plt.figure(figsize=(6, 4))
plt.bar(labels, counts, color=colors)
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Tweet Count')
plt.tight_layout()
plt.show()
