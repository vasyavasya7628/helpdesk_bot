from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from handlers.user.user_fsm import UserFSM
from keyboards.menu.start_keyboard import get_kb_start
from res.resources import Text

window_router = Router()


@window_router.message(F.text == Text.WRITE_TO_IT.value)
async def write_window_num(message: Message, state: FSMContext):
    await message.answer(f"Введите номер окна:\n"
                         f"(Если вы нажали кнопку случайно, напишите \"отмена\" и нажмите кнопку \"ENTER\")",
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(UserFSM.send_window)


@window_router.message(UserFSM.send_window)
async def reply_window(message: Message, state: FSMContext):
    res = await is_digit(state, message.text)
    if message.text == "отмена" or message.text == "Отмена":
        await state.clear()
        await message.answer("Возврат в главное меню", reply_markup=get_kb_start())
    else:
        if res is None:
            await message.answer(f"Вы ввели не число. Введите окно ещё раз. \n(Окно должно быть числом)")
            await state.set_state(UserFSM.send_window)
        elif 0 <= res <= 89:
            await message.answer(f"Вы ввели окно: {res}. Опишите вашу проблему.")
            await state.update_data(window=message.text)
            await state.set_state(UserFSM.success_message)
        else:
            await message.answer("Такого окна не существует. Введите окно ещё раз. \n(Введите существующее окно)")
            await state.set_state(UserFSM.send_window)


async def is_digit(state, text):
    try:
        num = int(text)
        await state.set_state(UserFSM.send_window)
        return num
    except ValueError:
        await state.set_state(UserFSM.send_window)
