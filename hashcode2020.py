import itertools
from operator import itemgetter


max_slices = 0
types_pizza = 0
smallest_pizza = 0
pizza_slices_list = []
solution = []


def read_file(fname):
    global max_slices
    global types_pizza
    global smallest_pizza
    global pizza_slices_list

    with open(fname) as f:
        for i, l in enumerate(f):
            if i == 0:
                max_slices = int(l.split()[0])
                types_pizza = int(l.split()[1])
            if i == 1:
                smallest_pizza = int(l.split()[0])
                pizza_slices_list = l.split()


def write_solution(namefile):
    f = open(namefile + ".out", "w")
    f.write(str(len(pizza_slices_list[0])) + '\n')
    for a in solution:
        f.write(str(a) + ' ')
    f.close()


def main():
    global pizza_slices_list
    # read_file("a_example.in")
    # read_file("b_small.in")
    # read_file("c_medium.in")
    read_file("d_quite_big.in")

    print("max_slices: " + str(max_slices))
    print("types_pizza: " + str(types_pizza))
    print("smallest_pizza: " + str(smallest_pizza))
    print("pizza_slices_list: " + str(pizza_slices_list))
    print("-------------------------")

    pizza_slices_list = list(map(int, pizza_slices_list))

    print("length array solution: " + str(len(solution[0])))


if __name__ == "__main__":
    main()
