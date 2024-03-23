from kittens.tui.handler import result_handler
from typing import List
from kitty.boss import Boss


def main(args: List[str]) -> str:
    pass


@result_handler(no_ui=True)
def handle_result(args: List[str],
                  answer: str,
                  target_window_id: int,
                  boss: Boss) -> None:
    tab = boss.active_tab

    if target_window_id == 1:
        w = boss.window_id_map.get(2)
        tab.set_active_window(w);
        tab.reset_window_sizes();
    else:
        w = boss.window_id_map.get(1)
        tab.set_active_window(w);
        tab.resize_window("wider", 100)
        tab.resize_window("taller", 100)