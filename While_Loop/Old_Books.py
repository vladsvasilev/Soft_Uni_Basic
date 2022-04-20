# While_Loop_Exercise
# 01 - Old Books

book = input()

book_count = 0
book_found = False
next_book = input()
while next_book != "No More Books":

    if next_book == book:
        book_found = True
        break

    book_count += 1
    next_book = input()
if book_found:
    print(f"You checked {book_count} books and found it.")
else:
    print(f"The book you search is not here!")
    print(f"You checked {book_count} books.")


