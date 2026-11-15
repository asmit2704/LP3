def solve_n_queens(n):
    board = [[0] * n for i in range(n)]

    def solve(row, cols, diag1, diag2):

        if row == n:
            return True

        for col in range(n):

            if col not in cols and row-col not in diag1 and row+col not in diag2:

                board[row][col] = 1

                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)

                if solve(row+1, cols, diag1, diag2):
                    return True

                # Backtracking
                board[row][col] = 0

                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)

        return False

    if solve(0, set(), set(), set()):
        return board

    return None


n = int(input("Enter number of queens: "))

if n <= 0:
    print("Enter a positive number")

else:
    result = solve_n_queens(n)

    if result == None:
        print("No solution exists")

    else:
        print("N-Queens Matrix:")
        for row in result:
            print(row)