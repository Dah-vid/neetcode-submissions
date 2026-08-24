class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums): #iterate through every value 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]#we found the solution, return first index [diff] and second one [i]
            prevMap[n] = i #we didnt find the solution we update our hashmap
        return # dont need to return because we are guaranteed solution is there but regardless we do
