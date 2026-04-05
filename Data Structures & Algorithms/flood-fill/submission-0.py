class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        start_color = image[sr][sc]
        q = deque()
        q.append((sr, sc))
        visited = set()

        while q:
            cr, cc = q.popleft()
            if (cr, cc) in visited:
                continue
            visited.add((cr, cc))
            image[cr][cc] = color

            if cr + 1 < ROWS and image[cr + 1][cc] == start_color:
                q.append((cr + 1, cc))
            if cr - 1 > -1 and image[cr - 1][cc] == start_color:
                q.append((cr - 1, cc))
            if cc + 1 < COLS and image[cr][cc + 1] == start_color:
                q.append((cr, cc + 1))
            if cc - 1 > -1 and image[cr][cc - 1] == start_color:
                q.append((cr, cc - 1))
        
        return image