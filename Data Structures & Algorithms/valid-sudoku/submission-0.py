class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counter = {str(i): 0 for i in range(1, 10)}

        for row in range(9):
            for col in range(9):
                elem = board[row][col]
                if elem != '.':
                    counter[elem] += 1
                    if counter[elem] == 2:
                        return False
            
            counter = {str(i): 0 for i in range(1, 10)}

        for col in range(9):
            for row in range(9):
                elem = board[row][col]
                if elem != '.':
                    counter[elem] += 1
                    if counter[elem] == 2:
                        return False
            
            counter = {str(i): 0 for i in range(1, 10)}

        
        for square in range(9):
            for row in range((square // 3) * 3, (square // 3) * 3 + 3):
                for col in range((square % 3) * 3, (square % 3) * 3 + 3):
                    elem = board[row][col]
                    if elem != '.':
                        counter[elem] += 1
                        if counter[elem] == 2:
                            return False
            counter = {str(i): 0 for i in range(1, 10)}

        return True

