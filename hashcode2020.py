import itertools
from operator import itemgetter

# Primera linea
from urllib3.connectionpool import xrange

total_books = 0
total_libraries = 0
total_days = 0

# Segona linea
books_scores = []

# Ter
libraries = []
library = {'number_books': 0, 'signup_time': 0, 'ship_limit': 0, 'books': [0, 1, 2]}

sorted_libraries = []
sorted_solution_libraries = []


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
            elif i % 2 == 0:
                number_books = l.split()[0]
                signup_time = l.split()[1]
                ship_limit = l.split()[2]

                libraries.append(
                    {'number_books': number_books, 'signup_time': signup_time, 'ship_limit': ship_limit, 'books': []})
            elif i % 2 != 0:
                libraries[len(libraries) - 1]['books'] = l.split()




def logic():
    global sorted_solution_libraries
    global sorted_libraries
    for library in libraries:
        for i, book in enumerate(library['books']):
            library['books'][i] = (book, books_scores[int(book)])
        sorted_library = sorted(library['books'], key=lambda x: x[1], reverse=True)
        sorted_libraries.append(sorted_library)
    print(sorted_libraries)

    seen = set()
    repeated = set()
    for l in sorted_libraries:
        for i in set(l):
            if i in seen:
                repeated.add(i)
            else:
                seen.add(i)

    print("repeated: " + str(repeated))
    for a, element_to_remove in enumerate(repeated):
        for i in [x for x in xrange(len(sorted_libraries)) if x != a]:
            if element_to_remove in sorted_libraries[i]:
                sorted_libraries[i].remove(element_to_remove)
    solution_libraries = []
    for i, library in enumerate(sorted_libraries):
        solution_libraries.append((library, libraries[i]['signup_time'], i))
    print("solution libraries: " + str(solution_libraries))
    sorted_solution_libraries = sorted(solution_libraries, key=lambda x: x[1])
    print("-------------------------")
    print("sorted_solution_libraries: " + str(sorted_solution_libraries))


def write_solution(namefile):
    f = open(namefile + "_output.txt", "w")
    f.write(str(len(sorted_solution_libraries)) + '\n')
    for library in sorted_solution_libraries:
        f.write(str(library[2]) + " " + str(len(library[0])) + '\n')
        for a in library[0]:
            f.write(str(a[0]) + ' ')
        f.write('\n')
    f.close()


def main():
    #file = "a_example"
    #file = "b_read_on"
    #file = "c_incunabula"
    #file = "d_tough_choices"
    #file = "e_so_many_books"
    file = "f_libraries_of_the_world"



    read_file("problem/" + file + ".txt")
    logic()
    print("total_books: " + str(total_books))
    print("total_libraries: " + str(total_libraries))
    print("total_days: " + str(total_days))
    print("-----------------------")
    print("books_scores: " + str(books_scores))
    print(libraries)
    print("-----------------------")
    print(sorted_libraries)

    write_solution(file)

if __name__ == "__main__":
    main()
