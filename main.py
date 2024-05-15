import asyncio


from aiogram import Bot, Dispatcher, Router, F 
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand
from handlers import include_routers

dp = Dispatcher()


bot = Bot(token='7195550903:AAGjmtNd5nNsKKvN0kxSv1gviSJCkHcndxU')
dp = Dispatcher

url="https://www.reddit.com/r/memes.json"
headers = {'User-Agent': 'MemeBot/1.0'}

router = Router()
@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command = 'start', description= 'Запуск бота'),
        BotCommand(command='help', description='Справка'),
    ])

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text ='вперед', callback_data= 'next')]
    ])
    await msg.answer(text="страница 1", reply_markup=inline_markup)
    
@router.callback_query(F.datta == 'next')
async def next_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text ='назад', callback_data='back')]
    ])
    await callback_query.message.replace()
    await callback_query.message.answer(
        text = 'страница 2',
        Reply_markup=inline_markup)
    
@router.callback_query(F.datta == 'next')
async def next_handler(callback_query:CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text ='назад', callback_data='back')]
    ])
    await callback_query.message.replace()
    await callback_query.message.answer(
        text = 'страница 1',
        Reply_markup=inline_markup)

    markup = ReplyKeyboardMarkup(Keyboard =[
        [KeyboardButton(text='говно'), KeyboardButton(text='переделывай')],
        [KeyboardButton(text='отчислиться')]
    ])

    markup = ReplyKeyboardMarkup(Keyboard = [[KeyboardButton(text='привет')]])
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='говно', callback_data ='1'), 
            InlineKeyboardButton(text='Переделай', callback_data = '2')],
        [       
            InlineKeyboardButton(text='Отчислиться', callback_data = '3')]
    ])
    
    
@router.callback_query(F.datta == '1')
async def callback_query_handler(callback_query:CallbackQuery):
    await callback_query.message.answer (text = 'разработка')



async def main():
       await dp.start_polling(bot)
dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())






