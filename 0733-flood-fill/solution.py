def replace(image, sr, sc, color, original):
    if image[sr][sc] == original and image[sr][sc] != color:
        image[sr][sc] = color
        m = len(image) - 1
        n = len(image[0]) - 1

        if sc > 0:
            if image[sr][sc - 1] == original: image = replace(image, sr, sc - 1, color, original)
        if sc < n:
            if image[sr][sc + 1] == original: image = replace(image, sr, sc + 1, color, original)
        if sr > 0:
            if image[sr - 1][sc] == original: image = replace(image, sr - 1, sc, color, original)
        if sr < m:
            if image[sr + 1][sc] == original: image = replace(image, sr + 1, sc, color, original)

    return image

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return replace(image, sr, sc, color, image[sr][sc])
