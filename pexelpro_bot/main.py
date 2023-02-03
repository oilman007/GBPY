import time
import logging
import sqlite3
from aiogram import Bot, Dispatcher, executor, types
from random import randint
import privacy


# https://pypi.org/project/pyTelegramBotAPI/


# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


class DBRecord:
    def __init__(self, user, subject, message, attachment, status, id):
        self.user = user
        self.subject = subject
        self.message = message
        self.attachment = attachment
        self.status = status
        self.id = id




# global variables
bot = Bot(privacy.TOKEN)
dp = Dispatcher(bot=bot)

default_state = '<undefined>'
record = DBRecord(default_state,default_state,default_state,[],"",0)
tag = ''
#cur_query = None
menu_msg = None
to_delete_msg = None



# menu
async def edit_menu(message, new_text, new_keyboard):
    await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                text = new_text, reply_markup= new_keyboard)

def request_menu():
    return f"request ID: {randint(1, 1000)}\n\nsubject: {record.subject}\n\ntext: {record.message}\n\nfiles: {', '.join(record.attachment)}"




# keyboards
async def request_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.row(types.InlineKeyboardButton("edit subject", callback_data=tag_subject),
                    types.InlineKeyboardButton("edit text", callback_data=tag_text),
                    types.InlineKeyboardButton("add attachment", callback_data=tag_newfile))

    btns = []
    for i in record.attachment:
        btns.append(types.InlineKeyboardButton(f"remove '{i}'", callback_data=f'{tag_remfile} {i}'))
    
    keyboard.row(*btns)

    if record.subject != '' and record.subject != default_state and (record.message != '' and record.message != default_state or len(record.attachment) > 0):
        keyboard.row(types.InlineKeyboardButton("send request", callback_data=tag_commit))

    keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_to_start))
    return keyboard 


async def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    keyboard.row(types.InlineKeyboardButton("create a new request", callback_data=tag_nr),
                        types.InlineKeyboardButton("check my requests status", callback_data=tag_rs))
    keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_exit))
    return keyboard





# commands
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    global menu_msg
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    menu_msg = await message.reply(f"Hi, {user_full_name}!")
    #time.sleep(1)
    #btns = types.ReplyKeyboardMarkup(row_width=2)
    #btn_calc = types.KeyboardButton('/calculator')
    #btn_out = types.KeyboardButton('/quit')
    #btns.add(btn_calc, btn_out)
    #await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)
    await edit_menu(menu_msg, 'Which operation do you want to make?', await start_keyboard())





# tags
tag_exit = "0"
tag_nr = "1"
tag_rs = "2"
#tag_hello = "3"
tag_subject = "4"
tag_text = "5"
tag_file = "6"
tag_newfile = "7"
tag_remfile = "8"
tag_commit = "10"
tag_to_nr = "11"
tag_save = "12"
tag_to_start = "13"




