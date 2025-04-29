from api.moviesAPI import MoviesAPI


class APIManager:
    """
    Class for managing api manager
    """
    def __init__(self, session):
        self.session = session
        self.movies_api = MoviesAPI(session)