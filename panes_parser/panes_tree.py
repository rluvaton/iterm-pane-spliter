from typing import Union


class Size:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __eq__(self, other):
        return self.height == other.height and self.width == other.width


class TreeNode:
    def __init__(self, node_id: Union[int, str, None], size: Size):
        self.id = node_id
        self.size = size

    def __eq__(self, other):
        return self.id == other.id and self.size == other.size


class TreeLeaf(TreeNode):
    def __init__(self, node_id: Union[int, str], size: Size):
        super().__init__(node_id, size)

    def __eq__(self, other):
        return self.id == other.id and self.size == other.size


class SplitNode(TreeNode):
    def __init__(self, split_type: str, size: Size, splits: list[TreeNode]):
        super().__init__(None, size)
        assert split_type == 'bottom' or split_type == 'right', \
            'split_type must be either "bottom" or "right"'
        assert len(splits) == 2, 'splits must be a list of 2 elements'

        self.type = split_type
        self.splits = splits

    def __eq__(self, other):
        # TODO - fix splits compare
        return self.type == other.type and self.splits == other.splits and self.size == other.size
