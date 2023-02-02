
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def dyn(text_button):
    a=len(text_button)
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=text_button[i],callback_data=str(i))for i in range(0,a)
            ]
        ]
    )
phone=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='share your phone noombir',request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
