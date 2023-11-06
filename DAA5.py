def n_queens(n):
    col = set()
    posDiag = set()  # (r+c)
    negDiag = set()  # (r-c)

    def count_solutions(board, r):
        if r == n:
            return 1

        total_solutions = 0

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            total_solutions += count_solutions(board, r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

        return total_solutions

    board = [["."]*n for i in range(n)]
    return count_solutions(board, 0)

if __name__ == "__main__":
    num_solutions = n_queens(8)
    print(f"Number of solutions for 8-Queens: {num_solutions}")
