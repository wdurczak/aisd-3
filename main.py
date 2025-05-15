import argparse
from generate import GenerateAll
from userProvided import userProvidedGenerating
from select_representation import Representation
from grap_operations import GraphOperations
from collections import deque

def main():
    parser = argparse.ArgumentParser(
        description="Graf – operacje: BFS, DFS i sortowanie topologiczne"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--user-provided', action='store_true',
        help="Wczytaj graf od użytkownika"
    )
    group.add_argument(
        '--generate', action='store_true',
        help="Wygeneruj losowy graf"
    )
    args = parser.parse_args()

    if args.generate:
        gen = GenerateAll()
        nodes, saturation = gen.generateData()
        matrix = gen.generateGraph(nodes, saturation)
    else:
        gen_user = userProvidedGenerating()
        matrix = gen_user.userProvidedData()

    n = len(matrix)


    rep = Representation()
    rep_type = rep.selectRepresentation()

    adj = [[] for _ in range(n)]
    for u in range(n):
        for v, val in enumerate(matrix[u]):
            if val == 1:
                adj[u].append(v)


    ops = GraphOperations()


    while True:
        action = input("\naction: ").strip()

        if action == 'Print':
            if rep_type == 'matrix':
                rep.printAsMatrix(matrix, n)
            elif rep_type == 'list':
                rep.printAsList(matrix, n)
            else:
                rep.printAsTable(matrix, n)

        elif action == 'find':
            try:
                u = int(input("from> "))
                v = int(input("to> "))
                graph_for_find = adj if rep_type=='list' else matrix
                rep_for_find   = 'list' if rep_type=='list' else 'matrix'
                exists, msg = ops.find_edge(graph_for_find, u, v, rep_for_find)
                print(msg)
            except ValueError:
                print("Niepoprawne dane wejściowe!")

        elif action == 'Breath-first search':
            try:
                start = int(input("Startowy węzeł: "))
                graph_for_bfs = adj if rep_type=='list' else matrix
                rep_for_bfs   = 'list' if rep_type=='list' else 'matrix'
                seq = ops.bfs(graph_for_bfs, start, rep_for_bfs)
                print("BFS:", " ".join(map(str, seq)))
            except ValueError:
                print("Niepoprawny numer węzła!")

        elif action == 'Depth-first search':
            try:
                start = int(input("Startowy węzeł: "))
                graph_for_dfs = adj if rep_type=='list' else matrix
                rep_for_dfs   = 'list' if rep_type=='list' else 'matrix'
                seq = ops.dfs(graph_for_dfs, start, rep_for_dfs)
                print("DFS:", " ".join(map(str, seq)))
            except ValueError:
                print("Niepoprawny numer węzła!")

        elif action.lower() == 'topo-kahn':
            try:
                graph_for_kahn = adj if rep_type=='list' else matrix
                rep_for_kahn   = 'list' if rep_type=='list' else 'matrix'
                topo = ops.topological_sort_kahn(graph_for_kahn, rep_for_kahn)
                print("Topologiczne (Kahna):", " ".join(map(str, topo)))
            except ValueError as e:
                print(e)

        elif action.lower() == 'topo-tarjan':
            try:
                graph_for_tarjan = adj if rep_type=='list' else matrix
                rep_for_tarjan   = 'list' if rep_type=='list' else 'matrix'
                topo = ops.topological_sort_tarjan(graph_for_tarjan,
                                                   rep_for_tarjan)
                print("Topologiczne (Tarjan):", " ".join(map(str, topo)))
            except ValueError as e:
                print(e)

        elif action.lower() == 'exit':
            print("Koniec programu.")
            break

        else:
            print("Dostępne akcje: Print, find, "
                  "Breath-first search, Depth-first search, "
                  "topo-kahn, topo-tarjan, exit")

if __name__ == "__main__":
    main()