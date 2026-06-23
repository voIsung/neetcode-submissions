class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = []

        for i in range(1, 10):
            numbers.append(str(i))

        for row in board:
            row_count = {}

            for cell in row:
                if cell in numbers:
                    found = cell
                    row_count[found] = row_count.get(found, 0) + 1

                    if row_count[found] >= 2:
                        return False
         
        for col in range(9):
            col_count = {}

            for row in range(9):
                cell = board[row][col]

                if cell in numbers:
                    found = cell
                    col_count[found] = col_count.get(found, 0) + 1

                    if col_count[found] >= 2:
                        return False

        box_count = {}

        for row in range(9):
            for col in range(9):
                cell =  board[row][col]
                box_index = (row // 3) * 3 + (col // 3)                   
                
                if cell in numbers:
                    found = (box_index, cell)
                    box_count[found] = box_count.get(found, 0) + 1
        
                    if box_count[found] >= 2:
                        return False
        
        return True