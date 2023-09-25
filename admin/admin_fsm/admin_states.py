from aiogram.fsm.state import StatesGroup, State


class AdminFSM(StatesGroup):
    reg_success = State()
    choose_district = State()
