simple = '0 0 0 0 0 0 6 0 9 ' \
         '1 0 0 0 0 4 0 0 0 ' \
         '0 0 5 3 0 6 8 2 1 ' \
         '0 0 4 6 7 0 0 5 0 ' \
         '0 0 7 0 0 0 9 0 0 ' \
         '0 0 0 5 4 0 0 0 0 ' \
         '3 7 0 4 0 5 2 0 6 ' \
         '0 0 0 0 0 0 5 1 0 ' \
         '0 6 0 0 2 0 0 3 7'

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
            row = []
            for i in range(3):
                row.extend(sudoku[3 * (i * 3 + j + g * 9):3 * (i * 3 + j + g * 9 + 1)])
            result[j + g * 3] = row
    return result


def get_block(sudoku, numb_block):
    return get_blocks(sudoku)[numb_block]


def get_line_from_rows(sudoku):
    result = []
    [result.extend(row) for row in sudoku]
    return result


def get_line_from_columns(sudoku):
    result = []
    [[result.append(sudoku[j][i]) for j in range(9)] for i in range(9)]
    return result


def get_line_from_blocks(sudoku):
    sudoku = get_blocks(get_line_from_rows(sudoku))

    return get_line_from_rows(sudoku)


def check_last_hero(sudoku):
    for num_row, row in enumerate(sudoku):

        for i, numb in enumerate(row):
            if numb == 0:
                possib_numbs = [n for n in numbers if n not in row]
                row[i] = possib_numbs
            if type(numb) == list:
                possib_numbs = [n for n in numb if n not in row]
                row[i] = possib_numbs
        row = check_last_in_cells(row)
        sudoku[num_row] = row

    return sudoku


def check_solve(sudoku):

    rows_sudoku = get_rows(sudoku)
    columns_sudoku = get_columns(sudoku)
    blocks_sudoku = get_blocks(sudoku)
    for num in sudoku:
        if type(num) == list or num == 0:
            return(False)
        for row in rows_sudoku:
            if row.count(num)!=1:
                return(False)
        for col in columns_sudoku:
            if col.count(num)!=1:
                return(False)
        for block in blocks_sudoku:
            if block.count(num)!=1:
                return(False)

    return(True)


def check_last_in_cells(row):
    in_cells = {}
    for cell in row:
        if type(cell) == list:
            for numb in cell:
                in_cells.update({numb: in_cells.get(numb, 0) + 1})

    for key in in_cells.keys():
        if in_cells[key] == 1:
            for position_cell, cell in enumerate(row):
                if type(cell) == list and key in cell:
                    row[position_cell] = key
                    break
    return row

if __name__ == '__main__':

    solv_sudoku = simple.split(' ')
    solv_sudoku = [int(num) for num in solv_sudoku]
    for row in get_rows(solv_sudoku):
        print(row)
    print()

    count_iterations = 0
    #while count_iterations!=10:
    while check_solve(solv_sudoku) != True:
        solv_sudoku = get_line_from_rows(check_last_hero(get_rows(solv_sudoku)))
        solv_sudoku = get_line_from_columns(check_last_hero(get_columns(solv_sudoku)))
        solv_sudoku = get_line_from_blocks(check_last_hero(get_blocks(solv_sudoku)))

        for i, numb in enumerate(solv_sudoku):
            if type(numb) == list and len(numb) == 1:
                solv_sudoku[i] = numb[0]


        print()
        for row in get_rows(solv_sudoku):
            print(row)


        count_iterations += 1
        print(count_iterations)






