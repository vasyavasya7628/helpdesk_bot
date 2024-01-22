from enum import Enum


class Names(Enum):
    GET_DISTRICTS = [
        "Отдел 'Мои документы' город Кемерово, бр Пионерский, 3",
        "26",
        "31"
    ]


print(Names.GET_DISTRICTS.value)
