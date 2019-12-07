# Bernardo Faria numero 87636 ------ Ricardo Caetano numero 87699 ---- Grupo 20 Taguspark
import random

# LearningAgent to implement
# no knowledeg about the environment can be used
# the code should work even with another environment


class LearningAgent:

    # init
    # nS maximum number of states
    # nA maximum number of action per state
    def __init__(self, nS, nA):


        self.nS = nS
        self.nA = nA

        self.epsilon = 0.25
        self.alpha = 0.1
        self.gamma = 0.65

        self.matrix_q = [[None for i in range(self.nA)] for i in range(self.nS)]

    # Select one action, used when learning
    # st - is the current state
    # aa - is the set of possible actions
    # for a given state they are always given in the same order
    # returns
    def selectactiontolearn(self, st, aa):

        # With probability (1 -epsilon) choose the action which has the highest Q-value.
        # With probability epsilon$ choose any action at random.
        matrix = self.matrix_q[st][0]
        next_action = 0

        if random.random() < self.epsilon:
            action = random.choice(aa)
            self.epsilon *= 0.999
            return aa.index(action)
        else:
            for i in range(len(aa)):
                if self.matrix_q[st][i] == None:
                    break
                if self.matrix_q[st][i] > matrix:
                    matrix = self.matrix_q[st][i]
                    next_action = i

            return next_action

    # Select one action, used when evaluating
    # st - is the current state
    # aa - is the set of possible actions
    # for a given state they are always given in the same order
    # returns
    # a - the index to the action in aa
    def selectactiontoexecute(self, st, aa):

        matrix = self.matrix_q[st][0]
        next_action = 0

        for i in range(len(aa)):
            if self.matrix_q[st][i] == None:
                continue
            if self.matrix_q[st][i] > matrix:
                matrix = self.matrix_q[st][i]
                next_action = i

        return next_action

    def next_max_q(self, st):
        # retorna a coluna do maior valor que esta na linha st
        if self.matrix_q[st][0] == None:
            self.matrix_q[st][0] = 0
            return 0

        maxQ = self.matrix_q[st][0]
        index = 0

        for i in range(len(self.matrix_q[st])):
            if self.matrix_q[st][i] == None:
                continue
            elif self.matrix_q[st][i] > maxQ:
                index = i
                maxQ = self.matrix_q[st][i]

        return index

    # this function is called after every action
    # ost - original state
    # nst - next state
    # a - the index to the action taken
    # r - reward obtained

    def learn(self, ost, nst, a, r):



        if self.matrix_q[ost][a] == None:
            self.matrix_q[ost][a] = 0

        best_next_action_index = self.next_max_q(nst)

        self.matrix_q[ost][a] = self.matrix_q[ost][a] + self.alpha * \
            (r + self.gamma *
             self.matrix_q[nst][best_next_action_index] - self.matrix_q[ost][a])