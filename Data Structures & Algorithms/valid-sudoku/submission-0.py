class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def get_row(k):
            return board[k]

        def get_col(k):
            return [board[i][k] for i in range(9)]

        def get_blk(k):
            cs = (k % 3) * 3
            rs = (k // 3) * 3
            ret = []
            for i in range(rs, rs+3):
                for j in range(cs, cs+3):
                    ret.append(board[i][j])
            return ret

        def is_valid(blk):
            blk = [e for e in blk if e != '.']
            return len(set(blk)) == len(blk)

        for k in range(9):
            if not is_valid(get_row(k)) or not is_valid(get_col(k)) or not is_valid(get_blk(k)):
                return False

        return True