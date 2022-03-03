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

# implement the above function to get input data
target_list = ['nicotine', 'breast cancer', 'lung cancer']
specie_name = 'homo sapiens'
full_df = pd.DataFrame()
for target in target_list:
    df = api_request(target, specie_name)
    full_df[target] = df['name']


# simple example of tokenizing 'name' variable
## to-do: combine with the above loop
from nltk.tokenize import word_tokenize
df_tokenized = pd.DataFrame()
for target in target_list:
    df_tokenized[target] = full_df[target].apply(word_tokenize)
#df['tokenized_nicotine'] = df['name'].apply(word_tokenize)

print(df_tokenized)
# merge onto one dataframe for view
#df_merged = pd.concat([df['tokenized_nicotine'], df_bc['tokenized_breastcancer']], axis = 1)
