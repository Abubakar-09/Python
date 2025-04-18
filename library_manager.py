import os
import json

def load_library():
    if os.path.exists("library.txt"):
        # good
        a = 0
    else:
        with open("library.txt", "w") as file:
            json.dump([],file,indent=4)

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read_status = True if read_input == 'yes' else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    data = []
    with open("library.txt", "r") as file:
        data = json.load(file)

    data.append(book)

    with open("library.txt", "w") as file:
        json.dump(data, file, indent=4)

    print("Book added successfully!\n")            

def remove_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")

    data = []
    with open("library.txt", "r") as file:
        data = json.load(file)

    for i in data:
        if i["title"] == title and i["author"] == author :
            data.remove(i)
            print(f"Book Removed Successfully\n")

    with open("library.txt", "w") as file:
        json.dump(data, file, indent=4)            

def search_book():
    title = input("Enter the book title: ").lower()
    author = input("Enter the author: ").lower()

    data = []
    with open("library.txt", "r") as file:
        data = json.load(file)

    for i in data:
        if i["title"] == title and i["author"] == author :
            print(f"{i}\n")

def main():
    library = load_library()
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()        