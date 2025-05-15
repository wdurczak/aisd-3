import random

class GenerateAll:
    def generateData(self):
        while True:
            try:
                nodes = int(input("nodes: "))
                if nodes <= 0:
                    print("Niepoprawna ilość wierzchołków (Podaj liczbę większą od 0)")
                    continue
                break
            except ValueError:
                print("Sprawdź poprawność danych! (Oczekiwana liczba całkowita)")

        while True:    
            try:
                saturation = int(input("saturation (0-100): "))
                if saturation < 0 or saturation > 100:
                    print("Niepoprawna wartość - nasycenie musi być między 0 a 100")
                    continue
                break
            except ValueError:
                print("Sprawdź poprawność danych! (Oczekiwana liczba całkowita)")

        return nodes, saturation

    def generateGraph(self, nodes, saturation):
        max_edges = nodes * (nodes - 1)
        target_edges = (max_edges * saturation) // 100

        matrix = [[0] * nodes for _ in range(nodes)]
        possible_edges = [(i, j) for i in range(nodes) for j in range(nodes) if i != j]
        selected_edges = random.sample(possible_edges, target_edges)

        for i, j in selected_edges:
            matrix[i][j] = 1   
            matrix[j][i] = -1  

        return matrix

    def printGraphMatrix(self, matrix):
        print("\nMacierz incydencji:")
        print("   " + " ".join(f"{i:3}" for i in range(len(matrix))))
        print("-" * (4 * len(matrix) + 3))
        
        for row_idx, row in enumerate(matrix):
            print(f"{row_idx:2}|", " ".join(f"{val:3}" for val in row))