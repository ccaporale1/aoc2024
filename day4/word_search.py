'''
Referencing:
https://dev.to/mauricioabreu/solving-word-search-problem-2n6h


'''
class WordSearch:
    def __init__(self,grid,words=[""]):
        self.grid = grid
        self.words = words
        self.word = words[0]
        self.finds = [] #((r,c),(r,c)) pairs

    def search(self,word):
        # find
        self.word = word

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == self.word[0]:  # Only start DFS if the first character matches
                    found,end = self.__dfs(r, c, 0)
                    if found:
                        return True
                    
        return False
    
    def __dfs(self, r, c, index, direction=None):
        # Define possible directions
        directions = {
            "down": (1, 0),
            "up": (-1, 0),
            "right": (0, 1),
            "left": (0, -1),
            "down-right": (1, 1),
            "down-left": (1, -1),
            "up-right": (-1, 1),
            "up-left": (-1, -1)
        }

        # Boundary and character match check
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]) or self.grid[r][c] != self.word[index]:
            return []

        # Base case: if the last character is matched
        if index == len(self.word) - 1:
            return [(r, c)]

        # Temporarily mark the cell as visited
        temp = self.grid[r][c]
        self.grid[r][c] = "#"

        matches = []

        # If no direction yet, explore all directions
        if direction is None:
            for dir_name, (dr, dc) in directions.items():
                matches.extend(self.__dfs(r + dr, c + dc, index + 1, dir_name))
        else:
            # Continue only in the specified direction
            dr, dc = directions[direction]
            matches.extend(self.__dfs(r + dr, c + dc, index + 1, direction))

        # Restore the cell after exploration
        self.grid[r][c] = temp
        return matches





    
    def find_all(self, word):
        self.finds = []  # Reset finds
        self.word = word
        seen_paths = set()  # Use a set to store unique paths

        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == self.word[0]:  # Start DFS if the first character matches
                    ends = self.__dfs(r, c, 0)
                    if len(ends) > 0:
                        for end in ends:
                            location = ((r, c), end)
                            reverse_location = (end, (r, c))  # Reverse path
                            if location not in seen_paths and reverse_location not in seen_paths:
                                seen_paths.add(location)
                                self.finds.append(location)

        return len(self.finds)