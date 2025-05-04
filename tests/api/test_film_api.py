from api.api_manager import APIManager
import pdb


class TestAPI:
    def test_all_films(self, api_manager: APIManager):
        """
        Positive test to get all films
        """
        response = api_manager.movies_api.get_list_movies().json()

        assert isinstance(response["movies"], list), "Movies not a list"
        assert len(response["movies"]) > 0, "No movies found"

    def test_all_films_with_params(self, api_manager: APIManager):
        """
        films with params
        """
        response_data = api_manager.movies_api.get_list_movies(params={"locations": "SPB"}).json()
        movies = response_data["movies"]
        for movie in movies:
            assert movie["location"] == "SPB", f"Film : {movie['name']} with another location {movie['location']} "


    def test_add_new_film(self, api_manager: APIManager, create_film):
        """
        Add new film
        """
        create_film
        data_film = create_film
        for field in ["id", "name", "description", "genreId", "imageUrl", "price", "location", "published",
                      "createdAt"]:
            assert field in data_film, f"Нет поля {field} в ответе"

    def test_deleted_film(self, api_manager: APIManager, movie_lifecycle):
        """
        Check if film is deleted
        """
        movie_lifecycle

"""
Две фикстуры, делают примерно то же самое, но зачем я создал две?
В первой мы получаем response, созданного фильма, проверка на создание фильма пройдена
затем фикстура удаляет созданный фильм -> фикстура не падает = фильм удаляется без проблем

для movie_lifecycle я вопроизвел весь жизненный путь фильма и проверил,что фильм действительно удален (404)
вопрос: такая реализация правильная или можно было БЫ сделать в одной фикстуре?
"""
