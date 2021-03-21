from class_book import Book
import copy

def main():
    pushkin = Book()
    print(pushkin)
    pushkin_copy = copy.copy(pushkin)
    andrianov = Book("Andrianov", "typing on PC", 2007, "self-teacher")
    print(andrianov)
    gosher = Book("Gosher", "HTML5", 2015, "tutorial")

    print(pushkin_copy)
    print(gosher)


if __name__ == "__main__":
    main()