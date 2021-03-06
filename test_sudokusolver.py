import sudokusolver as s
import pytest


# TODO Add test cases for unexpected input?
@pytest.mark.parametrize('test_square, expected_result', [
    ((0, 4), [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)]),
    ((1, 3), [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]),
    ((2, 6), [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8)]),
    ((3, 7), [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)]),
    ((4, 1), [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)]),
    ((5, 7), [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8)]),
    ((6, 8), [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)]),
    ((7, 3), [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)]),
    ((8, 2), [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]),
])
def test_get_row(test_square, expected_result):
    assert s.get_row(test_square) == expected_result


# TODO Add test cases for unexpected input?
@pytest.mark.parametrize('test_square, expected_result', [
    ((0, 0), [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]),
    ((7, 1), [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]),
    ((4, 2), [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]),
    ((0, 3), [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)]),
    ((8, 4), [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)]),
    ((3, 5), [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]),
    ((6, 6), [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)]),
    ((2, 7), [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)]),
    ((3, 8), [(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)]),
])
def test_get_col(test_square, expected_result):
    assert s.get_col(test_square) == expected_result


# TODO Add test cases for unexpected input?
@pytest.mark.parametrize('test_square, expected_result', [
    ((0, 0), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]),
    ((1, 3), [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]),
    ((2, 6), [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]),
    ((3, 2), [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]),
    ((3, 5), [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]),
    ((3, 6), [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]),
    ((8, 2), [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]),
    ((8, 5), [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]),
    ((7, 7), [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]),
])
def test_get_box(test_square, expected_result):
    assert s.get_box(test_square) == expected_result


@pytest.mark.parametrize('test_list0, test_list1, test_list2, expected_result', [
    ([1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2]),
    ([1, 2, 3], [1, 2, 4], [3, 4, 5], []),
    ([1, 2, 3], [4, 5, 6], [7, 8, 9], []),
    ([1, 'a', (2, 3)], [2, (2, 3)], [(2, 3), 'a', 1, 2, 3], [(2, 3)]),
])
def test_three_list_intersection(test_list0, test_list1, test_list2, expected_result):
    assert s.three_list_intersection(test_list0, test_list1, test_list2) == expected_result


@pytest.mark.parametrize('test_sudoku, expected_result', [
    ('', []),
    ('a30070000600195000098000060800060003400803001700020006060000280000419005000080079', []),
    (' 30070000600195000098000060800060003400803001700020006060000280000419005000080079', []),
    ('53007000060019500009800006080006000340080300170002000606000028000041900500008007 ', []),
    ('5300700006001950000980000608000600034008030017000200060600002800004190050000800791', []),
    ('530070000600195000098000060800060003400803001700020006060000280000419005000080079',
     [[[5, []], [3, []], [0, []], [0, []], [7, []], [0, []], [0, []], [0, []], [0, []]],
      [[6, []], [0, []], [0, []], [1, []], [9, []], [5, []], [0, []], [0, []], [0, []]],
      [[0, []], [9, []], [8, []], [0, []], [0, []], [0, []], [0, []], [6, []], [0, []]],
      [[8, []], [0, []], [0, []], [0, []], [6, []], [0, []], [0, []], [0, []], [3, []]],
      [[4, []], [0, []], [0, []], [8, []], [0, []], [3, []], [0, []], [0, []], [1, []]],
      [[7, []], [0, []], [0, []], [0, []], [2, []], [0, []], [0, []], [0, []], [6, []]],
      [[0, []], [6, []], [0, []], [0, []], [0, []], [0, []], [2, []], [8, []], [0, []]],
      [[0, []], [0, []], [0, []], [4, []], [1, []], [9, []], [0, []], [0, []], [5, []]],
      [[0, []], [0, []], [0, []], [0, []], [8, []], [0, []], [0, []], [7, []], [9, []]]]
     )
])
def test_convert_sudoku_string_to_grid(test_sudoku, expected_result):
    assert s.convert_sudoku_string_to_grid(test_sudoku) == expected_result


