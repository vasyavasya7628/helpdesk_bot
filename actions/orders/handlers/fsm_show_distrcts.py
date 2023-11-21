from aiogram.fsm.state import State, StatesGroup


class DistrictsFSM(StatesGroup):
    chose_district = State()
