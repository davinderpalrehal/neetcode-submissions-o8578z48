class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()

        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph:
            return False
        if dst not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        
        self.graph[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        q = deque()
        q.append(src)
        visited = set()

        while q:
            curr = q.popleft()

            if dst in self.graph[curr]:
                return True
            if curr in visited:
                continue
            visited.add(curr)

            for n in list(self.graph[curr]):
                if n not in visited:
                    q.append(n)
        
        return False