import itertools
from operator import itemgetter

max_slices = 0
types_pizza = 0
smallest_pizza = 0
pizza_slices_list = []
final_combination = []
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


def search_combinations():
    best_combination = 0
    global final_combination

    for i in range(len(pizza_slices_list), 0, -1):
        if best_combination == max_slices:
            break
        for seq in itertools.combinations(enumerate(pizza_slices_list), i):
            if best_combination == max_slices:
                break
            sumseq = sum(list(map(itemgetter(1), seq)))
            if sumseq <= max_slices & sumseq >= best_combination:
                best_combination = sumseq
                final_combination = [seq, best_combination]
                # print(solution)

def write_solution(namefile):
    f = open(namefile + ".out", "w")
    f.write(str(len(final_combination[0])) + '\n')
    for a in solution:
        f.write(str(a) + ' ')
    f.close()

def main():
    global pizza_slices_list
    global solution
    # namefile = 'b_small'
    # namefile = 'a_example'
    namefile = 'c_medium'
    # namefile = 'd_quite_big'
    read_file(namefile + ".in")

    print("max_slices: " + str(max_slices))
    print("types_pizza: " + str(types_pizza))
    print("smallest_pizza: " + str(smallest_pizza))
    print("pizza_slices_list: " + str(pizza_slices_list))
    print("-------------------------")

    pizza_slices_list = list(map(int, pizza_slices_list))
    search_combinations()
    print("length array solution: " + str(len(final_combination[0])))
    print(final_combination)
    solution = list(map(itemgetter(0), final_combination[0]))
    print("-------------------------\n")
    print("solution to print: " + str(solution))
    write_solution(namefile)


if __name__ == "__main__":
    main()