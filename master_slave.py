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
                match w_number:
                    case 1:
                        tab.first_window()
                    case 2:
                        tab.second_window()
                    case 3:
                        tab.third_window()
                    case 4:
                        tab.fourth_window()
                    case 5:
                        tab.fifth_window()
                    case 6:
                        tab.sixth_window()
                    case 7:
                        tab.seventh_window()
                    case 8:
                        tab.eighth_window()
                    case 9:
                        tab.ninth_window()
                    case 10:
                        tab.tenth_window()
                    case _:
                        tab.next_window()

                if tab.current_layout.name != "splits":
                    tab.toggle_layout("splits")
