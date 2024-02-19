from aiogram.fsm.state import State, StatesGroup


class UserFSM(StatesGroup):
    user_message_sed_success = State()
    user_success_message = State()
