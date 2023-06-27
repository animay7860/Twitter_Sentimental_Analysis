import streamlit as st
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
import tweepy

# Set up Twitter API credentials
consumer_key = "OCgWzDW6PaBvBeVimmGBqdAg1"
consumer_secret = "tBKnmyg5Jfsewkpmw74gxHZbbZkGIH6Ee4rsM0lD1vFL7SrEIM"
access_token = "1449663645412065281-LNjZoEO9lxdtxPcmLtM35BRdIKYHpk"
access_token_secret = "FL3SGsUWSzPVFnG7bNMnyh4vYK8W1SlABBNtdF7Xcbh7a"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Function for text preprocessing
def preprocess_text(text):
    text = re.sub(r"@\w+\s?", "", text)

    # remove non-alphabetic characters and convert to lowercase
    text = re.sub(r"[^a-zA-Z\s]", "", text).lower()

    # remove unnecessary whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


# Function to fetch recent tweets
def fetch_recent_tweets(username, count):
    try:
        tweets = tweepy.Cursor(
            api.user_timeline,
            screen_name=username,
            count=count,
            since_id=None,
            max_id=None,
            trim_user=True,
            exclude_replies=True,
            contribubtor_details=False,
            include_entities=False,
        ).items(count)
        return [tweet.text for tweet in tweets]
    except tweepy.TweepError as e:
        st.error(f"Error: {e}")
        return []


# Function to perform sentiment analysis
def analyze_sentiment(tweet):
    preprocessed_tweet = preprocess_text(tweet)
    blob = TextBlob(preprocessed_tweet)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"


# Streamlit app
def main():
    st.title("Twitter Sentiment Analysis")

    # Input for user to enter a Twitter username
    twitter_username = st.text_input("Enter a Twitter username")
    tweet_count = st.number_input(
        "Enter the count of recent tweets", min_value=1, value=50, step=1
    )
    # Retrieve and display recent tweets
    if st.button("Get Recent Tweets"):
        st.write("Fetching recent tweets...")
        recent_tweets = fetch_recent_tweets(twitter_username, count=50)
        df = pd.DataFrame(recent_tweets, columns=["Tweet"])
        df["Sentiment"] = df["Tweet"].apply(analyze_sentiment)
        st.write("Sentiment Analysis of Recent Tweets:")
        st.dataframe(df)


if __name__ == "__main__":
    main()
