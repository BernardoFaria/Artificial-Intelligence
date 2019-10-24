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
    self.openSet = [list(), list(), list()]

    #For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    self.cameFrom = [dict(), dict(), dict()]

    #For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    self.gScore = [dict(), dict(), dict()]

    self.already_visited = list()

  def search(self, init, limitexp=2000, limitdepth=10, tickets=[math.inf, math.inf, math.inf]):

    def heuristic(node, destiny):  #send the tupple of coords of the nodes in auxheur
        return math.sqrt(((destiny[0]-node[0])**2)+((destiny[1]-node[1])**2))

    def total_cost(node, goal, agent): # function f that reperesent g + h
        return self.gScore[agent].get(node, math.inf) + heuristic(self.auxheur[node-1] , self.auxheur[goal-1])

    def is_goal(node1, node2, node3, agent):
        result = list()
        if (len(init) == 1):
            return [node1] == self.goal
        elif (len(init)==3):
            return [node1, node2, node3] == self.goal

    def lowest_node(node, goal, agent):

        min_cost = total_cost(node[0], goal, agent)

        small = node[0]

        for n in node[1:]:
            node_s = total_cost(n, goal, agent)

            if (node_s < min_cost):

                min_cost = node_s
                small = n

        return small


    def reconstruct_path(current, agent):
        total_path = [[[], [current]]]


        while current in self.cameFrom[agent]:
            last_node = current
            current = self.cameFrom[agent][current]
            next = go_next(current, last_node)
            total_path[0][0].extend(next)
            total_path = [[[], [current]]] + total_path
        # print(total_path)
        return total_path


    def go_next(f, to):
        for n in self.model[f]:
            if n[1] == to:
                return [n[0]]
        return [-1]


    def check_tickets(current, neighbor, agent):
        check_tickets = [0, 0, 0]

        path = reconstruct_path(current, agent)

        for step in path:

            if step[0]:
                check_tickets[step[0][0]] += 1
        next = go_next(current, neighbor)
        check_tickets[next[0]] += 1
        return all([check_tickets[i] <= tickets[i] for i in range(3)])

    def verifica_posicoes(current):
        if (len(init) == 1):
            return -1
        elif (current[0] == current[1]):
            cost_0 = total_cost(current[0], self.goal[0], 0)
            cost_1 = total_cost(current[1], self.goal[1], 1)
            if (cost_0 > cost_1):
                return 0
            else: # if (cost_0 < cost_1)
                return 1
        elif (current[1] == current[2]):
            cost_1 = total_cost(current[1], self.goal[1], 1)
            cost_2 = total_cost(current[2], self.goal[2], 2)
            if (cost_1 > cost_2):
                return 1
            else: # if (cost_1 < cost_2)
                return 2
        elif (current[0] == current[2]):
            cost_0 = total_cost(current[0], self.goal[0], 0)
            cost_2 = total_cost(current[2], self.goal[2], 2)
            if (cost_0 > cost_2):
                return 0
            else: # if (cost_0 < cost_2)
                return 2
        else:
            return -1

    for i in range (len(init)):
        self.openSet[i] = list([init[i]])
        self.gScore[i] = {init[i]:0}

    last_node = init
    while limitexp > 0 and limitdepth > 0:

        current = [math.inf, math.inf, math.inf]
        c = 3
        flag = 0
        while (flag != 1):
            for i in range(len(init)):

                current[i] = lowest_node(self.openSet[i], self.goal[i], i)

            c = verifica_posicoes(current)
            if (c != -1 ):
                self.openSet[c].remove(current[c])

            elif (c == -1 and (current not in self.already_visited)):
                for i in range(len(init)):
                    self.openSet[i].remove(current[i])

                self.already_visited.append(current)
                # print("WHAZAAAAAA")
                flag = 1
            elif (c == -1 and (current in self.already_visited)):
                for i in range(len(init)):
                    self.openSet[i].remove(current[i])

        if (is_goal(current[0], current[1], current[2], i)):
            print("Entrou no is_goal:" + str([current[0], current[1], current[2]]))
            for i in range(len(init)):
                result = reconstruct_path(current[i], i)
            return result

        for i in range(len(init)):
            for neighbor in self.model[current[i]]:

                neighbor = neighbor[1]

                next_g = self.gScore[i][current[i]] + 1

                if self.gScore[i].get(neighbor, math.inf) > next_g:
                    if not check_tickets(current[i], neighbor, i):
                        continue

                    self.cameFrom[i][neighbor] = current[i]
                    self.gScore[i][neighbor] = next_g

                if neighbor not in self.openSet[i]:

                    self.openSet[i].append(neighbor)
                    limitexp -= 1
        limitdepth -= 1

    return []
