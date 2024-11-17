from collections import defaultdict, deque

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    num_tasks = int(lines[0].split()[0])
    comparisons = [line.strip().split(' < ') for line in lines[1:num_tasks]]
    tasks = lines[num_tasks].strip().split()
    
    return comparisons, tasks

def build_graph(comparisons):
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
    comparisons, tasks = read_input('/home/frederik/dev/bwinf-2024/Aufgabe_2-Schwierigkeiten/src/schwierigkeiten0.txt')
    graph, in_degree = build_graph(comparisons)
    sorted_tasks = topological_sort(graph, in_degree, tasks)
    
    print("Gute Anordnung der Aufgaben:", "; ".join(sorted_tasks))

if __name__ == "__main__":
    main()

