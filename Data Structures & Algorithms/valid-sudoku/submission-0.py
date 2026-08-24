class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) #using a hash map to detect duplicates where the key is the column number and the value is going to be another set, the set will represent all values in this column
        rows = collections.defaultdict(set) #same thing
        squares = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):  #iterate through the ennitre grid whose dimensions are 9 by 9
            for c in range(9):
                if board[r][c] == ".": #a position can be empty and it is represented with a dot so we skip it and continue to the next iteration of the loop
                    continue
                if (board[r][c] in rows[r] or # have we found the duplicate, if we have we return false immediately, so this value if its not empty it  hasnt already been detected. So if the board is in rows,at the current row were in, rows is our hashap, the key were puting [r]is the current row were in, row[r] represents a hash set of all avalues that occur at this roew number[r], so this current number board[r][c] is already inside the current row[r] meaning weve already seen this value board[r][c] before in the current row were in rows[r] , meaning its a duplicate in which case we can return false but thats not it, next line
                    board[r][c] in cols[c] or # the exact same thing is gonna be true if board[r][c] has already occured in the same column cols[c] before, if this value has already occured in the current column we're in , that means weve detected another duplicate and we can return false
                    board[r][c] in squares[(r // 3, c //3)]): # laslty we check if the value board[r][c] has already occured in the current square we're in, squares[(r // 3, c //3)]) will return a set of all the values we've seen in the current square before and if this value board[r][c]  is a duplicate , that means its already in squares[(r // 3, c //3)]) so we can return false,
                     return False # basically the baove is a our way of validating the current sudoku boad i valid, if we have any duplicates, that means its not valid and we return false, it is valid , we continue and we update all three of our hashmaops above
                cols[c].add(board[r][c]) # add to it the current character we just saw
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True