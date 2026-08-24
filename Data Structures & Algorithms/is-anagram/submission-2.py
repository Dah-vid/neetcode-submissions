class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {} #Create hash map for S 
        t_count = {} #Create hash map for t 


        for char in s: #loop through and increment if it exists
            s_count[char] = s_count.get(char, 0) + 1

        for char in t: 
            t_count[char] = t_count.get(char, 0) + 1

        return s_count == t_count
        