sudoku = [9, 8, 4, 0, 3, 1, 0, 7, 2,
          6, 1, 0, 0, 0, 7, 0, 0, 0,
          2, 5, 7, 0, 0, 9, 8, 0, 0,

          3, 0, 0, 0, 6, 0, 0, 1, 0,
          0, 0, 0, 3, 7, 0, 9, 2, 0,
          0, 0, 9, 0, 0, 5, 0, 0, 0,

          0, 3, 0, 0, 0, 6, 0, 0, 0,
          0, 4, 5, 0, 1, 8, 0, 9, 6,
          1, 9, 6, 7, 0, 0, 2, 8, 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_rows(sudoku):
    return [sudoku[i:i + 9] for i in range(0, 81, 9)]


def get_row(sudoku, num_row):
    return get_rows(sudoku)[num_row]


def get_columns(sudoku):
    return [[sudoku[i * 9 + j] for i in range(9)] for j in range(9)]


def get_column(sudoku, numb_col):
    return get_columns(sudoku)[numb_col]


def get_blocks(sudoku):
    result = [None for i in range(9)]
    for g in range(3):
        for j in range(3):
            line = []
            for i in range(3):
                line.extend(sudoku[3 * (i * 3 + j + g * 9):3 * (i * 3 + j + g * 9 + 1)])
            result.insert(j + g * 3, line)
    return result


def get_block(sudoku, numb_block):
    return get_blocks(sudoku)[numb_block]


def get_line_from_rows(sudoku):
    result = []
    [[result.append(numbs) for numbs in row] for row in sudoku]
    return result

def get_line_from_columns(sudoku):
    result = []
    for i in range(9):
        for j in range(9):
            result.append(sudoku[j][i])
    return result

def check_last_hero(sudoku):

    for num_row, row in enumerate(sudoku):
        for i, numb in enumerate(row):
            if numb == 0:
                possib_numbs = [n for n in numbers if n not in row]
                row[i] = possib_numbs
            if type(numb)==list:
                possib_numbs = [n for n in numb if n not in row]
                row[i] = possib_numbs
            sudoku[num_row] = row

    return sudoku

if __name__ == '__main__':

    solv_sudoku = sudoku
    print(get_rows(solv_sudoku))
    solv_sudoku = get_line_from_rows(check_last_hero(get_rows(solv_sudoku)))
    print(get_rows(solv_sudoku))
    solv_sudoku = get_line_from_columns(check_last_hero(get_columns(solv_sudoku)))
    print(get_rows(solv_sudoku))


    for i, numb in enumerate(solv_sudoku):
        if type(numb) == list and len(numb) == 1:
            solv_sudoku[i] = numb[0]
    print(get_rows(solv_sudoku))


