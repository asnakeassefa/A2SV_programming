class Solution:
    def inbound(self,image,row,col):
        return 0<= row <len(image) and 0<= col<len(image[0])
    
    def DFS(self,image,row,col,visited,ref,color):
        direction = [(0,1),(0,-1),(1,0),(-1,0)]

        if not self.inbound(image,row,col) or (row,col) in visited:
            return
        visited.add((row,col))
        if image[row][col] == ref:
            image[row][col] = color
        for n_row,n_col in direction:
            new_row = row + n_row
            new_col = col + n_col
            if self.inbound(image,new_row,new_col) and image[new_row][new_col] == ref:
                self.DFS(image,new_row,new_col,visited,ref,color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ref = image[sr][sc]
        self.DFS(image,sr,sc,set(),ref,color)
        return image