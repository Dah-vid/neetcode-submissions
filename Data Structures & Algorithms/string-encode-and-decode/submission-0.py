class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, str) -> List[str]:

        res, i = [], 0

        while i < len(str): #this is so we can go through all the characters
            j = i
            while str[j] != "#":  #check for delimiter
                j+=1
            #extract length
            length = int(str[i:j]) #converts to integer the slice of i to j , j excluded
            res.append(str[j + 1 : j +1 + length])
            i = j + 1 + length
        return res
            