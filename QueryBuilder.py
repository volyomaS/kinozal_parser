class QueryBuilder:
    def __init__(self):
        self.__query = "https://kinozal-tv.appspot.com/browse.php?"
        self.__name = "s="
        self.__q = ""

    def add_name(self, film_name):
        self.__name += f"{film_name} "

    def add_year(self, year):
        self.__q += f"d={year}&"

    def add_quality(self, quality):
        self.__name += f"{quality} "

    def build(self):
        return self.__query + self.__name.strip() + "&" + self.__q
