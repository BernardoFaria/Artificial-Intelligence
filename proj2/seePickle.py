import pickle

pickle_in2 = open("mapasgraph2.pickle", "rb")
example_in2 = pickle.load(pickle_in2)
file = open("mapasgraph.pickle.out", "w+")
file.write(str(example_in2))
file.close()
