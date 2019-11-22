# shows a user's playlists (need to be authenticated via oauth)

# SPOTIPY_CLIENT_ID='3c7bae39aa2b4ea0b4e11f8a09f01071'
# SPOTIPY_CLIENT_SECRET=''
# SPOTIPY_REDIRECT_URI='http://mysite.com'

import sys
import spotipy
import spotipy.util as util
import os
os.environ["SPOTIPY_CLIENT_ID"] = "3c7bae39aa2b4ea0b4e11f8a09f01071"
os.environ["SPOTIPY_CLIENT_SECRET"] = ""
os.environ["SPOTIPY_REDIRECT_URI"] = "https://github.com/m4ni5h/"

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print ("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    username = "M4NI5H"
    # else:
    #     print ("Whoops, need your username!")
    #     print ("usage: python user_playlists.py [username]")
    #     sys.exit()
    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print (playlist['name'])
                print ('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print ("Can't get token for", username)