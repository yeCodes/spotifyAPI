# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 17:32:39 2022

@author: Y
"""

# https://requests.readthedocs.io/en/latest/user/quickstart/ - quickstart guide for library
# can go to fundamental library + look up general quickstart/ intro OR specific methods from library used
import requests

# https://developer.spotify.com/console/post-next/?device_id=
# Oauth == authentication key generated on tihs page - https://developer.spotify.com/console/post-next/?device_id=


SPOTIFY_PLAY_NEXT_TRACK_URL= 'https://api.spotify.com/v1/me/player/next'
SPOTIFY_ACCESS_TOKEN = 'BQD9Zim7gbQ-JsoOa4fr2k7BPAQSoW6iHIWPyWsrKjmNJe7x6W5GzCUlrIByIdJkjGoBObePvasvP7bvmfP-NPh_qWIIFd6bKsJEOOg3pAe2GMaV3_fguBQNOhLjgC_vfJPSz_i8ar89wFP2E7cE9muGGBuIJPTpgRhDLar4-hu8u5w'

def playNextTrack(access_token):
    
    # post request here. not returning anything or getting anything
    requests.post(
        SPOTIFY_PLAY_NEXT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    #json_resp = response.json()
    #return

def main():
    changeTrack = playNextTrack(
        SPOTIFY_ACCESS_TOKEN
        )
    
if __name__ == '__main__':
    main()