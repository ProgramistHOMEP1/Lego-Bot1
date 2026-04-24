import asyncio
from aiogram import Router, F
from aiogram.types import BotCommand, FSInputFile
from random import choice
from random import randint,choice
from buttons import glavnie_knopotki,funkcii_vish_list,funkcii_figurki
import pymongo
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from data_baze import db_users,States
import os
import shutil
from picture_utils import set_wish_list_image_name
wish_lists_router = Router()
# -------------------------------МЕНЮ ВИШ-ЛИСТОВ------------------------------------
@wish_lists_router.message(F.text=="Функции виш-листов")
async def command_ping(action):
    user = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
    names = ""
    for wish_list in user["wish_lists"]:
        names =  names + f"- `{wish_list['name']}` \n"
    await action.answer(f"Ваши виш-листы: \n\n{names}",reply_markup=funkcii_vish_list,parse_mode="Markdown")
#
# -------------------------------КНОПОЧКИ ВИШ-ЛИСТОВ--------------------------------
# ---------------------------------------------------------------Добавление виш-листа--------------------------------------------------------------
@wish_lists_router.message(F.text=="Добавить виш-лист")
async def command_ping(action,state: FSMContext):
    await action.answer(f"Введите название Вашего нового виш-листа",reply_markup=funkcii_vish_list)
    await state.set_state(States.waiting_wishlist_name_to_add)

@wish_lists_router.message(States.waiting_wishlist_name_to_add)
async def process_name(action,state: FSMContext):
    rezult = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
    
    for wish_list in rezult["wish_lists"]:
        if wish_list["name"]==action.text:
            await action.answer(f"Введите новое название для вашего виш-листа, такое название уже есть!",reply_markup=funkcii_vish_list)
            return 0
    rezult["wish_lists"].append({'name': action.text, 'minis': []})
    new_wish_lists = (rezult["wish_lists"])
    db_users.update_many(
        filter={
            "tg_id": action.from_user.id
        },
        update={
            "$set":{
                "wish_lists": new_wish_lists
            }
        }
    )
    names = ""
    for wish_list in new_wish_lists:
        names =  names + f"- `{wish_list['name']}` \n"
    os.mkdir(f"users_minifigures_photos/{action.from_user.id}/{action.text}")
    set_wish_list_image_name(action.text,f"users_minifigures_photos/{action.from_user.id}/{action.text}/wishlist.png")
    await action.answer(f"*Виш-лист с названием '{action.text}' добавлен!*\n*Ваши виш-листы:* \n\n{names}",reply_markup=funkcii_vish_list,parse_mode="Markdown")
    await state.clear()
# ---------------------------------------------------------------------Удаление виш-листа----------------------------------------------------------
@wish_lists_router.message(F.text=="Удалить виш-лист")
async def command_ping(action,state: FSMContext):
    await action.answer(f"Введите название виш-листа который хотите удалить",reply_markup=funkcii_vish_list)
    await state.set_state(States.waiting_wishlist_name_to_delete)


@wish_lists_router.message(States.waiting_wishlist_name_to_delete)
async def process_name(action,state: FSMContext):
    shutil.rmtree(f"users_minifigures_photos/{action.from_user.id}/{action.text}")
# --------Поиск пользователя---------
    user = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
# -------------Само удалиние-------------
    find_wish_list = ""
    for wish_list in user["wish_lists"]:
        if wish_list["name"]==action.text:
            find_wish_list = wish_list
            break
    if find_wish_list=="":
            await action.answer_photo(FSInputFile("Sistemimages/Обезьянкасреднийпалец.jpg"),caption="Пиши грамотно, балбес!",reply_markup=funkcii_vish_list)
            return None
    user["wish_lists"].remove(find_wish_list)
# ------------Запись новой версии виш-листов------------
    db_users.update_many(
        filter={
            "tg_id": action.from_user.id
        },
        update={
            "$set":{
                "wish_lists": user["wish_lists"]
            }
        }
    )
    names = ""
    for wish_list in user["wish_lists"]:
        names =  names + f"- `{wish_list['name']}` \n"
    await action.answer(f"*Виш-лист с названием '{action.text}' удален!*\n*Ваши виш-листы:* \n\n{names}",reply_markup=funkcii_vish_list,parse_mode="Markdown")
    await state.clear()
# Домашнее задание:
# Сделать кнопку "Просмотр вишлистов"
# По нажатию будут отображен список с названиями вишлистов (ТОЧНО ТАКОЙ ЖЕ, как у тебя уже и так 
# отображается при заходе в меню вишлистов - просто скопируй код)
# Только в конец сообщения добавь текст "Введите названия вишлиста для просмотра"

@wish_lists_router.message(F.text=="Просмотр виш-листа")
async def command_ping(action,state: FSMContext):
    await action.answer(f"Просмотр виш-листа",reply_markup=funkcii_vish_list)
    user = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
    names = ""
    for wish_list in user["wish_lists"]:
        names =  names + f"- `{wish_list['name']}` \n"
    await action.answer(f"Ваши виш-листы: \n\n{names}\nВведите название виш-листа который хотите просмотреть",reply_markup=funkcii_vish_list,parse_mode="Markdown")
    await state.set_state(States.waiting_wishlist_name_to_check)

@wish_lists_router.message(States.waiting_wishlist_name_to_check)
async def process_name(action,state: FSMContext):
    user = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
    is_wish_list_exists = False
    for wish_list in user["wish_lists"]:
        if wish_list["name"]==action.text:
            is_wish_list_exists = True
    
    if is_wish_list_exists==False:
        await action.answer(f"Извините, такого виш-листа не существует!",reply_markup=funkcii_vish_list)
    else:
        await action.answer_photo(FSInputFile(f"users_minifigures_photos/{action.from_user.id}/{action.text}/wishlist.png",reply_markup=funkcii_vish_list))
        await state.clear()
# await action.answer_photo(FSInputFile("Sistemimages/Обезьянкасреднийпалец.jpg")