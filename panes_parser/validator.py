from typing import Union
from panes_parser.types import Corner, Coordinates


def assert_pane_structure(pane_structure: list[list[Union[int, str]]]) -> None:
    assert len(pane_structure) > 0, 'paneStructure must not be empty'
    assert len(pane_structure[0]) > 0, 'paneStructure must not be empty'
    assert all(len(row) == len(pane_structure[0]) for row in pane_structure), 'paneStructure must be a rectangle'

    corners = get_corners(pane_structure)

    for corner in corners:
        assert_only_rectangles(corner)
        assert_filled(corner, pane_structure)


def assert_only_rectangles(corner: Corner) -> None:
    assert corner.top_left.column == corner.bottom_left.column, \
        'top left and bottom left must be on the same column'

    assert corner.top_right.column == corner.bottom_right.column, \
        'top right and bottom right must be on the same column'

    assert corner.top_left.row == corner.top_right.row, \
        'top left and top right must be on the same row'

    assert corner.bottom_left.row == corner.bottom_right.row, \
        'bottom left and bottom right must be on the same row'


def assert_filled(corner: Corner, panes_structure: list[list[Union[int, str]]]) -> None:
    for row in range(corner.top_left.row, corner.bottom_left.row + 1):
        for column in range(corner.top_left.column, corner.top_right.column + 1):
            assert panes_structure[row][column] == corner.value or panes_structure[row][column] is None, \
                'rectangle must be filled with the same number'


def get_corners(matrix: list[list[Union[int, str]]]) -> list[Corner]:
    items = [item for row in matrix for item in row if item is not None]
    unique_items = list(set(items))
    return [get_corner_for_item(matrix, item) for item in unique_items]


def get_corner_for_item(matrix: list[list[Union[int, str]]], item: Union[int, str]) -> Corner:
    top_left_corner = None
    bottom_left_corner = None
    top_right_corner = None
    bottom_right_corner = None

    for row_number, row in enumerate(matrix):
        if item in row:
            column_number = row.index(item)
            top_left_corner = Coordinates(row=row_number, column=column_number)
            break

    assert top_left_corner is not None, f"{item} not found in matrix"

    for row_number, row in reversed(list(enumerate(matrix))):
        if item in row:
            column_number = row.index(item)
            bottom_left_corner = Coordinates(row=row_number, column=column_number)
            break

    for row_number, row in enumerate(matrix):
        if item in row:
            column_number = len(row) - 1 - row[::-1].index(item)
            top_right_corner = Coordinates(row=row_number, column=column_number)
            break

    for row_number, row in reversed(list(enumerate(matrix))):
        if item in row:
            column_number = len(row) - 1 - row[::-1].index(item)
            bottom_right_corner = Coordinates(row=row_number, column=column_number)
            break

    return Corner(
        value=item,
        top_left=top_left_corner,
        bottom_left=bottom_left_corner,
        top_right=top_right_corner,
        bottom_right=bottom_right_corner
    )
