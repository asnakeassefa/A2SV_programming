class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for row in image:
            row.reverse()
            for i,val in enumerate(row):
                row[i] = 0 if val == 1 else 1
        return image