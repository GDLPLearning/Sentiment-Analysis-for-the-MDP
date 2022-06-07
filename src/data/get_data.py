# get_data.py
""" """
import bcrypt  # Good password hashing for your software and your servers
import keys
import pandas as pd
import tweepy as tw


# Creating and Configuring an OAuthHandler to Authenticate with Twitter
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Encrypt the keys
consumer_key = bcrypt.hashpw(consumer_key.encode(), bcrypt.gensalt())
consumer_secret = bcrypt.hashpw(consumer_secret.encode(), bcrypt.gensalt())
access_token = bcrypt.hashpw(access_token.encode(), bcrypt.gensalt())
access_token_secret = bcrypt.hashpw(access_token_secret.encode(), bcrypt.gensalt())

# Creating an API Object and setting the connection with the API
api = tw.API(auth, wait_on_rate_limit=True)


# Define the search term and the date_since date as variables
def making_the_query(search_query, date_since):
    """
    recieve two parameters, the key word that we will use to filter the request and
    the start date (yyyy-mm-dd) to make our query.

    returns a list with all the fetched tweets
    """
    query = search_query + ' medellin -filter:retweets'

    tweets = tw.Cursor(api.search_tweets,
                       q=query,
                       lang="es",
                       since=date_since,
                       tweet_mode="extended").items(2)

    list_of_tweets = [[tweet.full_text,
                       str(tweet.user.screen_name),
                       tweet.user.location,
                       tweet.created_at,
                       tweet.id,
                       tweet.retweet_count,
                       tweet.favorite_count] for tweet in tweets]

    return list_of_tweets


def create_the_df(list_of_tweets):
    """
    Recieve one parameter, the list with all the tweets and return a dataFrame
    """

    # creating the dic to fill with the tweets that we fetch
    diccionario = {
        'full_text': [],
        'user': [],
        'location': [],
        'date': [],
        'tweet_id': [],
        'number_rt': [],
        'number_likes': []
    }

    dict_to_fill = diccionario.copy()

    for row in range(len(list_of_tweets)):
        # agregando los datos al diccionario
        dict_to_fill['full_text'].append(list_of_tweets[row][0])
        dict_to_fill['user'].append(str(list_of_tweets[row][1]))
        dict_to_fill['location'].append(list_of_tweets[row][2])
        dict_to_fill['date'].append(list_of_tweets[row][3])
        dict_to_fill['tweet_id'].append(list_of_tweets[row][4])
        dict_to_fill['number_rt'].append(int(list_of_tweets[row][5]))
        dict_to_fill['number_likes'].append(int(list_of_tweets[row][6]))

    df = pd.DataFrame.from_dict(dict_to_fill)

    return df


def arreglando_texto(texto):
    """recibe el texto del tweet y lo entrega de forma que no afecta la estructura de los csv"""
    words = texto.split()
    tweet = ''
    for w in words:
        try:
            w_ini = w[:4]
        except:
            w_ini = w
    # filtrando para eliminar los enlaces del tweet
        if w_ini != 'http': tweet+= f' {w}'

    return tweet


replace_key_words = {
    'movilidad sostenible':'1',
    'movilidad inteligente':'2',
    'servicios publicos':'3',
    'energias alternativas':'4',
    'reciclaje':'5',
    'energias renovables':'6',
    'urbanimo ecologico':'7',
    'urbanismo':'8',
    'desarrollo rural':'9',
    'bienestar animal':'10',
    'biodiversidad':'11',
    'energias limpias':'12',
    'movilidad':'13',
    'reciclar':'14',
    'energias':'15',
    'rural':'16'
}

# palabras claves seleccionadas para realizar la busqueda
key_words = [
                   '"movilidad sostenible"', '"movilidad inteligente"', '"servicios publicos"',
                   '"energias alternativas"', '"reciclaje"', '"energias renovables"',
                   '"urbanimo ecologico"', '"urbanismo"', '"desarrollo rural"',
                   '"bienestar animal"', '"biodiversidad"', '"energias limpias"',
                   '"movilidad"','"reciclar"', '"energias"', '"rural"',
]

# creando una consulta para cada palabra clave
date_since = "2022-05-21" # date filter to search the tweets
count = 0
for search_query in key_words:

  list_of_tweets = making_the_query(search_query, date_since)
  df = create_the_df(list_of_tweets)
  # creando una nueva columna con la palabra clave
  df['id_key_word'] = search_query.replace('"','')

  if count == 0:
    df_final = df
    count = 1
  else:
    df_final = df_final.append(df, ignore_index=True)

# limpiando la columna con el texto del tweet
df_final['full_text'] = df_final['full_text'].apply(arreglando_texto)
df_final['id_key_word'] = df_final['id_key_word'].replace(replace_key_words)

# using dictionary to convert specific columns
convert_dict = {
  'user':str,
  'number_likes': int,
  'number_rt': int
  }

# convert columns type to match the dataset structure
df_final = df_final.astype(convert_dict)

day = date_since[8:10]
month = date_since[5:7]
year = date_since[:4]
df_final.to_csv(f'/content/tweets_{day}{month}{year}.csv',index = False)