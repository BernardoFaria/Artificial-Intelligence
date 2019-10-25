def getKey(node):
    return node[0]


def main():

    a = [[1, 2], [0, 1]]
    a = sorted(a, key=getKey)
    print(a)

main()
