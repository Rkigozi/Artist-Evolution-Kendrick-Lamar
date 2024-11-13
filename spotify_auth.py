import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up authentication
auth_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
)
sp = spotipy.Spotify(auth_manager=auth_manager)
