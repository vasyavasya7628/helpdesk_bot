from aiogram.fsm.state import StatesGroup, State


class UserFSM(StatesGroup):
    success_message = State("success_message")
    is_message_correct = State("is_message_correct")
    check_message = State("check_message")
    send_message = State("send_message")
