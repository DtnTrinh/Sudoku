# Đọc bảng Sudoku từ tệp
def read_sudoku_from_file(file_path):
    with open(file_path, "r") as file:
        sudoku_board = [[int(num) for num in line.split()] for line in file]
    return sudoku_board

# Hàm kiểm tra tính hợp lệ của bảng Sudoku
def is_valid(board, row, col, num):
    # Kiểm tra hàng
    if num in board[row]:
        return False

    # Kiểm tra cột
    if num in [board[i][col] for i in range(9)]:
        return False

    # Kiểm tra ô 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Hàm giải Sudoku
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# In bảng Sudoku
def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Đọc bảng Sudoku từ tệp sudoku_01.txt
    input_file = "sudoku_12.txt" #,,,,,12
    sudoku_board = read_sudoku_from_file(input_file)

    # Giải Sudoku
    if solve_sudoku(sudoku_board):
        print("\nBảng Sudoku đã giải:")
        print_sudoku(sudoku_board)
    else:
        print("\nKhông có giải pháp cho Sudoku này.")
