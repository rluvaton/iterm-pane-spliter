import iterm2
from math import ceil
import iterm2.util
from iterm2 import Session

from iterm_pane_spliter.panes_parser.panes_tree import Size


async def get_tty(session: Session, output_path: str) -> None:
    await session.async_send_text(f'tty > "{output_path}"\n')


def set_pane_size(current_dimensions: Size, session: Session, node_size: Size):
    new_size = adapt_size(current_dimensions, node_size)
    session.preferred_size = iterm2.util.Size(new_size.width, new_size.height)


def adapt_size(current_dimensions: Size, from_dimensions: Size) -> Size:
    height_ratio = 100 / current_dimensions.height
    width_ratio = 100 / current_dimensions.width

    return Size(
        height=ceil(from_dimensions.height * height_ratio),
        width=ceil(from_dimensions.width * width_ratio),
    )
