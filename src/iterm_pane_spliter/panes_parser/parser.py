from typing import Union

from src.iterm_pane_spliter.panes_parser.panes_tree import Size, TreeNode, TreeLeaf, SplitNode
from src.iterm_pane_spliter.panes_parser.validator import assert_pane_structure


def convert_pane_structures_to_tree(pane_structure: list[list[Union[int, str]]]) -> TreeNode:
    assert_pane_structure(pane_structure)
    size = Size(height=len(pane_structure), width=len(pane_structure[0]))

    number_of_panes = len(set(cell for row in pane_structure for cell in row))

    if number_of_panes == 1:
        return TreeLeaf(
            node_id=pane_structure[0][0],
            size=size
        )

    column_split_tree_node = split_columns(pane_structure, size)
    if column_split_tree_node is not None:
        return column_split_tree_node

    row_split_tree_node = split_rows(pane_structure, size)
    if row_split_tree_node is not None:
        return row_split_tree_node

    raise ValueError("Not supported yet")


def split_columns(pane_structure: list[list[Union[int, str]]], size: Size) -> Union[SplitNode, None]:
    column_to_split_until = get_first_column_to_split(pane_structure)
    from_column_split = get_last_column_to_split(pane_structure)

    if column_to_split_until is not None:
        left, right = split_to_2_vertical_sections(pane_structure, column_to_split_until + 1)
    elif from_column_split is not None:
        left, right = split_to_2_vertical_sections(pane_structure, from_column_split)
    else:
        return None

    return SplitNode(
        split_type="right",
        size=size,
        splits=[
            convert_pane_structures_to_tree(left),
            convert_pane_structures_to_tree(right),
        ],
    )


def split_rows(pane_structure: list[list[Union[int, str]]], size) -> Union[SplitNode, None]:
    row_to_split_until = get_first_row_to_split(pane_structure)
    from_row_split = get_last_row_to_split(pane_structure)

    if row_to_split_until is not None:
        top, bottom = split_to_2_horizontal_sections(pane_structure, row_to_split_until + 1)
    elif from_row_split is not None:
        top, bottom = split_to_2_horizontal_sections(pane_structure, from_row_split)
    else:
        return None

    return SplitNode(
        split_type="bottom",
        size=size,
        splits=[
            convert_pane_structures_to_tree(top),
            convert_pane_structures_to_tree(bottom),
        ]
    )


def get_first_row_to_split(pane_structure: list[list[Union[int, str]]]) -> Union[int, None]:
    to_row = -1
    exit_loop = False

    for i in range(len(pane_structure) - 1):
        row = pane_structure[i]
        next_row = pane_structure[i + 1]

        for j in range(len(row)):
            if row[j] != next_row[j]:
                exit_loop = True
                break

        to_row = i
        if exit_loop:
            break

    rows_that_maybe_can_split = pane_structure[: to_row + 1]

    if not rows_that_maybe_can_split:
        return None

    rows_that_left = pane_structure[to_row + 1 :]

    ids_in_rows_that_split = set(cell for row in rows_that_maybe_can_split for cell in row)
    ids_in_rows_that_left = set(cell for row in rows_that_left for cell in row)

    can_split = all(id not in ids_in_rows_that_left for id in ids_in_rows_that_split)

    if not can_split:
        return None

    return to_row


def get_last_row_to_split(pane_structure: list[list[Union[int, str]]]) -> Union[int, None]:
    upside_down_matrix = pane_structure[::-1]
    index = get_first_row_to_split(upside_down_matrix)

    if index is None:
        return None

    return len(upside_down_matrix) - index - 1


def get_first_column_to_split(pane_structure: list[list[Union[int, str]]]) -> Union[int, None]:
    return get_first_row_to_split(list(map(list, zip(*pane_structure))))


def get_last_column_to_split(pane_structure: list[list[Union[int, str]]]) -> Union[int, None]:
    return get_last_row_to_split(list(map(list, zip(*pane_structure))))


def split_to_2_vertical_sections(
        pane_structure: list[list[Union[int, str]]],
        column_index: int
) -> tuple[list[list[Union[int, str]]], list[list[Union[int, str]]]]:
    left = [row[:column_index] for row in pane_structure]
    right = [row[column_index:] for row in pane_structure]
    return left, right


def split_to_2_horizontal_sections(
        pane_structure: list[list[Union[int, str]]],
        row_index: int
) -> tuple[list[list[Union[int, str]]], list[list[Union[int, str]]]]:
    top = pane_structure[:row_index]
    bottom = pane_structure[row_index:]
    return top, bottom
