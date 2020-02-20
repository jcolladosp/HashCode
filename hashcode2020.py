import itertools
from operator import itemgetter

# Primera linea
total_books = 0
total_libraries = 0
total_days = 0

# Segona linea
books_scores = []

# Ter
libraries = []
library = {'number_books': 0, 'signup_time': 0, 'ship_limit': 0, 'books': [0, 1, 2]}


def read_file(fname):
    global total_books
    global total_libraries
    global total_days
    global books_scores
    global libraries


    with open(fname) as f:
        for i, l in enumerate(f):
            if i == 0:
                total_books = int(l.split()[0])
                total_libraries = int(l.split()[1])
                total_days = int(l.split()[2])
            elif i == 1:
                books_scores = l.split()
            elif len(l.split()) == 3:
                number_books = l.split()[0]
                signup_time = l.split()[1]
                ship_limit = l.split()[2]

                libraries.append({'number_books': number_books, 'signup_time': signup_time, 'ship_limit': ship_limit, 'books': []})
            else:
                libraries[len(libraries)-1]['books'] = l.split()

def write_solution(namefile):
    f = open(namefile + ".out", "w")
    # f.write(str(len(pizza_slices_list[0])) + '\n')


# for a in solution:
#    f.write(str(a) + ' ')
# f.close()


def main():
    read_file("problem/a_example.txt")

    print("total_books: " + str(total_books))
    print("total_libraries: " + str(total_libraries))
    print("total_days: " + str(total_days))
    print("-----------------------")
    print("books_scores: " + str(books_scores))
    print(libraries)


if __name__ == "__main__":
    main()
