
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
colors=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='red'),
            KeyboardButton(text='gay'),
            KeyboardButton(text='blue',request_contact=True)
        ]
    ],
    resize_keyboard=True
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

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def dyn(text_button):
    a=len(text_button)
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=text_button[i],callback_data=str(i))for i in range(0,a)
            ]
        ]
    )
def buttons(text_button):
    a = len(text_button)
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=str(text_button[i][0])+str(text_button[i][1]),callback_data=str((i+1)))for i in range(0,a)
            ]
        ]
    )
