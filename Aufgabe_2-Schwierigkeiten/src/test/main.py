from collections import defaultdict, deque
import sys

def read_input(file_path):
    # Lese die Eingabedatei und extrahiere die Vergleiche und Aufgaben
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    n, m, k = map(int, lines[0].split())
    comparisons = [line.strip().split(' < ') for line in lines[1:n + 1]]
    tasks = lines[n + 1].strip().split()  # Lese alle Aufgaben
    
    return comparisons, tasks, k

def build_graph(comparisons):
    # Erstelle den Graphen und berechne die Eingangsgrade
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for comparison in comparisons:
        for i in range(len(comparison) - 1):
            graph[comparison[i]].append(comparison[i + 1])
            in_degree[comparison[i + 1]] += 1
            if comparison[i] not in in_degree:
                in_degree[comparison[i]] = 0
    
    return graph, in_degree

def topological_sort(graph, in_degree, tasks):
    # Führe eine topologische Sortierung durch
    queue = deque([task for task in tasks if in_degree[task] == 0])
    sorted_tasks = []
    
    while queue:
        task = queue.popleft()
        sorted_tasks.append(task)
        
        for neighbor in graph[task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_tasks

def main():
    # Hauptfunktion, die die Eingabe liest, den Graphen erstellt und die Aufgaben sortiert
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        return
    
    input_file = sys.argv[1]
    comparisons, tasks, k = read_input(input_file)
    graph, in_degree = build_graph(comparisons)
    sorted_tasks = topological_sort(graph, in_degree, tasks)
    
    print("Gute Anordnung der Aufgaben:", "; ".join(sorted_tasks[:k]))  # Berücksichtige nur die ersten k Aufgaben

if __name__ == "__main__":
    main()
