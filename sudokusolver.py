import copy

VERBOSE = False


def solve_basic(puzzle: str) -> list:
    """
    Solves the sudoku grid using basic rules by finding missing numbers from grid,row and column with numbers 0-9 (0
    being empty).

    :param puzzle: String of the grid to solve (0-9 where 0's are empty squares)
    :return: The solved grid
    """
    current_puzzle = convert_sudoku_string_to_grid(puzzle)
    if VERBOSE:
        print(f'Starting solve: {puzzle}')
    print_sudoku(current_puzzle)

    unsolved_count = 1
    while unsolved_count != 0:
        unsolved_count = 0
        check_progress_puzzle = copy.deepcopy(current_puzzle)
        # Find missing value options for all squares unfilled
        for i in range(0, 9):
            for j in range(0, 9):
                if current_puzzle[j][i][0] == 0:
                    miss_options = get_square_options_missing_numbers((j, i), current_puzzle)
                    current_puzzle[j][i][1] = miss_options
                    if VERBOSE:
                        print(f'Missing options ({j}, {i}): {miss_options}')
                    if len(miss_options) == 1:
                        current_puzzle[j][i][0] = miss_options[0]
                        if VERBOSE:
                            print(f'Missing found ({j}, {i}): {miss_options[0]}')
                    else:
                        unsolved_count += 1
        # Find single options
        for i in range(0, 9):
            for j in range(0, 9):
                if current_puzzle[j][i][0] == 0:
                    scan_options = get_square_options_scan_singles((j, i), current_puzzle)
                    if VERBOSE:
                        print(f'Singles scan ({j}, {i}): {scan_options}')
                    if len(scan_options) == 1:
                        current_puzzle[j][i][0] = scan_options[0]
                        if VERBOSE:
                            print(f'Singles found ({j}, {i}): {scan_options[0]}')
        # Find naked pairs
        for i in range(0, 9):
            for j in range(0, 9):
                if current_puzzle[j][i][0] == 0:
                    pairs_options = get_square_options_pairs((j, i), current_puzzle)
                    if VERBOSE:
                        print(f'Pairs search ({j},{i}): {pairs_options}')
                    if pairs_options:
                        current_puzzle[j][i][1] = pairs_options
                        if VERBOSE:
                            print(f'Pairs found ({j},{i}): {pairs_options}')
                        print(f'Pairs found ({j},{i}): {pairs_options}')
                        print_sudoku(current_puzzle)
        if check_progress_puzzle == current_puzzle:
            break

    if VERBOSE:
        print(f'Unresolved squares: {unsolved_count}')
    return current_puzzle


def find_x_pattern():
    # find pairs looking, and then check if they have another pair in a rectangle/square
    return []


def find_pairs_looking():
    # check if this square sees a naked pair
    # remove them from this options
    return []


def get_square_options_pairs(square: tuple, grid: list) -> list:
    """
    Searches the squares row,col and box to see if it forms a naked pair

    :param square: A tuple (row, column) coordinate of the square
    :param grid: The sudoku grid as a 3D list
    :return: A list of squares that are a naked pair
    """
    options = find_group_pairs(square, get_box(square), grid)
    if len(options) == 2:
        return options
    options = find_group_pairs(square, get_box(square), grid)
    if len(options) == 2:
        return options
    options = find_group_pairs(square, get_box(square), grid)
    if len(options) == 2:
        return options
    return []


