# Michael Cozzolino 
def main():
    newlist = []
    infile = open('bestsellers.txt', 'r')
    books = infile.readlines()
    infile.close()
    for book in books:
        book = book.rstrip('\n')
        #string = str(books[index])
        x = book.split('\t')
        newlist.append(x[0])
    print (newlist)
    search = str(input('insert keyword'))
    matchlist = []
    for o in newlist:
        if search in o:
            matchlist = newlist[o]
    print(matchlist)
        

    
if __name__ == '__main__':
    main()
# Michael Cozzolino
