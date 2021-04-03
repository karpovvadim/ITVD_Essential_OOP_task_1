import copy


class Book:
    def __init__(self, author="Pushkin", title="Ruslan_and_Ludmila", publication_year=1820, genre="poem"):
        self._author = author
        self._title = title
        self._publication_year = publication_year
        self._genre = genre

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._author == other._author and \
            self._title == other._title and \
            self._publication_year == other._publication_year and \
            self._genre == other._genre

    def __as_string(self, format_string):
        return format_string.format(
            self._author,
            self._title,
            self._publication_year,
            self._genre
        )

    def __str__(self):
        return self.__as_string("{}, {}, {}, {}")

    def __repr__(self):
        return self.__as_string("Book - publication year - {2!r}, author - {0!r}, {1}, {3}")
