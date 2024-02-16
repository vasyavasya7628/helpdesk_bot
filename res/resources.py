from enum import Enum


class Text(Enum):
    PARSE_MODE = "HTML"
    TELL_ABOUT_YOUR_PROBLEM = "Сообщить о неисправности/проблеме (Для специалистов)"
    REGISTER_FOR_ADMINS = "Зарегистрироваться(Для администраторов)"
    END_REGISTER_FOR_ADMINS = "Регистрация завершена!"
    CHOOSE_BUTTON = "Выберите"
    INCORRECT_TEXT = "Если вы хотите сообщить о неполадках, следуйте кнопкам в меню"
    INCORRECT_IMAGE = "Этот бот не для того, чтобы отправлять стикеры."
    INCORRECT_GIF = "Этот бот не для того, чтобы отправлять Гиф-файлы."
    WRITE_TO_IT = "Написать в IT-Отдел."
    ADMIN_CHOOSE_DISTRICT = "Выберите ведомство из списка(Для It специалистов):"
    USER_CHOOSE_DISTRICT = "Выберите ведомство из списка(Для специалистов c окно):"
    RETURN_TO_MAIN_MENU = "Вернуться в главное меню"
    MY_ORDERS_AT_WORK = "В работе"
    MY_ORDERS_DELAYED = "Отложены"
    MY_ORDERS_COMPLETED = "Выполненные"
    ACTIVE_ORDERS = "Ожидают реакции"
    MY_ORDERS = "Мои заявки"
    ORDERS = "Выберите ведомство в котором вы хотите посмотреть заявки?"
    YOUR_ORDERS = "Ваши заявки"
    ADMIN_LOGIN = "Зарегистрироваться(для it специалистов)"
    ORDER_LIST = "Список заявок"
    REGISTER_COMPLETE = "Регистрация завершена!"
    GREETINGS = ("Здравствуйте, чем я могу вам помочь?\n"
                 "Если вы специалист и у вас есть проблема, нажмите кнопку 'Написать в IT-Отдел'.\n")
    DESCRIBE_YOUR_PROBLEM = "Опишите вашу проблему"
    MESSAGE_CORRECT = "Вы уверены, что описали проблему правильно?"
    LOWER_CASE = "_"
    ORDER_SEND = "Заявка успешно создана! Специалисты свяжутся с вами в ближайшее время."
    GET_DISTRICTS = [
        "Отдел 'Мои документы' город Кемерово, бр Пионерский, 3",
        "26",
    ]
    SEND_YES = "Да✅"
    SEND_NO = "Нет❌"
    SEND_MESSAGE_TO_IT = "Да, отправить сообщение об ошибке специалистам"
    DONT_SEND_NOT_SURE = "Я не уверен(а), хочу изменить сообщение."
    MENU = "Меню"


# 🔧 🔨 ⚒ 🛠 ⛏


class OrderStatus(Enum):
    WAITING = "ожидает реакции"
    IN_PROGRESS = "в работе"
    ENDED = "завершена"
    DELAYED = "отложена"


class OrderActions(Enum):
    GET_WORK = "Взять в работу🛠",
    DELAY_WORK = "Передать заявку другому специалисту📡",
    END_WORK = "Закрыть в заявку✅"


class OrderDatabaseActions(Enum):
    CLOSE = "close"
    DELAY = "delay"
