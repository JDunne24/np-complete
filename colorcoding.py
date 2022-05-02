def main():

    n = input()
    e = input()
    graph = dict()

    for _ in e:
        myList = input().split()
        graph[(myList[1], myList[2])] = myList[0]

    colors = dict()

    def color(graph, k):
        x = 0
        for vertex in graph:
            colors[vertex] = x
            x += 1
            if x >= k:
                x = 0

    color(graph, n)

    visited = set()

    for x in graph:
        if x not in visited:
            set.add(x)

        



if __name__ == "__main__":
    main()
