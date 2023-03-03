class Review:
    all = []

    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        Review.all.append(self)

    def get_rating(self):
        return self._rating  
    
    def set_rating(self, rating):
        if isinstance(rating, int) and (0 < rating < 6):
            self._rating = rating
        else:
            print("Invalid rating")

    rating = property(get_rating, set_rating)

    def get_viewer(self):
        return self._viewer  
    
    def set_viewer(self, viewer):
        from classes.Viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            print("viewer is not in Viewer class")

    viewer = property(get_viewer, set_viewer)

    def get_movie(self):
        return self._movie  
    
    def set_movie(self, movie):
        from classes.Movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            print("movie is not in Movie class")

    movie = property(get_movie, set_movie)


        


    

    # movie property goes here!
