from typing import cast, Union

from iterm2 import Session

from panes_parser.panes_tree import TreeNode, TreeLeaf, SplitNode


class PaneData:
    def __init__(self, session: Session, node: TreeLeaf):
        self.session = session
        self.node = node


async def split_trees(session: Session, node: TreeNode, all_panes: dict[Union[str, int], PaneData]) -> None:
    if node.id is not None:
        await session.async_set_name(f"{node.id}")
        all_panes[node.id] = PaneData(session, cast(TreeLeaf, node))
        return

    split_node = cast(SplitNode, node)

    if split_node.type == 'bottom':
        top, bottom = split_node.splits

        # The current session will be the top session
        top_session = session
        bottom_session = await session.async_split_pane(vertical=False)

        await split_trees(top_session, top, all_panes)
        await split_trees(bottom_session, bottom, all_panes)

        return

    if split_node.type == 'right':
        left, right = split_node.splits

        # The current session will be the left session
        left_session = session
        right_session = await session.async_split_pane(vertical=True)

        await split_trees(left_session, left, all_panes)
        await split_trees(right_session, right, all_panes)

        return

    raise ValueError(f"Invalid node type: {node['type']}")
