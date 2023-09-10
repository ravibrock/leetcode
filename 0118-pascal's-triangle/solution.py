class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for n in range(1, numRows):
            length = len(triangle[n - 1])
            temp = [1] * (length + 1)
            temp[0], temp[length] = 1, 1 
            for i in range(1, length): temp[i] = triangle[n - 1][i - 1] + triangle[n - 1][i]
            triangle.append(temp)
        return triangle
