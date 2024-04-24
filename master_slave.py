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

    option = args[1] if len(
        args) > 1 else None

    match option:
        case "mark":
            setattr(boss, "mwid", target_window_id)
        case _:
            to_focus = None
            mwid: int
            w_number = int(
                option) if option is not None and option.isdecimal() else None

            if hasattr(boss, "mwid"):
                mwid = getattr(boss, "mwid")
            else:
                mwid = target_window_id
                setattr(boss, "mwid", target_window_id)

            if mwid != target_window_id and w_number is None:
                to_focus = mwid
                tab.set_active_window(to_focus)
                if tab.current_layout.name != "stack":
                    tab.toggle_layout("stack")
            else:
                # TODO use neighbouring windows instead
                for index, window in enumerate(tab.windows):
                    if w_number is None:
                        if window.id != mwid:
                            to_focus = window.id
                            break
                    elif w_number >= len(tab.windows):
                        if index == len(tab.windows) - 1:
                            to_focus = window.id
                    elif index >= w_number and window.id != mwid:
                        to_focus = window.id
                        break

                if to_focus is not None:
                    tab.set_active_window(to_focus)

                if tab.current_layout.name != "splits":
                    tab.toggle_layout("splits")
