
class userProvidedGenerating:
    def userProvidedData(self):
        while True:
            try:
                nodes = int(input("nodes: "))
                if nodes <= 0:
                    print("Podaj liczbę > 0")
                    continue
                break
            except ValueError:
                print("Wprowadź liczbę całkowitą!")

        matrix = [[0]*nodes for _ in range(nodes)]
        
        for i in range(nodes):
            while True:
                try:
                    successors = list(map(int, input(f"Podaj następniki wierzchołka {i}: ").split()))
                    invalid = [s for s in successors if s < 0 or s >= nodes or s == i]
                    
                    if invalid:
                        print(f"Niepoprawne wierzchołki: {', '.join(map(str, invalid))}")
                        continue
                        
                    for j in successors:
                        matrix[i][j] = 1
                        matrix[j][i] = -1
                    break
                except ValueError:
                    print("Wprowadź tylko liczby oddzielone spacjami")
        
        return matrix