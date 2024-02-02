from aiogram.fsm.state import State, StatesGroup


class AdminFSM(StatesGroup):
    start_it = State()
    admin_message_sed_success = State()
    admin_reg_success = State()
    admin_register_state = State()
