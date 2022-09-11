# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:54:27 2022

@author: Y
"""

import requests
from pprint import pprint
from datetime import datetime
import pandas as pd
# https://datagy.io/python-string-to-date/


# https://developer.spotify.com/console/get-current-user-saved-tracks/?market=&limit=&offset=
SPOTIFY_GET_USER_SAVED_TRACKS = 'https://api.spotify.com/v1/me/tracks' 
SPOTIFY_ACCESS_TOKEN = 'BQAt9NQe6mCUQgL8gHEfhpunQ2qqp6UW-RWrkNAAURUREzqMRxf4ksb1mRVJH7j4r7NKl-jnnmLwWS2IpviTgxngqu-4HWWkRwqulun1AiYtMKixrrs9eYOafhayvFaZq8dtNHyx-I1bw-DS66gM49QwLSRB3r5dgWLWa_uhQmbP2IqGiAshppoD'
accessTokenTrackDetails = ''

def getUserPlaylists(access_token):
    
    response = requests.get(
        SPOTIFY_GET_USER_SAVED_TRACKS,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    currentTrackName = [] 
    currentTrackURL = [] 
    currentTrackAPIURL = []
    currentDateAdded = []
    currentTrackId = []
    
    for i in resp_json['items']:
        
        currentTrackName.append(i['track']['name'])
        currentTrackURL.append(i['track']['external_urls']['spotify'])
        currentTrackAPIURL.append(i['track']['href'])
        currentTrackId.append(i['track']['id'])
        currentDateAdded.append(i['added_at'])
     
    # https://datagy.io/pandas-dataframe-from-list/
    zipped = list(zip( currentTrackName, currentTrackURL, currentTrackAPIURL, currentTrackId, currentDateAdded))
    
    # convert to dataframe
    df = pd.DataFrame(zipped, columns = ['trackName', 'trackURL', 'trackAPIURL', 'trackID', 'dateAdded'])
    
    df.loc[:,'dateAdded'] = formatDate(df.loc[:,'dateAdded'])
    savedTracks = df
        

    # return dictionary
    return savedTracks
    
    
def formatDate(series):
    
    for i in series:
        text = i.split("T")
        date = text[0]
        date = datetime.strptime(date, '%Y-%m-%d')
        #time = text[1]
    return date
    
    
def getTrackInfo(df):
    
    # https://reactgo.com/python-convert-list-to-comma-string/#:~:text=Python%20has%20a%20built-in%20String%20join%20%28%29%20method,%22b%22%2C%20%22c%22%29%20x%20%3D%20%22%2C%22.join%28myList%29%20print%28x%29%20Output%3A%20a%2Cb%2Cc
    commaSepList = ",".join(df.loc[:, 'trackID'])
    
    
    # API description of audio features - https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features
    AUTH = 'BQAYFjwL2hAtAAgnVXTujqY42pxjxZcxwJ6zfVZRMlaYTJMpbr_AgVArMFktKhmHmbSM0UqOa8p5uiS9jgEVpFiq0AIyPGEaOS6WZJ8HfWOn2i5ioCsomiJP2s2-3WyVAVFzaIJHAHQN0OCk0z2mN13661g99tsLnXtcqbOVg68'
    getTrackAudioFeatures = '	https://api.spotify.com/v1/audio-features'
    
    # how to attach payload ot get request - https://requests.readthedocs.io/en/latest/user/quickstart/
    payload = {'ids': commaSepList}
    
    response = requests.get(
        getTrackAudioFeatures,
        params = payload,
        headers={
            "Authorization": f"Bearer {AUTH}"
        }
    )
    resp_json = response.json()
     
    featuresDictionary = resp_json['audio_features']
    featuresDf = pd.DataFrame.from_dict(featuresDictionary)
    
    df2 = pd.concat([df, featuresDf], axis = 1, join ='inner')
    
    
    return df2
    

def main():
    savedTracks = getUserPlaylists(
        SPOTIFY_ACCESS_TOKEN
        )
    
    
    pprint(savedTracks, indent = 4) 
    
    dataGrid = getTrackInfo(savedTracks)
    dataGrid.to_csv(r"*****Enter location to save CSV in", index=False, header=True)
    
if __name__ == '__main__':
    main()

        