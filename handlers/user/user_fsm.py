from aiogram.fsm.state import State, StatesGroup


class UserFSM(StatesGroup):
    cancel_message = State()
    send_window = State()
    enter_window = State()
    incorrect_message = State()
    check_window = State()
    send_message = State()
    success_message = State()
    message_send_success = State()

    test_send = State()

