from credentials.api_keys import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
import requests

def auth():
    # URLS
    AUTH_URL = 'https://accounts.spotify.com/authorize'
    TOKEN_URL = 'https://accounts.spotify.com/api/token'
    BASE_URL = 'https://api.spotify.com/v1/'


    # Make a request to the /authorize endpoint to get an authorization code
    auth_code = requests.get(AUTH_URL, {
        'client_id': SPOTIFY_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': 'https://open.spotify.com/collection/playlists',
        'scope': 'playlist-modify-private',
    })
    print(auth_code)


auth()