# callback
@dp.callback_query_handler(lambda c: True)
async def callback_func(query):

    global tag, to_delete_msg, menu_msg, record
    #cur_query = query
    tag = query.data   
    #menu_msg = query.message     

    if tag == tag_nr:
        #await query.message.reply(f"tag_nr") #{', '.join(files)}
        keyboard =  await request_keyboard()
        #await query.message.reply(f"keyboard") #{', '.join(files)}
        txt = request_menu()
        #await query.message.reply(f"request_menu") #{', '.join(files)}
        await edit_menu(query.message, request_menu(), await request_keyboard())
        #await query.message.reply(f"ku-ku {tag}") #{', '.join(files)}

    elif tag == tag_subject:
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_to_nr))
        await edit_menu(query.message, request_menu(), keyboard)
        to_delete_msg = await query.message.reply(f"enter subject")    

    elif tag == tag_to_nr:
        await delete_msg(to_delete_msg)
        await edit_menu(query.message, request_menu(), await request_keyboard())

    elif tag == tag_text:
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_to_nr))
        await edit_menu(query.message, request_menu(), keyboard)
        to_delete_msg = await query.message.reply(f"enter message")

    elif tag == tag_newfile:
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_to_nr))
        await edit_menu(query.message, request_menu(), keyboard)
        to_delete_msg = await query.message.reply(f"enter attachment")  

    elif tag == tag_commit:
        keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.row(   types.InlineKeyboardButton("send request", callback_data=tag_save),
                        types.InlineKeyboardButton("cancel", callback_data=tag_nr))
        await edit_menu(query.message, request_menu(), keyboard)
    
    elif tag == tag_save:
        # save 
        await edit_menu(query.message, 'Which operation do you want to make?', await start_keyboard())
    
    elif tag == tag_exit:
        await edit_menu(query.message, 'Goodbye! See you...', None)

    elif tag == tag_to_start:
        await edit_menu(query.message, 'Which operation do you want to make?', await start_keyboard())
    
    elif len(record.attachment) > 0:
        #await query.message.reply(f"ku-ku {tag}") #{', '.join(files)}
        tag_split = tag.split()        
        if len(tag_split) > 1 and tag_split[0] == tag_remfile:            
            record.attachment.remove(tag_split[1])
            await edit_menu(query.message, request_menu(), await request_keyboard())
  
    

# messages
async def delete_msg(message: types.Message):
    #await message.reply(f"ku-ku {tag}")
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=["text"])
async def start_handler(message: types.Message):
        global record, tag  #, cur_query
        #await message.reply(f"ku-ku {tag}")
        if tag == tag_subject:
            record.subject = message.text
            await delete_msg(message)
            await delete_msg(to_delete_msg)
            await edit_menu(menu_msg, request_menu(), await request_keyboard())
        if tag == tag_text:
            record.message = message.text
            await delete_msg(message)
            await delete_msg(to_delete_msg)
            await edit_menu(menu_msg, request_menu(), await request_keyboard())


@dp.message_handler(content_types=  ["audio", "document", "photo", "video", "video_note", "voice"])
async def start_handler(message: types.Message):
        global record, tag  #, cur_query
        #await message.reply(f"ku-ku {tag}")
        if tag == tag_newfile:
            record.attachment.append(f"{len(record.attachment) + 1}_{message.content_type}")
            await delete_msg(message)
            await delete_msg(to_delete_msg)
            await edit_menu(menu_msg, request_menu(), await request_keyboard())







if __name__ == '__main__':
    executor.start_polling(dp)





# https://www.tutorialspoint.com/sqlite/sqlite_python.htm

conn = sqlite3.connect('data.db')
#conn.close()

def get_requests(user):
    cursor = conn.execute("SELECT id, user, subject, message, attachment, status from requests")
    result = []
    for row in cursor:
        if row[1] == user:
            #               user, subject, text, files, status, id
            result.append(DBRecord(row[1],row[2],row[3],row[5].split(","),row[6],row[0]))
    return result

def put_request(request: DBRecord):
    conn.execute(f"INSERT INTO requests (id, user, subject, message, attachment, status) \
                VALUES ({request.id},{request.user},{request.subject},{request.message},{', '.join(record.attachment)},{request.status}) )");
    conn.commit()





# trash

# menues
# async def start_menu(message):
#     await edit_menu(message, 'Which operation do you want to make?', await start_keyboard())


# async def exit_menu(message):
#     await edit_menu(message, 'Goodbye! See you...', types.ReplyKeyboardRemove())

# async def new_request_header_menu(message):
#     await edit_menu(message, new_request_header(), await new_request_keyboard())

# async def files_menu(message):
#     #await message.reply(f"mu-mu")
#     keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    
#     keyboard.row(types.InlineKeyboardButton("add new", callback_data=tag_newfile))
#     for i in files:
#         keyboard.row(types.InlineKeyboardButton(f"remove {i}", callback_data=f'{tag_remfile}_{i}'))
#     keyboard.row(types.InlineKeyboardButton("cancel", callback_data=tag_nr))

#     await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
#                                 text=new_request_header(), reply_markup=keyboard)
