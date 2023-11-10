import tkinter as tk

# Hàm kiểm tra tính hợp lệ của bảng Sudoku
def is_valid(row, col, num):
    # Kiểm tra hàng và cột
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Kiểm tra ô 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Hàm kiểm tra nhập liệu cho các ô trống
def check_entry(event, entry, selected_row, selected_col):
    # Lấy giá trị nhập vào ô
    value = entry.get()

    # Đảm bảo giá trị nhập vào là số từ 1 đến 9 hoặc để trống
    if value.isdigit() and 1 <= int(value) <= 9:
        # Cập nhật giá trị của ô trong bảng Sudoku
        board[selected_row][selected_col] = int(value)
    elif value == "":
        # Nếu người dùng để trống ô nhập liệu, thì cập nhật giá trị trong bảng Sudoku thành 0
        board[selected_row][selected_col] = 0
    else:
        # Nếu người dùng nhập giá trị không hợp lệ, thì xóa giá trị và hiển thị ô trống
        entry.delete(0, "end")
        board[selected_row][selected_col] = 0
    # Gọi lại hàm hiển thị bảng để cập nhật giao diện
    display_board()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Sudoku Game")

# Biến board là biến toàn cục
with open("sudoku_03.txt", "r") as file:
    # Đọc từng dòng trong tệp và chuyển đổi nó thành danh sách các số nguyên
    rows = file.readlines()
    board = [[int(num) for num in row.split()] for row in rows]

entries = [[None for _ in range(9)] for _ in range(9)]

# Kích thước ô nhập liệu
entry_width = 3
entry_height = 1

# Hàm để cập nhật ô được chọn
def select_entry(event):
    global selected_entry
    selected_entry = event.widget

# Hàm hiển thị bảng Sudoku và cho phép nhập giá trị vào ô
def display_board():
    canvas.delete("all")  # Xóa nội dung cũ trên Canvas
    for i in range(10):
        line_width = 2 if i % 3 == 0 else 1
        x0, y0, x1, y1 = i * cell_size, 0, i * cell_size, 9 * cell_size
        canvas.create_line(x0, y0, x1, y1, width=line_width)
        x0, y0, x1, y1 = 0, i * cell_size, 9 * cell_size, i * cell_size
        canvas.create_line(x0, y0, x1, y1, width=line_width)

    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            x = j * cell_size + cell_size / 2
            y = i * cell_size + cell_size / 2
            if cell != 0:
                canvas.create_text(x, y, text=str(cell), font=('Helvetica', 16))
            else:
                if entries[i][j] is None:
                    # Tạo một khung bao quanh ô nhập liệu cho các ô trống
                    frame = tk.Frame(root, width=cell_size, height=cell_size)
                    frame.grid(row=i, column=j)
                    entry = tk.Entry(frame, width=entry_width, font=('Helvetica', 16), bd=0, justify='center')
                    entry.grid(row=0, column=0, sticky="nsew")  # Canh giữa nội dung
                    entry.bind("<Button-1>", select_entry)
                    entry.bind("<Key>", lambda event, selected_row=i, selected_col=j: check_entry(event, entry, selected_row, selected_col))  # Kiểm tra nhập liệu
                    entries[i][j] = entry

# Tạo Canvas để vẽ đường kẻ và ô số
cell_size = 60
canvas = tk.Canvas(root, width=cell_size * 9, height=cell_size * 9, bg='white')
canvas.grid(row=0, column=0, rowspan=9, columnspan=9)
display_board()

button_frame = tk.Frame(root)
button_frame.grid(row=9, column=0, columnspan=9)
button_font = ('Helvetica', 18)
def set_number(num):
    if selected_entry is not None:
        selected_entry.delete(0, "end")
        selected_entry.insert(0, str(num))
        display_board()
# Tạo 9 nút riêng lẻ từ 1 đến 9 và gắn dữ liệu là các số từ 1 đến 9
for i in range(1, 10):
    button = tk.Button(root, text=str(i), command=lambda num=i: set_number(num))
    button.grid(row=10, column=i - 1)
    button.config(font=button_font, borderwidth=0)

# Biến lưu trữ ô nhập liệu được chọn
selected_entry = None

# Mở cửa sổ
root.mainloop()
