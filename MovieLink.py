class MovieLink:
    def __init__(self, name: str, releaseYear: int, link: str, imageLink: str, quality: str, size: str, duration: str) -> None:
        self.__name = name
        self.__releaseYear = releaseYear
        self.__link = link
        self.__imageLink = imageLink
        self.__quality = quality
        self.__size = size
        self.__duration = duration
