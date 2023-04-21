import numpy as np

# Define a função que verifica se um número pode ser inserido em uma posição específica
def is_valid(grid, row, col, num):
    # Verifica se o número já existe na linha
    if num in grid[row]:
        return False
    # Verifica se o número já existe na coluna
    if num in grid[:, col]:
        return False
    # Verifica se o número já existe na subgrade 3x3
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    if num in grid[subgrid_row:subgrid_row+3, subgrid_col:subgrid_col+3]:
        return False
    # Se passar por todas as verificações, é válido
    return True

# Define a função que resolve o Sudoku usando backtracking
def solve_sudoku(grid, row=0, col=0):
    # Encontra a próxima posição vazia
    while grid[row, col] != 0:
        col += 1
        if col == 9:
            row += 1
            col = 0
            if row == 9:
                # Se todas as posições estiverem preenchidas, retorna True
                return True
    # Tenta inserir um número em uma posição vazia
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row, col] = num
            if solve_sudoku(grid, row, col):
                return True
            grid[row, col] = 0
    # Se não houver mais números para tentar, retorna False
    return False

# Define a função que gera um Sudoku aleatório
def generate_sudoku():
    grid = np.zeros((9, 9), dtype=int)
    solve_sudoku(grid)
    # Remove alguns números aleatórios para criar um quebra-cabeça
    for _ in range(40):
        row, col = np.random.randint(9, size=2)
        while grid[row, col] == 0:
            row, col = np.random.randint(9, size=2)
        grid[row, col] = 0
    return grid

# Define a função que exibe o Sudoku
def print_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i, j] == 0:
                print(".", end=" ")
            else:
                print(grid[i, j], end=" ")
            if j % 3 == 2 and j < 8:
                print("|", end=" ")
        print()
        if i % 3 == 2 and i < 8:
            print("-" * 21)

# Gera um Sudoku aleatório
grid = generate_sudoku()

# Exibe o Sudoku
print_sudoku(grid)

# Solicita ao usuário que preencha o Sudoku
while not solve_sudoku(grid):
    print("Ops, algo deu errado! Verifique suas respostas e tente novamente.")
    print_sudoku(grid)

# Exibe o Sudoku resolvido
print("Parabéns! Você resolveu")
