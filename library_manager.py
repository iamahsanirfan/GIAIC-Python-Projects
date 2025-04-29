import json

def load_library():
    try:
        with open('library.txt', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The library file is corrupted. Starting with an empty library.")
        return []

def save_library(library):
    with open('library.txt', 'w') as f:
        json.dump(library, f)

def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    while True:
        year_str = input("Enter the publication year: ").strip()
        try:
            year = int(year_str)
            if year < 0:
                print("Please enter a valid year.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the year.")
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    while read_status not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_status == 'yes'
    book = {
        'title': title,
        'author': author,
        'publication_year': year,
        'genre': genre,
        'read_status': read
    }
    library.append(book)
    print("Book added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    removed = False
    # Iterate backwards to avoid index issues when removing items
    for i in reversed(range(len(library))):
        if library[i]['title'].lower() == title.lower():
            del library[i]
            removed = True
    if removed:
        print("Book removed successfully!")
    else:
        print("No book found with that title.")

def search_books(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    while choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 or 2.")
        choice = input("Enter your choice: ").strip()
    search_term = input("Enter the search term: ").strip().lower()
    results = []
    if choice == '1':
        for book in library:
            if search_term in book['title'].lower():
                results.append(book)
    else:
        for book in library:
            if search_term in book['author'].lower():
                results.append(book)
    if not results:
        print("No matching books found.")
    else:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            status = "Read" if book['read_status'] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")

def display_all_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        status = "Read" if book['read_status'] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {status}")

def display_statistics(library):
    total = len(library)
    if total == 0:
        print("Total books: 0")
        print("Percentage read: 0.0%")
        return
    read_count = sum(1 for book in library if book['read_status'])
    percentage = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

def main():
    library = load_library()
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()