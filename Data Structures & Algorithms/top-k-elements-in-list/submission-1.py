class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #Create dictionary
        for num in nums:
            count[num] = 1 + count.get(num, 0) #It checks the current count for each number but returns 0 if it doesnt exist, then adds 1
        #basically it sets the value at position num in the dictionary
        arr = [] # create new list because lists can ba sorted and not dictionaries
        for num, cnt in count.items(): #loop thourgh the count, count.items gires us the pair, loop thorugh it and call the first num and the second cnt
            print(f"Number {num} appeared {cnt} times")# test logic
            arr.append([cnt, num])#add to arr but flip ordr to make cnt first because we want to sort by frequency

        arr.sort()

        res =[] #create empty result list
        while len(res) < k: #because k is frequency, we make sure the length of result is smaller than k 
            res.append(arr.pop()[1])# we pop the pair from arr, istr sorted so it pops and retruns the last one which is the most frequent, but then we sat [1] so it ops the one in the 1 position, which is the number of the pair and append to result
        return res
