class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))#initial value of 1, we want it to be the length of input array, multiply by length of array

        prefix = 1 #initialize as 1
        for i in range(len(nums)): #for each position in our input array
            res[i] = prefix #for each position in our result output array, i we take the prefix and put it in the position i 
            prefix *= nums[i]#after weve done that we take the input array value nums[i] and multiply by whatver the prefix happens to be, and we store the prefix in the results out put array
        postfix = 1
        for i in range(len(nums) -1, -1, -1): #start at the end of the input array and go up till the beginning  
            res[i] *= postfix #we're not simply storing the postfix value beccause that will end up overwriting the prefix we stored in the result, instred we multiply by the value that's already in the prefix result
            postfix *= nums[i] #we have to continually update the post fix, so we multiply by whatver value is in the input array nums
        return res