class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #create set from the intial array nums
        longest = 0 #keep track ofwhat the lngest consequetive sequence is, initally 0

        #for n in nums: iterate through every number in the nums array, but it exceeds timelimit because of duplicates
        for n in numSet: #iterate through every number in the nums set
            # check if its the start of a sequence
            if (n-1) not in numSet: # we check by this , if it doesnt have a left neighbour its the start of the sequence
                length = 0 #get the length of the sequence, initialize to 0 , we want to keep getting each consecutive number and checking if it exists in our numSet, if it does we keep expanding our length
                while (n + length) in numSet: #check the current number
                    length += 1 #as the length grows we check more consecutive numbers
                longest = max(length, longest) #at the end we could have potentially found the longest, we want to potentially update our longest by taking the max of the currentl lenght we computed, length, along with what the longest originlally was, longest
        return longest #return what the longest sequence was that we just computed