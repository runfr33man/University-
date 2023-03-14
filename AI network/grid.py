import numpy as np
# genetic algorithm search of the one max optimization problem
from numpy.random import randint
from numpy.random import rand

# CREATE A RANDOMLY POPULATED LIST OF LISTS
# cellMAP = np.random.randint(2, size=(11, 7))
# print(cellMAP)

# [[1 0 0 1 0 0]
#  [1 1 0 1 0 1]
#  [1 1 1 0 0 0]
#  [1 0 0 1 0 0]
#  [1 1 1 1 1 0]
#  [0 0 1 1 1 0]]

# ITERATE OVER EACH ROW/COLUMN VALUE
# for row in range(cellMAP.shape[0]):
#    for column in range(cellMAP.shape[1]):
#        print(cellMAP[row][column])

# 1
# 0
# 0
# 1
# 0
# 0
# 1
# 1
# 0... etc


# ----GOAL-----
'''
fi_grid = [[1, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0],
           [1, 0, 0, 0, 1, 0, 0],
           [1, 0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0, 0],
           [1, 0, 1, 0, 0, 0, 0],
           [1, 0, 0, 1, 0, 0, 0],
           [1, 0, 0, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 1, 0],
           [1, 0, 0, 0, 0, 0, 1]]
           
s_grid = [[1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0],
          [1, 0, 0, 0, 1, 0, 0],
          [1, 0, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 0, 0],
          [1, 0, 0, 1, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0, 0]]
'''

# 1
# 0
# 0
# 0
# 0
# 1
# 0
# 1
# 0
# 0... ETC


choice = int(input("Choose the grid you want to run the program for:\n1 for K and 2 for D\n"))
while choice != 1 and choice != 2:
    print("Please input a valid number!")
    choice = int(input("Choose the grid you want to run the program for:\n1 for K and 2 for D\n"))


def objective(x):
    global choice
    goal = np.random.randint(1, size=(11, 7))
    if choice == 1:
        goal[0,0],goal[0,6] = 1,1
        goal[1,0],goal[1,5] = 1,1
        goal[2,0],goal[2,4] = 1,1
        goal[3,0],goal[3,3] = 1,1
        goal[4,0],goal[4,2] = 1,1
        goal[5,0],goal[5,1] = 1,1
        goal[6,0],goal[6,2] = 1,1
        goal[7,0],goal[7,3] = 1,1
        goal[8,0],goal[8,4] = 1,1
        goal[9,0],goal[9,5] = 1,1
        goal[10,0],goal[10,6] = 1,1
    else:
        goal[0,0],goal[0,1] = 1,1
        goal[1,0],goal[1,2] = 1,1
        goal[2,0],goal[2,3] = 1,1
        goal[3,0],goal[3,4] = 1,1
        goal[4,0],goal[4,5] = 1,1
        goal[5,0],goal[5,5] = 1,1
        goal[6,0],goal[6,5] = 1,1
        goal[7,0],goal[7,4] = 1,1
        goal[8,0],goal[8,3] = 1,1
        goal[9,0],goal[9,2] = 1,1
        goal[10,0],goal[10,1] = 1,1
    dif = 0

    for row in range(goal.shape[0]):
        for column in range(goal.shape[1]):
            if goal[row][column] != x[row][column]:
                dif += 1

    return dif


def createGrid(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
    # initial population of random bitstring
    pop = []
    pop = [np.random.randint(2, size=(11, 7)) for _ in range(n_pop)]
    scores = []

# keep track of best solution
    best, best_eval = 0, objective(pop[0])
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best \n%s = %.3f" % (gen,  pop[i], scores[i]))

                if scores[i] == 0:
                    return [best, best_eval]
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]

# mutation operator 
def mutation(grid , r_mut):

    tmpGridList = []
    for row in range(grid.shape[0]):
        for column in range(grid.shape[1]):
            tmpGridList.append(grid[row][column])
    for i in range(len(tmpGridList)):
        # check for a mutation
        if rand() < r_mut:
            # flip the bit
            if tmpGridList[i] == 0:
                tmpGridList[i] = 1
            else:
                tmpGridList[i] = 0

    gridarr = np.array(tmpGridList)

    grid = np.reshape(gridarr, (11, 7))


def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        tmpp1List = []
        for row in range(p1.shape[0]):
            for column in range(p1.shape[1]):
                tmpp1List.append(p1[row][column])

        tmpp2List = []
        for row in range(p2.shape[0]):
            for column in range(p2.shape[1]):
                tmpp2List.append(p2[row][column])

        pt = randint(1, len(tmpp1List)-1)

        # perform crossover

        tmpC1List, tmpC2List = tmpp1List.copy(), tmpp2List.copy()
        tmpC1List = tmpp1List[:pt] + tmpp2List[pt:]
        tmpC2List = tmpp2List[:pt] + tmpp1List[pt:]

        c1arr = np.array(tmpC1List)
        c2arr = np.array(tmpC2List)

        c1 = np.reshape(c1arr, (11, 7))
        c2 = np.reshape(c2arr, (11, 7))

    return [c1, c2]


# tournament selection
def selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


# define the total iterations
n_iter = 100
# bits
n_bits = 20
# define the population size
n_pop = 500
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)
# perform the genetic algorithm search
best, score = createGrid(objective, n_bits, n_iter, n_pop, r_cross, r_mut)

print('Done!')
print('%s = %f' % (best, score))
