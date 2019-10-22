import math
import pickle
import time



class SearchProblem:
  def __init__(self, goal, model, auxheur=[]):
    self.goal = goal #obejtivo
    self.model = model #grafo com as transicoes entre localizacoes
    self.auxheur = auxheur

    #The set of discovered nodes that may need to be (re-)expanded.
    #Initially, only the start node is known.
    self.openSet = list()

    #List of parents
    # self.parents = []

    #For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    self.cameFrom = dict()

    #For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    self.gScore = dict()

  def search(self, init, limitexp=2000, limitdepth=10, tickets=[math.inf, math.inf, math.inf]):

    def heuristic(node, destiny):  #send the tupple of coords of the nodes in auxheur
        return math.sqrt(((destiny[0]-node[0])**2)+((destiny[1]-node[1])**2))

    def total_cost(node, goal): # function f that reperesent g + h
        # print("Node:" + str(node))
        # print("Goal:" + str(goal))
        # print("gScore:" + str(self.gScore.get(node, math.inf)))
        # print("auxheur:" + str(heuristic(self.auxheur[node-1] , self.auxheur[goal-1])))
        # print("\n")
        return self.gScore.get(node, math.inf) + heuristic(self.auxheur[node-1] , self.auxheur[goal-1])

    def is_goal(node):
        return node == self.goal[0]

    def lowest_node(node, goal):
        #0 is the node that is fScore.key() and 1 is the cost that is fScore.value()

        print("Node antes do if:")
        print(node)
        min_cost = total_cost(node[0], goal)

        small = node[0]

        for n in node[1:]:
            node_s = total_cost(n, goal)
            if (node_s < min_cost):
                min_cost = node_s
                small = n

        return small


    def reconstruct_path(current):
        total_path = [[[], [current]]]
        while current in self.cameFrom:
            last_node = current
            current = self.cameFrom[current]
            next = go_next(current, last_node)
            total_path[0][0].extend(next)
            total_path = [[[], [current]]] + total_path
        return total_path


    def go_next(f, to):
        for n in self.model[f]:
            if n[1] == to:
                return [n[0]]
        return [-1]


    def check_tickets(current, neighbor):
        check_tickets = [0, 0, 0]
        path = reconstruct_path(current)
        for step in path:

            if step[0]:
                check_tickets[step[0][0]] += 1
        next = go_next(current, neighbor)
        check_tickets[next[0]] += 1
        return all([check_tickets[i] <= tickets[i] for i in range(3)])




    self.openSet = list(init)
    self.gScore = {init[0]:0}


    while self.openSet:
        #the node in openSet having the lowest fScore[] value
        current = lowest_node(self.openSet, self.goal[0])
        print("Current no while")
        print(current)

        if (is_goal(current)):
            return reconstruct_path(current)

        self.openSet.remove(current)
        # print("Current:")
        # print(current)
        # print("Model:")
        # print(self.model[current])

        for neighbor in self.model[current]:
            neighbor = neighbor[1]
            print(self.gScore)
            next_g = self.gScore[current] + 1

            if self.gScore.get(neighbor, math.inf) > next_g:
                if not check_tickets(current, neighbor):
                    print("----")
                    continue

                self.cameFrom[neighbor] = current
                self.gScore[neighbor] = next_g

                if neighbor not in self.openSet:
                    self.openSet.append(neighbor)
    return "RiP"