@pytest.mark.parametrize('test_sudoku, expected_result', [
    ([], ''),
    ([[[5, []], [3, []], [0, []], [0, []], [7, []], [0, []], [0, []], [0, []], [0, []]],
      [[6, []], [0, []], [0, []], [1, []], [9, []], [5, []], [0, []], [0, []], [0, []]],
      [[0, []], [9, []], [8, []], [0, []], [0, []], [0, []], [0, []], [6, []], [0, []]],
      [[8, []], [0, []], [0, []], [0, []], [6, []], [0, []], [0, []], [0, []], [3, []]],
      [[4, []], [0, []], [0, []], [8, []], [0, []], [3, []], [0, []], [0, []], [1, []]],
      [[7, []], [0, []], [0, []], [0, []], [2, []], [0, []], [0, []], [0, []], [6, []]],
      [[0, []], [6, []], [0, []], [0, []], [0, []], [0, []], [2, []], [8, []], [0, []]],
      [[0, []], [0, []], [0, []], [4, []], [1, []], [9, []], [0, []], [0, []], [5, []]],
      [[0, []], [0, []], [0, []], [0, []], [8, []], [0, []], [0, []], [7, []], [9, []]]],
     '530070000600195000098000060800060003400803001700020006060000280000419005000080079')])
def test_convert_sudoku_grid_to_string(test_sudoku, expected_result):
    assert s.convert_sudoku_grid_to_string(test_sudoku) == expected_result


def test_find_group_missing_numbers():
    grid = [[[5, []], [3, []], [0, []], [0, []], [7, []], [0, []], [0, []], [0, []], [0, []]],
            [[6, []], [0, []], [0, []], [1, []], [9, []], [5, []], [0, []], [0, []], [0, []]],
            [[0, []], [9, []], [8, []], [0, []], [0, []], [0, []], [0, []], [6, []], [0, []]],
            [[8, []], [0, []], [0, []], [0, []], [6, []], [0, []], [0, []], [0, []], [3, []]],
            [[4, []], [0, []], [0, []], [8, []], [0, []], [3, []], [0, []], [0, []], [1, []]],
            [[7, []], [0, []], [0, []], [0, []], [2, []], [0, []], [0, []], [0, []], [6, []]],
            [[0, []], [6, []], [0, []], [0, []], [0, []], [0, []], [2, []], [8, []], [0, []]],
            [[0, []], [0, []], [0, []], [4, []], [1, []], [9, []], [0, []], [0, []], [5, []]],
            [[0, []], [0, []], [0, []], [0, []], [8, []], [0, []], [0, []], [7, []], [9, []]]]
    squares = [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
    assert s.find_group_missing_numbers(squares, grid) == [2, 4, 5, 7, 8, 9]


def test_get_square_options_missing_numbers():
    grid = [[[5, []], [3, []], [0, []], [0, []], [7, []], [0, []], [0, []], [0, []], [0, []]],
            [[6, []], [0, []], [0, []], [1, []], [9, []], [5, []], [0, []], [0, []], [0, []]],
            [[0, []], [9, []], [8, []], [0, []], [0, []], [0, []], [0, []], [6, []], [0, []]],
            [[8, []], [0, []], [0, []], [0, []], [6, []], [0, []], [0, []], [0, []], [3, []]],
            [[4, []], [0, []], [0, []], [8, []], [0, []], [3, []], [0, []], [0, []], [1, []]],
            [[7, []], [0, []], [0, []], [0, []], [2, []], [0, []], [0, []], [0, []], [6, []]],
            [[0, []], [6, []], [0, []], [0, []], [0, []], [0, []], [2, []], [8, []], [0, []]],
            [[0, []], [0, []], [0, []], [4, []], [1, []], [9, []], [0, []], [0, []], [5, []]],
            [[0, []], [0, []], [0, []], [0, []], [8, []], [0, []], [0, []], [7, []], [9, []]]]
    square = (3, 6)
    options = s.get_square_options_missing_numbers(square, grid)
    options.sort()
    assert options == [4, 5, 7, 9]


def test_find_group_single_candidate():
    grid = [[[5, []], [3, []], [0, []], [0, []], [7, []], [0, []], [0, []], [0, []], [0, []]],
            [[6, []], [0, []], [0, []], [1, []], [9, []], [5, []], [0, []], [0, []], [0, []]],
            [[0, [1, 2]], [9, []], [8, []], [0, []], [0, []], [0, []], [0, []], [6, []], [0, []]],
            [[8, []], [0, []], [0, []], [0, []], [6, []], [0, []], [0, []], [0, []], [3, []]],
            [[4, []], [0, []], [0, []], [8, []], [0, []], [3, []], [0, []], [0, []], [1, []]],
            [[7, []], [0, []], [0, []], [0, []], [2, []], [0, []], [0, []], [0, []], [6, []]],
            [[0, [1, 3, 9]], [6, []], [0, []], [0, []], [0, []], [0, []], [2, []], [8, []], [0, []]],
            [[0, [2, 3]], [0, []], [0, []], [4, []], [1, []], [9, []], [0, []], [0, []], [5, []]],
            [[0, [1, 2, 3]], [0, []], [0, []], [0, []], [8, []], [0, []], [0, []], [7, []], [9, []]]]
    square = (6, 0)
    squares = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)]
    assert s.find_group_single_candidate(square, squares, grid) == [9]


