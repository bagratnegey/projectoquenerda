
from keyboards.inline import dyn
from aiogram import types
from states import Flow
from loader import dp,db

text_button=[
    ['ye','no'],
    ['banana','bread','soap','pants','cockolate'],
    ['cocolad','icream','cockie'],
    ['winter','spring','summer','autumn']
]

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def bot_echo(message:types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer(f'wrong data,retry')
    else:
        await Flow.RegisterState.set()
        await message.answer(f'wellcum{message.from_user.full_name}\n')
        await db.add_user(message.contact.user_id,message.contact.phone_number)

@dp.callback_query_handler(text='0',state=Flow.RegisterState)
async def choose_yes(call:types.CallbackQuery):
    await Flow.Pickfruit.set()
    await call.message.answer(f'peick a fruit',reply_markup=dyn(text_button[1]))

@dp.callback_query_handler(text='1',state=Flow.RegisterState)
async def choose_no(call: types.CallbackQuery):
    await call.message.answer(f'well now you registered user')


@dp.callback_query_handler(text='0',state=Flow.Pickfruit)
async def second_choose(call:types.CallbackQuery):
    await Flow.Pickseason.set()
    await call.message.answer(f'pick the cold sweet',reply_markup=dyn(text_button[2]))

@dp.callback_query_handler(text='1',state=Flow.Pickseason)
async def third_one(call:types.CallbackQuery):
    await Flow.FinishedChoosing.set()
    await call.message.answer(f'thank,pick 2nd season of the year',reply_markup=dyn(text_button[3]))

@dp.callback_query_handler(text='1',state=Flow.FinishedChoosing)
async def finished_choosing(call:types.CallbackQuery):
    await Flow.FinishedChoosing.set()
    await call.message.answer(f'thank')

@dp.message_handler(state=Flow.RegisterState,commands=['Data'])
async def both_echo(message: types.Message):
    result=await db.get_users()
    a=''
    for i in result:
        a =+ f'id{i[0]},phone:{i[1]}.\n'
        await message.answer(text=a,reply_markup=buttons(result))




