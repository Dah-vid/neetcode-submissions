class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brute force, time limit exceeded, O(n^2)
        #res = 0 #Inintialize our result to 0 because we cant have a negative area in this context
        #go through every single combination
        #for l in range(len(height)): # left pointer go through every single indice of height
            #for r in range(l + 1, len(height)):# always at least one position ahead of left
                #area = (r -l) * min(height[l], height[r])  # for each of this , compute the area of the rectangle, width (r - l) multiplied by height,  we can find the height by using the min height because thats always our bottle neck, water spills out if too small
                #res = max(res, area) # we want the maximum area

        #return res

        #Linear time
        res = 0
        l, r = 0, len(height) - 1 # initialize our left pointer all the way to the left 0, right all the way to the right
        while l < r: # if they're equal or if left passes right, its not good
            area = (r -l) * min(height[l], height[r]) #copied from brute
            res = max(res, area) #copied

            if height[l] < height[r]:
                l += 1 # if height at left is less than height at right,we shift our left pointer to the right , increment. Because we want to maximize both of these heights 
            #elif height[l] < height[r]:     commented out because it does the same as below code and is faster when commented out
                #r -= 1 #if the opposite we would want to shift our right pointer and we would want to decrement it, commented out because it does the same as below code and is fatser when commented out
            else:
                r -= 1 # last case if they were equal, we could increment our left or decrement our right we can do either one, we chose this one and realize this does the same as previous so we condense previous and its fater runtime too
               
        return res


       