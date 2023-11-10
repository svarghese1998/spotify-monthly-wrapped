from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import spotipy
import streamlit as st


def connection():
    """Sets up the spotify Connection"""
    scope = "user-top-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=st.secrets["SPOTIPY_CLIENT_ID"], client_secret=st.secrets["SPOTIPY_CLIENT_SECRET"], redirect_uri=st.secrets["SPOTIPY_REDIRECT_URI"],scope=scope))
    return sp


def dispay_artist():
    """This will load and display the top 10 short term artists for the person entering the website"""
    sp = connection()
    sp_range = "short_term"
    top_artists_result = sp.current_user_top_artists(time_range=sp_range, limit=10)
    top_artists_list = top_artists_result["items"]
    top_artists_dict = {}
    for i, artist in enumerate(top_artists_list):
        if i == 0:
            st.subheader(f" 🏅 {artist['name']} ")
            artist_image_url = artist["images"][0]["url"]
            st.image(artist_image_url)
            continue

        st.subheader(f"{i+1}.)  {artist['name']} ")
        top_artists_dict[i + 1] = artist["name"]


def dispay_tracks():
    """This will load and display the top 10 short term tracks for the user entering the website"""
    sp = connection()
    sp_range = "short_term"
    top_tracks = sp.current_user_top_tracks(time_range=sp_range, limit=10)
    for i, track in enumerate(top_tracks["items"]):
        if i == 0:
            st.subheader(f" 🏅 {track['name']} ")
            track_image_url = track["album"]["images"][0]["url"]
            st.image(track_image_url)
            continue
        st.subheader(f"{i+1}.)  {track['name']}")


############################################
## Below is the code of the streamlit app ##
############################################
col1, col2, col3 = st.columns(3)
currentMonth = datetime.now().strftime("%B")
col2.title(f"Your {currentMonth} Spotify Wrapped👇🏿")

if col2.button("🎁Unvail"):
    left_column, right_column = st.columns(2)
    st.balloons()
    with left_column:
        st.title("Top Tracks 🏆")
        dispay_tracks()

    with right_column:
        st.title("Top Artists 🏆")
        dispay_artist()
