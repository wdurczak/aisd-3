class Representation:
    def selectRepresentation(self):
        while True:
            try:
                repType = str(input("type: "))
                if (repType!='matrix' and repType!='list' and repType!='table'):
                    print("takiego typu nie obsługujemy")
                    continue
                return repType
            except ValueError:
                print("Niepoprawny typ danych")

    def printAsMatrix(self, graph, nodes):
        print("\nMacierz sąsiedztwa:")
        print("     " + " ".join(f"{i:>3}" for i in range(nodes)))
        print("    " + "-" * (4 * nodes))
        

        for row_idx, row in enumerate(graph):
            formatted = []
            for val in row:
                if val >= 0:
                    formatted.append(f" {val:2}")
                else:
                    formatted.append(f"{val:3}")
            print(f"{row_idx:2} |", " ".join(formatted))

    def printAsList(self, graph, nodes):
        print("\nLista następników:")
        for i in range(nodes):
            successors = [str(j) for j in range(nodes) if graph[i][j] == 1]
            print(f"{i} ->", " ".join(successors))

    def printAsTable(self, graph, nodes):
        print("\nTabela połączeń:")
        print("Wierzchołek | Następniki")
        print("-" * 25)
        for i in range(nodes):
            successors = [str(j) for j in range(nodes) if graph[i][j] == 1]
            print(f"{i:^11}|", " ".join(successors) if successors else "brak") 