def test_get_options_scan_singles():
    grid = [[[5, []], [3, []], [0, []], [0, []], [7, []], [0, []], [0, []], [0, []], [0, []]],
            [[6, []], [0, []], [0, []], [1, []], [9, []], [5, []], [0, []], [0, []], [0, []]],
            [[0, [1, 2]], [9, []], [8, []], [0, []], [0, []], [0, []], [0, []], [6, []], [0, []]],
            [[8, []], [0, []], [0, []], [0, []], [6, []], [0, []], [0, []], [0, []], [3, []]],
            [[4, []], [0, []], [0, []], [8, []], [0, []], [3, []], [0, []], [0, []], [1, []]],
            [[7, []], [0, []], [0, []], [0, []], [2, []], [0, []], [0, []], [0, []], [6, []]],
            [[0, [1, 3, 9]], [6, []], [0, []], [0, []], [0, []], [0, []], [2, []], [8, []], [0, []]],
            [[0, [2, 3]], [0, []], [0, []], [4, []], [1, []], [9, []], [0, []], [0, []], [5, []]],
            [[0, [1, 2, 3]], [0, []], [0, []], [0, []], [8, []], [0, []], [0, []], [7, []], [9, []]]]
    square = (6, 0)
    assert s.get_square_options_scan_singles(square, grid) == [9]


def test_find_group_pairs():
    grid = [[[0, []], [0, []], [9, []], [2, []], [0, []], [3, []], [8, []], [0, []], [0, []]],
            [[0, []], [0, []], [0, []], [0, []], [0, []], [9, []], [0, []], [0, []], [0, []]],
            [[4, []], [0, []], [8, []], [6, []], [7, []], [5, []], [1, []], [0, []], [3, []]],
            [[1, []], [0, []], [2, []], [0, []], [0, []], [0, []], [9, []], [0, []], [4, []]],
            [[0, []], [0, []], [0, []], [0, []], [0, []], [0, []], [0, []], [0, []], [0, []]],
            [[8, []], [0, []], [3, []], [0, []], [0, []], [0, []], [5, []], [0, []], [2, []]],
            [[9, []], [0, [4, 8]], [6, []], [5, []], [0, []], [2, []], [3, []], [0, []], [7, []]],
            [[0, [2, 3, 7]], [0, [2, 3, 4, 7, 8]], [1, []], [0, []], [0, []], [0, []], [0, []], [0, []], [0, []]],
            [[0, [2, 3, 7]], [0, [1, 2, 3, 7]], [5, []], [4, []], [0, []], [8, []], [6, []], [0, []], [0, []]]]
    square = (7, 1)
    group = [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
    assert set(s.find_group_pairs(square, group, grid)) == {4, 8}


@pytest.mark.parametrize('test_sudoku, expected_result', [
    ('530070000600195000098000060800060003400803001700020006060000280000419005000080079',
     '534678912672195348198342567859761423426853791713924856961537284287419635345286179'),
    ('970000043006000800000805000100090002060504070700030008000302000001000900680000025',
     '978261543526943817314875296145798632863524179792136458459382761231657984687419325')
])
def test_solve_basic(test_sudoku, expected_result):
    assert s.convert_sudoku_grid_to_string(s.solve_basic(test_sudoku)) == expected_result
