from api.api_v1.movies.storage import Storage


storage = Storage()


def get_storage() -> Storage:
    return storage