# Artist-Evolution-Kendrick-Lamar

# Kendrick Lamar: Artist Evolution Analysis

This project analyzes Kendrick Lamar's musical evolution by exploring changes in key metrics such as energy, tempo, popularity, and danceability across his albums. Using data from Spotify, I examined trends in his music over time to understand his artistic growth.

## Project Structure

- **Data Collection**: Used the Spotify API to gather data on Kendrick’s discography.
- **Data Preparation**: Cleaned and organized the data for analysis.
- **Exploratory Analysis**: Visualized key metrics to identify trends and changes across Kendrick's albums.
- **Summary**: Provided insights into Kendrick’s stylistic shifts over his career.

## Key Findings

- Early albums show higher energy, fitting Kendrick’s intense style.
- Later albums reflect more experimental and introspective tones.
- *DAMN.* stands out in popularity, showing Kendrick’s peak in mainstream appeal.

## Requirements

- **Python libraries**: `pandas`, `matplotlib`, `seaborn`, `spotipy`, and `dotenv`.
- **Spotify API**: A Spotify developer account and API credentials are required.

## How to Run

1. Clone the repository.
2. Set up your environment with required libraries.
3. Run the Jupyter Notebook to view the full analysis.

## Setting Up Spotify Credentials

To run this project, you’ll need Spotify API credentials.

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create a new app.
2. Copy the **Client ID** and **Client Secret** into a `.env` file in the project root directory:

   ```plaintext
   SPOTIPY_CLIENT_ID='your-client-id'
   SPOTIPY_CLIENT_SECRET='your-client-secret'
   SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

