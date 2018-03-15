# input_file, file with challenge_input


def bookshelf_solver(input_file):
    books = []
    books_on_shelf = []
    result = []
    counter= -1
    with open(input_file, "r") as file:
        shelfs = list(map(int, (file.readline().rstrip("\n").split(" "))))
        for line in file.readlines():
            books.append((int(line.rstrip("\n").split(" ")[0]), line.rstrip("\n").split(" ")[1:]))
    shelfs.sort(reverse=True)
    books.sort(key=lambda x: x[0], reverse=True)
    for shelf in shelfs:
        if len(books_on_shelf) == len(books):
            break
        result.append([shelf])
        counter+=1
        shelf_size = shelf
        for book in books:
            if shelf_size >= book[0] and book not in books_on_shelf:
                result[counter].append(" ".join(book[1]))
                shelf_size -= book[0]
                books_on_shelf.append(book)
    if len(books_on_shelf) != len(books):
        return "impossible"
    print("{} shelfs is needed".format(len(result)))
    for item in result:
        print(item[0]," : ",item[1:])

