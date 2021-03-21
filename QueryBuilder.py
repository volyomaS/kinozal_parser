class QueryBuilder:
    def __init__(self) -> None:
        self.__query = "https://kinozal-tv.appspot.com/browse.php?"
        self.__name = "s="
        self.__q = ""

    def add_name(self, film_name: str) -> None:
        self.__name += f"{film_name} "

    def add_year(self, year: int) -> None:
        self.__q += f"d={year}&"

    def add_quality(self, quality: str) -> None:
        self.__name += f"{quality} "

    def build(self) -> str:
        return self.__query + self.__name.strip() + "&" + self.__q
