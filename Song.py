class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class MusicStreamingSystem:
    def __init__(self):
        self.songs = []
        self.artists = {}

    def add_song(self, song):
        self.songs.append(song)
        if song.artist not in self.artists:
            self.artists[song.artist] = []
        self.artists[song.artist].append(song)

    def view_songs(self):
        for song in self.songs:
            print(f"Title: {song.title}, Artist: {song.artist}, Duration: {song.duration} seconds")

    def view_artist_songs(self, artist):
        if artist in self.artists:
            for song in self.artists[artist]:
                print(f"Title: {song.title}, Duration: {song.duration} seconds")
        else:
            print("Artist not found")

    def search_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                return song
        return None

# Example usage:
system = MusicStreamingSystem()

song1 = Song("Song 1", "Artist A", 180)
song2 = Song("Song 2", "Artist B", 240)
song3 = Song("Song 3", "Artist A", 210)

system.add_song(song1)
system.add_song(song2)
system.add_song(song3)

print("All Songs:")
system.view_songs()

print("\nArtist A Songs:")
system.view_artist_songs("Artist A")

print("\nSearch for Song 1:")
song = system.search_song("Song 1")
if song:
    print(f"Title: {song.title}, Artist: {song.artist}, Duration: {song.duration} seconds")
else:
    print("Song not found")
