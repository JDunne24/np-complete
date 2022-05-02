from curses import has_key
from itertools import permutations


def findLongestPath(edge_dict, node_set, num_nodes):
    longest_path_weight = 0
    for i in range(2, num_nodes + 1):
        paths = permutations(node_set, i)
        for path in paths:
            path_exists = True
            path_weight = 0
            for j in range(len(path) - 1):
                if path_exists:
                    if not edge_dict.has_key(([path[j], path[j+1]])):
                        path_exists = False
                    else:
                        path_weight += edge_dict[([path[j], path[j+1]])]
            if path_exists:
                if longest_path_weight < path_weight:
                    longest_path_weight = path_weight
                    longest_path = list()
                    for k in range(len(path)):
                        longest_path.append(path[k])
    return longest_path
    
def main():
    num_nodes = int(input)
    num_edges = int(input)
    edges = dict()
    nodes = set()
    for i in range(num_edges):
        string = str(input).split()
        edges[(string[1], string[2])] = string[3]
        nodes.add(string[1])
        nodes.add(string[2])
    print(findLongestPath(edges, nodes, num_nodes))

if __name__ == "__main__":
    main()