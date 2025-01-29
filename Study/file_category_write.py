input_filename = 'books.txt'

category = {}

# Read file and process data
with open(input_filename, 'r') as f:
    lines = f.readlines()

for i in range(0, len(lines), 2):
    book = lines[i].strip()  
    genre = lines[i + 1].strip()  

    if genre not in category:
        category[genre] = [book]  
    else:
        category[genre].append(book)  


with open('books_by_genre.txt', 'w') as file:
    for genre in sorted(category.keys()):  
        books_list = "; ".join(category[genre])  
        file.write(f"{genre}: {books_list}\n") 


with open('book_titles_sorted.txt', 'w') as file:
    all_books = []
    for book_list in category.values():
        all_books.extend(book_list)  

    for book in sorted(all_books):  
        file.write(f"{book}\n")  