# TODO improve to do more than just naked pairs
# TODO simplify this function
def find_group_pairs(square: tuple, squares: list, grid: list) -> list:
    """
    Finds if there are any values in this square's options that is only shared with one other square in the group

    :param square: A tuple (row, column) coordinate of the square
    :param squares: A list of squares (tuples) to check for options overlap
    :param grid: The sudoku grid as a 3D list
    :return: A list of squares that are a naked pair
    """
    if grid[square[0]][square[1]][0] != 0 or len(grid[square[0]][square[1]][1]) < 3:
        return []
    squares.remove(square)

    squares_options = grid[square[0]][square[1]][1]
    squares_placed = []
    for sq in squares:
        if grid[sq[0]][sq[1]][0] == 0:
            squares_options = squares_options + grid[sq[0]][sq[1]][1]
        else:
            squares_placed.append(grid[sq[0]][sq[1]][0])
    option_counts = {x: squares_options.count(x) for x in squares_options}
    pair_value = []
    return_value = []
    for option in grid[square[0]][square[1]][1]:
        if option in option_counts and option_counts[option] == 2:
            if option not in squares_placed:
                pair_value.append(option)
    if len(pair_value) == 2:
        for sq in squares:
            print(f'{pair_value}: {grid[sq[0]][sq[1]][0]} {grid[sq[0]][sq[1]][1]}')
            if pair_value[0] == grid[sq[0]][sq[1]][0] or pair_value[1] == grid[sq[0]][sq[1]][0]:
                # Already placed value
                return []
            if pair_value[0] in grid[sq[0]][sq[1]][1] and pair_value[1] in grid[sq[0]][sq[1]][1]:
                # found both values in a single other square in the grid
                return_value = pair_value
    return return_value


def get_square_options_scan_singles(square: tuple, grid: list) -> list:
    """
    Finds options for this square from missing options in other squares of row, box, column.

    :param square: A tuple (row, column) coordinate of the square
    :param grid: The sudoku grid as a 3D list
    :return: A list of possible values
    """
    box_options = find_group_single_candidate(square, get_box(square), grid)
    if len(box_options) == 1:
        return box_options
    row_options = find_group_single_candidate(square, get_row(square), grid)
    if len(row_options) == 1:
        return row_options
    col_options = find_group_single_candidate(square, get_col(square), grid)
    if len(col_options) == 1:
        return col_options
    return []


def find_group_single_candidate(square: tuple, squares: list, grid: list) -> list:
    """
    Checks for a single option a square can have based on no other square in a group having it as an option

    :param square: A tuple (row, column) coordinate of the square
    :param squares: A list of squares (tuples) to check the options of
    :param grid: The sudoku grid as a 3D list
    :return: A list of options
    """
    if square in squares:
        squares.remove(square)
    square_options = set(grid[square[0]][square[1]][1])
    for sq in squares:
        if grid[sq[0]][sq[1]][0] == 0:
            square_options = square_options - set(grid[sq[0]][sq[1]][1])
        else:
            square_options = square_options - {grid[sq[0]][sq[1]][0]}
    return list(square_options)


def get_square_options_missing_numbers(square: tuple, grid: list) -> list:
    """
    Finds options for this square from missing numbers in row, box, column.

    :param square: A tuple (row, column) coordinate of the square
    :param grid: The sudoku grid as a 3D list
    :return: A list of possible values
    """
    box_options = find_group_missing_numbers(get_box(square), grid)
    row_options = find_group_missing_numbers(get_row(square), grid)
    col_options = find_group_missing_numbers(get_col(square), grid)
    return three_list_intersection(box_options, row_options, col_options)


def find_group_missing_numbers(squares: list, grid: list) -> list:
    """
    Gets the missing numbers from the group of squares

    :param squares: A list of tuples (row, column) coordinates of squares
    :param grid: The sudoku grid as a 3D list
    :return: A list containing all the numbers (1-9) missing from the box
    """
    missing_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for square in squares:
        if grid[square[0]][square[1]][0] != 0:
            missing_nums.remove(grid[square[0]][square[1]][0])
    return missing_nums


def get_row(square: tuple) -> list:
    """
    Gets all the squares in the row, this square is in.

    :param square: A tuple (row, column) coordinate of the square
    :return: A list containing all the tuples of squares in the row
    """
    row_squares = []
    for i in range(0, 9):
        row_squares.append((square[0], i))
    return row_squares


def get_col(square: tuple) -> list:
    """
    Gets all the squares in the column, this square is in.

    :param square: A tuple (row, column) coordinate of the square
    :return: A list containing all the tuples of squares in the column
    """
    col_squares = []
    for j in range(0, 9):
        col_squares.append((j, square[1]))
    return col_squares


