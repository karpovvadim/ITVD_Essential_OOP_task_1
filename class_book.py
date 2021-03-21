import copy


class Book:
    def __init__(self, author="Pushkin", name="Ruslan_and_Ludmila", publication_year=1820, genre="poem"):
        self._author = author
        self._name = name
        self._publication_year = publication_year
        self._genre = genre

    #def __eq__(self, other):
        #return self.real == other.real and self.imaginary == other.imaginary

    def __str__(self):
        return "Book(%s, %s, %s, %s)" % (self._author, self._name, self._publication_year, self._genre)

 #   def __repr__(self):
 #       return "321"
