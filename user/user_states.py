from aiogram.fsm.state import StatesGroup, State


class UserFSM(StatesGroup):
    success_message = State()
    is_message_correct = State()
    check_message = State()
    send_message = State()
