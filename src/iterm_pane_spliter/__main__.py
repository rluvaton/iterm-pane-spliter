#!/usr/bin/env python3
import json
import os.path
import sys
from typing import Union

import iterm2
from iterm2 import Connection, App, Window

from iterm_pane_spliter.panes_creator import PaneData, split_trees
from iterm_pane_spliter.panes_parser.panes_tree import TreeNode
from iterm_pane_spliter.panes_parser.parser import convert_pane_structures_to_tree
from iterm_pane_spliter.terminal_helper import set_pane_size, get_tty

app: Union[App, None] = None
window: Union[Window, None] = None
connection: Union[Connection, None] = None
pane_tree: Union[TreeNode, None] = None
base_dir: Union[str, None] = None


async def split_panes_from_tree() -> dict[Union[str, int], PaneData]:
    tab = window.current_tab
    session = tab.current_session

    all_panes: dict[Union[str, int], PaneData] = {}

    await split_trees(
        session,
        pane_tree,
        all_panes,
    )

    for pane_id, data in all_panes.items():
        pane_session = data.session
        set_pane_size(pane_tree.size, pane_session, data.node.size)

        # You need to set the badge text in the default profile to be: `\(user.badge_text)` so it will be replaced
        await pane_session.async_set_variable("user.badge_text", f"{pane_id}")

    await tab.async_update_layout()

    return all_panes


async def main(connection_arg: Connection) -> None:
    global connection
    global app
    global window
    global base_dir

    connection = connection_arg

    app = await iterm2.async_get_app(connection)
    window = app.current_window
    if window is None:
        print("No current window")
        return

    await window.async_create_tab()
    all_panes = await split_panes_from_tree()

    if base_dir is None:
        return

    for pane_id, pane_data in all_panes.items():
        file_path = os.path.join(base_dir, f"{pane_id}.txt")
        pane_session = pane_data.session
        await get_tty(pane_session, file_path)


def cli():
    global base_dir
    global pane_tree

    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: python script.py [? tmp dir] "[[1,2,3],[4,5,6]]"')
        sys.exit(1)

    if len(sys.argv) == 3:
        base_dir = sys.argv[1]
        raw_pane_structure = sys.argv[2]
    else:
        base_dir = None
        raw_pane_structure = sys.argv[1]

    try:
        pane_structure = json.loads(raw_pane_structure)
    except json.JSONDecodeError:
        print("Invalid JSON input")
        sys.exit(1)

    pane_tree = convert_pane_structures_to_tree(pane_structure)
    iterm2.run_until_complete(main)


if __name__ == "__main__":
    cli()
