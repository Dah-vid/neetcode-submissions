class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # return results as list of lists
        nums.sort() # sort input array

        for i, a in enumerate(nums): # use each number in the input array as a possible first value, iterate through the index i and the value a
            if i > 0 and a == nums[i -1]:# dont want to re-use the same value in the same positions twice, if i > 0 menais it isnt the first value in the input array and a == nums[i- 1]means its the same value as before, so we want to continue, we dont want to reuse the same value twice 
                continue # continue to the next iteration of the loop

            l, r = i + 1, len(nums) - 1 # use two pointer for the remaining portion of the array, l will initially be i + 1 , r will be end of the list len(nums)- 1
            while l < r : # left and right cant be equal
                threeSum = a + nums[l] + nums[r] #compute the sum
                if threeSum > 0: #if its too great ie greater than than zero which is what we're looking for then we need to decrease it
                    r -= 1 # so roght pointer needs to be decremeted
                elif threeSum < 0: #if too small , make the sum bigger
                    l += 1 # so shiftleft pointer to the right
                else:
                    res.append([a, nums[l], nums[r]]) # last case, if its equal to zero we add it to our result, so we append all three. numbers
                #update our oiinters
                    l += 1 # only shift our left pointer, we dont ant to have same sum  so we use a loop 
                    while nums[l] == nums [l - 1] and l < r:  # if nums[l] == nums [l - 1]: that means we have the same value, so we have to keep shifting pur pointer, but we dont want our left pointer to ever pass the right pointer so we add that to the condition and l < r
                        l += 1 # this is where we implemeted the "keep shifting pur pointer"
        return res