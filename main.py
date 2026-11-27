import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import BotCommand, FSInputFile
from random import choice
from random import randint,choice
from inline_buttons import main_inline_keyboard,wishlists_keyboard,minifigures_keyboard
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from data_baze import db_users
from wish_list_handlers import wish_lists_router
from minifigurs_handlers import minifigurs_router
from config import mybot
import os
from picture_utils import set_wish_list_image_name
from utils import get_directory_tree

mydispatcher = Dispatcher(storage=MemoryStorage())

@mydispatcher.message(F.text=="/info")
async def command_start(action):
    text = get_directory_tree(path="./")
    await action.answer(f"```\n{text}\n```", parse_mode="Markdown")
 

@mydispatcher.message(F.text=="/start")
async def command_start(action):
    user = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
    if user==None:
        os.mkdir(str(f"users_minifigures_photos/{action.from_user.id}"))
        os.mkdir(f"users_minifigures_photos/{action.from_user.id}/Любимое")
        set_wish_list_image_name("Любимое",f"users_minifigures_photos/{action.from_user.id}/Любимое/wishlist.png")
        user = {
            "tg_id": action.from_user.id,
            "wish_lists": [
                {
                    "name": "Любимое",
                    "minis": [
                    ]
                },
            ]
        }
        db_users.insert_one(user)
    await action.answer(f"Приветствую Вас, {action.from_user.first_name}\nВаш id: {action.from_user.id}")
    await action.answer(f"Главное меню",reply_markup=main_inline_keyboard)

# Домашнее задание:

# 1) Перевести главное меню на инлайн кнопки
# 2) Перевести меню функций фигурок на инлайн кнопки

@mydispatcher.callback_query(F.data == "btn_main_menu")
async def command_ping(action):
    await action.message.edit_text(f"Главное меню",reply_markup=main_inline_keyboard)



# --------------------------------МЕНЮ ФИГУРОК--------------------------------------
@mydispatcher.callback_query(F.data == "btn_minifigures")
async def command_ping(action):
    await action.message.edit_text(f"Функции минифигурок",reply_markup=minifigures_keyboard)
# --------------------------------КНОПОЧКИ ФИГУРОК----------------------------------








@mydispatcher.callback_query(F.data == "btn_cansel")
async def cansel(action,state: FSMContext):
    await state.clear()
    await action.message.edit_text(f"Отмена действия",reply_markup=main_inline_keyboard)



async def main():
    await commands_menu()
    mydispatcher.include_router(wish_lists_router)
    mydispatcher.include_router(minifigurs_router)
    await mydispatcher.start_polling(mybot)

async def commands_menu():
    menu = [
        BotCommand(command="/start",description="Запустить бота"),
    ]
    await mybot.set_my_commands(menu)


if __name__=="__main__":
    asyncio.run(main())
