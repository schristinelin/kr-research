import requests
import pandas as pd
import urllib
import json


# function to access wikipathway swagger API
def api_request(target, species):
    species = urllib.parse.quote(species) # encode when needed
    # api link
    r = requests.get(f'https://webservice.wikipathways.org/findPathwaysByText?query={target}&species={species}&format=json')

    # convert into dataframe
    data = json.loads(r.text)
    df = pd.json_normalize(data['result'])

    return df

# implement the above function using example query
df = api_request('nicotine', 'homo sapiens')

# simple example of tokenizing 'name' variable
from nltk.tokenize import word_tokenize


# example of another pathway
df_bc = api_request('breast cancer', 'homo sapiens')

# tokenize df (nicotine dataframe), and df_bc (breast cancer)
df['tokenized_nicotine'] = df['name'].apply(word_tokenize)
df_bc['tokenized_breastcancer'] = df_bc['name'].apply(word_tokenize)

# merge onto one dataframe for view
df_merged = pd.concat([df['tokenized_nicotine'], df_bc['tokenized_breastcancer']], axis = 1)

print(df_merged)