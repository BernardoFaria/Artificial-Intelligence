import pickle

pickle_in1 = open("coords.pickle", "rb")
example_in1 = pickle.load(pickle_in1)
file = open("coords.pickle.out", "w+")
file.write(str(example_in1))
file.close()


pickle_in2 = open("mapasgraph.pickle", "rb")
example_in2 = pickle.load(pickle_in2)
file = open("mapasgraph.pickle.out", "w+")
file.write(str(example_in2))
file.close()