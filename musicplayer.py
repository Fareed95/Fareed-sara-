import os

# Dictionary mapping song names to their file paths
music = {
    "devotion": r"C:\Users\Admin\Music\Tasbeehat al Zaahra.mpeg",
    "kahani suno": r"C:\Users\Admin\Music\kahani suno.mp3"
}

def player(song_name):
    # Check if the song name exists in the dictionary
    if song_name in music:
        music_file_path = music[song_name]
        os.startfile(music_file_path)
    else:
        print(f"Song '{song_name}' not found in the music dictionary.")

# Call the player function with the song name
# player("devotion")