def get_box(square: tuple) -> list:
    """
    Gets all the squares in the box, this square is in.

    :param square: A tuple (row, column) coordinate of the square
    :return: A list containing all the tuples of squares in the box
    """
    # TODO check valid coordinates
    box_squares = []
    # Mod3 Box
    # 00 10 20
    # 01 11 21
    # 02 12 22
    box = (square[0] // 3, square[1] // 3)
    for j in range(0, 3):
        for i in range(0, 3):
            y = box[0] * 3 + j
            x = box[1] * 3 + i
            box_squares.append((y, x))
    return box_squares


def three_list_intersection(first_list: list, second_list: list, third_list: list) -> list:
    """
    Finds the intersection between three lists

    :param first_list: A list of values
    :param second_list: A list of values
    :param third_list: A list of values
    :return: A list containing the intersection of the three lists
    """
    options = list(set(first_list).intersection(second_list))
    return list(set(options).intersection(third_list))


def convert_sudoku_string_to_grid(sudoku_layout: str) -> list:
    """
    Converts a string of 81 numbers into a 3d list sudoku grid

    :param sudoku_layout: A string containing all the square values (0-9, 0 for blank) from top left to bottom right
    :return: A 3D list sudoku grid, [] if input fails
    """
    grid = []
    if len(sudoku_layout) == 81 and sudoku_layout.isnumeric():
        for row in range(0, 9):
            grid.append([])
            for column in range(0, 9):
                grid[row].append([int(sudoku_layout[column + row * 9]), []])
    return grid


def convert_sudoku_grid_to_string(sudoku_grid: list) -> str:
    """
    Converts a sudoku 3d list grid to a string

    :param sudoku_grid: A 3D list sudoku grid
    :return: A string representation of a sudoku from top left to bottom right (0-9 0 for blank)
    """
    values = []
    try:
        for row in range(0, 9):
            for column in range(0, 9):
                values.append(str(sudoku_grid[row][column][0]))
        return ''.join(values)
    except IndexError:
        return ''


def print_sudoku(grid: list) -> None:
    """
    Prints the current sudoku grid

    :param grid: The current sudoku grid
    :return: None
    """
    border = ' +-----+-----+-----+'
    for row_num, row in enumerate(grid):
        if row_num % 3 == 0:
            print(border)
        for col_num, square in enumerate(row):
            if col_num % 3 == 0:
                print(' | ', end='')
            if square[0] == 0:
                print('_', end='')
            else:
                print(square[0], end='')
        print(' |')
    print(f'{border}')


if __name__ == '__main__':
    # Used in Test
    # Easy, hard2
    easy_puzzle = '530070000600195000098000060800060003400803001700020006060000280000419005000080079'
    med_puzzle = '003000100050000060400503009009030200000106000508429301300704005040000010001000900'
    med_puzzle2 = '400809100007000090950020007100090003392407800600030009720080060010000200003102004'
    med_puzzle3 = '960010030302000804070000096000308000609000085000409000020584060508000207040090350'
    hard_puzzle = '000104000001000900090703060807000106000000000304000509050402030008000600000806000'
    # hard_puzzle2 = '005004000000060090300000007000040000008000400541000009200000003007400000000003000'
    hard_puzzle2 = '970000043006000800000805000100090002060504070700030008000302000001000900680000025'
    test_puzzle = '009203800000009000408605103102000904000000000803000502906502307001000000005408600'

    # print(f'Test puzzle: {test_puzzle}')
    # print(solve_basic(test_puzzle))
    print(f'Easy puzzle: {easy_puzzle}')
    print_sudoku(solve_basic(easy_puzzle))
    print(f'Medium puzzle: {med_puzzle}')
    print_sudoku(solve_basic(med_puzzle))
    print(f'Medium puzzle2: {med_puzzle2}')
    print_sudoku(solve_basic(med_puzzle2))
    print(f'Medium puzzle3: {med_puzzle3}')
    print_sudoku(solve_basic(med_puzzle3))
    print(f'Hard puzzle: {hard_puzzle}')
    print_sudoku(solve_basic(hard_puzzle))
    print(f'Hard puzzle2: {hard_puzzle2}')
    print_sudoku(solve_basic(hard_puzzle2))
