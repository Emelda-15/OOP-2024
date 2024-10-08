class Movie:
    def __init__(self, title, director, release_year, genre):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
    
    def play_trailer(self):
        print(f"Playing the trailer for {self.title}...")
    
    def get_info(self):
        print(f"{self.title} ({self.release_year}), directed by {self.director}, is a {self.genre} film.")

# Example of creating an object
movie1 = Movie("Inception", "Christopher Nolan", 2010, "Science Fiction")
movie1.get_info()
movie1.play_trailer()
