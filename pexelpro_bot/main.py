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
    #time.sleep(1)
    #btns = types.ReplyKeyboardMarkup(row_width=2)
    #btn_calc = types.KeyboardButton('/calculator')
    #btn_out = types.KeyboardButton('/quit')
    #btns.add(btn_calc, btn_out)
    #await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)
    await bot.send_message(message.from_user.id, 'Which operation do you want to make?', reply_markup=keyboard_request)

@dp.message_handler(commands=['с'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Goodbye! See you...',
                           reply_markup=types.ReplyKeyboardRemove())


tag_nr = "1"
tag_rs = "2"
tag_hello = "3"

tag_subject = "4"
tag_text = "5"
tag_file = "6"
tag_newfile = "7"
tag_remfile = "8"
tag_cancel = "9"
tag_commit = "10"

default_state = '<undefined>'
subject = default_state
text = default_state
files = [] 
tag = ''
cur_query = None
to_delete_msg = None


keyboard_request = types.InlineKeyboardMarkup(resize_keyboard=True)
keyboard_request.row(types.InlineKeyboardButton("create a new request", callback_data=tag_nr),
                     types.InlineKeyboardButton("check the status of my requests", callback_data=tag_rs))
keyboard_request.row(types.InlineKeyboardButton("nothing yet, just wanted to say hello", callback_data=tag_hello))



@dp.message_handler(commands=['request'])
async def start_handler(message: types.Message):
        await bot.send_message(message.from_user.id, 'Which operation do you want to make?', reply_markup=keyboard_request)



@dp.message_handler(content_types=["text"])
async def start_handler(message: types.Message):
        global subject, text, files, tag, cur_query
        #await message.reply(f"ku-ku {tag}")
        if tag == tag_subject:
            subject = message.text
            await func_nr(cur_query)
            await delete_msg(message)
        if tag == tag_text:
            text = message.text
            await func_nr(cur_query)
            await delete_msg(message)



async def delete_msg(message: types.Message):
    global to_delete_msg
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(message.chat.id, to_delete_msg.message_id)






@dp.message_handler(content_types=  ['image'])
async def start_handler(message: types.Message):
        global subject, text, files, tag, cur_query
        await message.reply(f"ku-ku {tag}")





@dp.callback_query_handler(lambda c: True)
async def callback_func(query):

    global tag, cur_query, to_delete_msg
    cur_query = query
    tag = query.data   

    #await query.message.reply("la-la")    

    if tag == tag_nr:
        await func_nr(query)

    elif tag == tag_subject:
        to_delete_msg = await query.message.reply(f"enter subject")        
        #to_delete_msg = await bot.send_message(query.message.chat.id, 'enter subject')

    elif tag == tag_text:
        to_delete_msg = await query.message.reply(f"enter text")

    elif tag == tag_file:
        await func_file(query)
    
    elif tag == tag_newfile:
        to_delete_msg = await query.message.reply(f"enter file")  

    elif tag == tag_commit:
        await func_file(query)
  
    



async def func_nr(query):
        #await query.message.reply(f"mu-mu")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.row(types.InlineKeyboardButton("add subject", callback_data=tag_subject),
                        types.InlineKeyboardButton("add text", callback_data=tag_text),
                        types.InlineKeyboardButton("add/remove file(s)", callback_data=tag_file))
        if subject != '' and subject != default_state and text != '' and text != default_state:
            keyboard.row(types.InlineKeyboardButton("send", callback_data=tag_commit))
        keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_cancel))

        temp = f"subject: {subject}\n\ntext: {text}\n\nfiles: {', '.join(files)}"

        await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    text=temp, reply_markup=keyboard)



async def func_file(query):
        #await query.message.reply(f"mu-mu")
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        
        keyboard.row(types.InlineKeyboardButton("add new", callback_data=tag_newfile))
        for i in files:
            keyboard.row(types.InlineKeyboardButton(f"remove {i}", callback_data=f'{tag_remfile}_{i}'))
        keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_cancel))

        temp = f"select option"

        await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                    text=temp, reply_markup=keyboard)






if __name__ == '__main__':
    executor.start_polling(dp)
