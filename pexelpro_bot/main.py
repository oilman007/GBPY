import time
import logging
from aiogram import Bot, Dispatcher, executor, types

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


MSG = "{}, choose an action:"

bot = Bot("6107381299:AAH_HNQbbkL2ofCLSrVXPT6SuItprBThsM8")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Hi, {user_full_name}!")
    time.sleep(1)
    #btns = types.ReplyKeyboardMarkup(row_width=2)
    #btn_calc = types.KeyboardButton('/calculator')
    #btn_out = types.KeyboardButton('/quit')
    #btns.add(btn_calc, btn_out)
    #await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)
    await bot.send_message(message.from_user.id, 'Which operation do you want to make?', reply_markup=keyboard)

@dp.message_handler(commands=['с'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Goodbye! See you...',
                           reply_markup=types.ReplyKeyboardRemove())

keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard.row(types.InlineKeyboardButton("create a new request", callback_data="nr"),
             types.InlineKeyboardButton("check the status of my requests", callback_data="rs"))
keyboard.row(types.InlineKeyboardButton("nothing yet, just wanted to say hello", callback_data="no"))

@dp.message_handler(commands=['request'])
async def start_handler(message: types.Message):
        await bot.send_message(message.from_user.id, 'Which operation do you want to make?', reply_markup=keyboard)

@dp.callback_query_handler(lambda c: True)
async def callback_calc(query):

    global value, old_value
    data = query.data

    if data == "C":
        value = ""
    elif data == "<=":
        if value != "":
            if len(value) == 1:
                value = ""
            else:
                value = value[:len(value)-1]
    elif data == "=":
        try:
            value = str(eval(value))
        except:
            value = "Error"
    else:
        value += data

    if (value != old_value and value != "") or ("0" != old_value and value == ""):
        if value == "":
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text="0", reply_markup=keyboard)
            old_value = "0"
        else:
            await bot.edit_message_text(chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        text=value, reply_markup=keyboard)

            old_value = value

    if value == "Error":
        value = ""

if __name__ == '__main__':
    executor.start_polling(dp)
