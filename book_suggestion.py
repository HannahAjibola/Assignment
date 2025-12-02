book_list = []


print("Welcome to the book suggestion system!")
print("1. Add Book")
print("2. Remove Book")
print("3. Update Book")
print("4. Show all books")

home = int(input("Select an option:"))

if home == 1:
    title =  input("Enter the book title:")
    book_list.append({"title:", title})
    print("Book successfully added!")
elif home ==2:
    book_to_remove = input("Enter the book title to remove:")
    print("Book removed successfully!")
    for book in book_list:
        if book["title"] == book_to_remove:
            print("Book successfully removed!")
            break;
    else:
        print("Book not found")

elif home == 3:
    update_book = input("Enter the old title:")
    for book in book_list:
        if book["title"] == update_book:
            new_title = input("Enter old title:")
        if new_title:
            book["title"] = new_title
        print("Book successfully update!")
    else:
        print("Book not found!")

elif home == 4:
    if book_list == []:
        print("The book list is empty!")
    else:
        for book in book_list:
            print(book)















#if __name__=="__main__":
    #main():
