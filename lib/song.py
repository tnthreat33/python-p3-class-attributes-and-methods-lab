class Song:
    count = 0 
    genres = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count() 
        self.add_to_genre(genre)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.appends(genre)


