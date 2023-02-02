
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import phone
from loader import dp
from states import Flow

@dp.message_handler(CommandStart,state=Flow.RegisterState)
async def bot_start(message: types.Message):
    await message.answer(f"you hev already blahjwwwrhergergj")

@dp.message_handler(CommandStart)
async def bot_echo(message:types.Message):
    await message.answer(f'for using this porvide phone number',reply_markup=phone)
