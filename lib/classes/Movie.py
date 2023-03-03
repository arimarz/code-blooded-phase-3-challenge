from classes.Review import Review


class Movie:

    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def get_title(self):
        return self._title  
    
    def set_title(self, title):
        if isinstance(title, str) and (0 < len(title)):
            self._title = title
        else:
            print("Invalid title")

    title = property(get_title, set_title)

    def reviews(self):
        return [review for review in Review.all if review.movie == self]

    def reviewers(self):
        return [review.viewer for review in self.reviews()]

    def average_rating(self):
        sum_ratings = sum([review.rating for review in self.reviews()])
        num_ratings = len(self.reviews())
        return sum_ratings / num_ratings
    
    @classmethod
    def highest_rated(cls):
        highest_rating = 0
        highest_movie = None
        for movie in cls.all:
            rating = movie.average_rating()
            if rating > highest_rating:
                highest_movie = movie
                highest_rating = rating
        return highest_movie
