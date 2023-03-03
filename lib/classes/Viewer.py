from classes.Review import Review


class Viewer:

    def __init__(self, username):
        self.username = username

    def get_username(self):
        return self._username  
    
    def set_username(self, username):
        if isinstance(username, str) and (6 <= len(username) <= 16):
            self._username = username
        else:
            print("Invalid username")

    username = property(get_username, set_username)

    def reviews(self):
        return [review for review in Review.all if review.viewer == self]

    def reviewed_movies(self):
        return [review.movie for review in self.reviews()]

    def movie_reviewed(self, movie):
        return any(review.movie == movie for review in self.reviews())

    def rate_movie(self, movie, rating):
        Review(self, movie, rating)
