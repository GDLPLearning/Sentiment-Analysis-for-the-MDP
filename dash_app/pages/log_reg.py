# import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import tools
# load data

def log_reg(text):
    df_rating=pd.read_csv('dash_app/pages/data/sentiment_1_0.csv')
    # clean the tweet and save it on a new column

    def clean_tweet(tweet):
        new_tweet=' '
        words = tweet.split()
        for w in words:
            wl = w.lower() # word in lower case
    
            # replace numbers
            for number, new_value in tools.replace_numbers_dict.items():
                wl = str(wl).replace(number,new_value)

            # replace some punctuations mark to keep only words
            for punctuation, new_value in tools.replace_punctuation_dict.items():
                wl = wl.replace(punctuation,new_value)
    
            # replace accent mark 
            for accent, new_value in tools.replace_accent_dict.items():
                wl = wl.replace(accent,new_value)

            if wl not in tools.model_stop_wprds:
                new_tweet += f'{wl} '
        return new_tweet[:-1]
    # clean data
    df_rating['clean_tweet'] = df_rating['full_text'].apply(clean_tweet)
    # split data into train and test
    tweets_train, tweets_test = train_test_split(df_rating, test_size=0.2, random_state=0)    # vectorize data
    vectorizer = CountVectorizer()
    x_train_bow = vectorizer.fit_transform(tweets_train['clean_tweet'])
    y_train_bow = tweets_train['sentiment']
    # train model
    lr_model_all = LogisticRegression()
    lr_model_all.fit(x_train_bow, y_train_bow)
    # predict
    text=clean_tweet(text)
    return lr_model_all.predict(vectorizer.transform([text]))[0]

#text=input('Enter a tweet: ')
#log_reg(text)
#print(f'The sentiment of the tweet is: {log_reg(text)}')
