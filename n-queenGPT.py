def is_safe(position, row, col):
    for r in range(row):
        c = position[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n):
    position = [-1] * n  # position[i] = column index of queen in row i

    def backtrack(row):
        if row == n:
            return True  # Found one solution
        for col in range(n):
            if is_safe(position, row, col):
                position[row] = col
                if backtrack(row + 1):
                    return True
        return False

    backtrack(0)
    return position

def print_board(position):
    n = len(position)
    for row in range(n):
        line = ""
        for col in range(n):
            if position[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)

n = int(input("Enter the value of N: "))
solution = solve_n_queens(n)

print("\nQueen positions: ",solution)

print("\nBoard visualization:")
print_board(solution)
