class Solution(object):
    def dfs(self, image,sr,sc, currentColor, newColor):
        nr = len(image)
        nc = len(image[0])
        if sr<0 or sc<0 or sr>=nr or sc>=nc or image[sr][sc]!=currentColor:
            return
        image[sr][sc] = newColor
        self.dfs(image,sr-1,sc,currentColor,newColor)
        self.dfs(image,sr+1,sc,currentColor,newColor)
        self.dfs(image,sr,sc-1,currentColor,newColor)
        self.dfs(image,sr,sc+1,currentColor, newColor)
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        currentColor = image[sr][sc]
        if currentColor == newColor:
            return image
        self.dfs(image, sr,sc, currentColor, newColor )
        return image
        