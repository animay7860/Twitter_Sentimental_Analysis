# Twitter Sentiment Analysis

##### HuggingFace Space: https://huggingface.co/spaces/animay620/Twitter_Sentimental_Analysis

This project is a simple web application built with Streamlit that performs sentiment analysis on recent tweets using TextBlob. It allows users to enter a Twitter username, specify the count of recent tweets to analyze, and display the sentiment analysis results in a data frame, along with bar plots for negative and positive sentiments and a count plot for negative, positive, and neutral sentences.
## ScreenShots
![image](https://github.com/animay7860/Twitter_Sentimental_Analysis/assets/99870091/eb6233da-e3fa-4ad4-a3d0-cdd2c46b4b39)

## Features

- Enter a Twitter username and specify the count of recent tweets to analyze.
- Perform sentiment analysis on the recent tweets using TextBlob.
- Display the sentiment analysis results in a DataFrame.
- Visualize the sentiment distribution with bar plots for negative and positive sentiments, and a count plot for negative, positive, and neutral sentences.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/animay7860/Twitter_Sentimental_Analysis.git
   ```
2. Change to the project directory:
    ```bash
    cd Twitter_Sentimental_Analysis
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### Usage
 1. Make sure you have your Twitter API credentials ready. If you don't have them, you can create a Twitter Developer account and obtain the required credentials.
 2. Open the app.py file and replace the placeholder values for the Twitter API credentials (YOUR_CONSUMER_KEY, YOUR_CONSUMER_SECRET, YOUR_ACCESS_TOKEN, and 
   YOUR_ACCESS_TOKEN_SECRET) with your actual Twitter API credentials.
 3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
 4. Open your browser and go to http://localhost:8501 to access the app.
 5. Enter a Twitter username and specify the count of recent tweets to analyze.
 6. Click the "Get Recent Tweets" button to fetch the recent tweets and perform sentiment analysis.
 7. View the sentiment analysis results in the DataFrame and the visualizations.

## Contributing
Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or submit a pull request.







   
