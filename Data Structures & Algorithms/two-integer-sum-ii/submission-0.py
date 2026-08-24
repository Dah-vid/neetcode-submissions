class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # left pointer l will be at the beginning so index 0, the right r will be at the last. iondex so len(numbers - 1)
        while l < r: #we need a loop to iterate through our array, this conditon l < r doesnt matter because we ae guaranteed a solution no matter what
            curSum = numbers[l] + numbers[r] #compute current sum

            if curSum > target: #if its too big
                r -= 1 # we take our right pointer and shift to the left
            elif curSum < target: # if its too small   
                l += 1 # we increase our sum by taking the left pointer and shifitng it to the right
            else:  # if our current sum is currently equal to the target, we wanna return our indices left and right
                return [l + 1 , r + 1] #its based on 1 so we add one to each of them
        return[] # we can put a return here but its not needed because we are guranteed a solution so our loop will return the solution


        