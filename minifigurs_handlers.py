import asyncio
from aiogram import Router, F
from aiogram.types import BotCommand, FSInputFile
from aiogram import types
from random import choice
from random import randint,choice
from buttons import glavnie_knopotki,funkcii_vish_list,funkcii_figurki
import pymongo
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from data_baze import db_users,States
from pprint import pprint
from config import mybot
import os
from picture_utils import crop_to_rectangle, paste_picture_to_wishlist

minifigurs_router = Router()

@minifigurs_router.message(F.text=="Добавить фигурку в виш-лист")
async def process_name(action,state: FSMContext):
    await action.answer(f"Выберите виш-лист в который хотите добавить минифигурку",reply_markup=funkcii_figurki)
    user = db_users.find_one(filter={
        "tg_id": action.from_user.id
    })
    names = ""
    for wish_list in user["wish_lists"]:
        names =  names + f"- `{wish_list['name']}` \n"
    await action.answer(f"Ваши виш-листы: \n\n{names}",reply_markup=funkcii_figurki,parse_mode="Markdown")
    await state.set_state(States.waiting_wishlist_name_to_add_minifigure)

@minifigurs_router.message(States.waiting_wishlist_name_to_add_minifigure)
async def process_name(action,state: FSMContext):
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
            await action.answer_photo(FSInputFile("Sistemimages/Обезьянкасреднийпалец.jpg"),caption="Пеши граматно, балбес!")
            return None
    await action.answer(f"Отправьте фотографию минифигурки, которую хотите добавить в виш-лист «{action.text}»",reply_markup=funkcii_figurki)
    await state.set_state(States.waiting_minifigure_picture_to_add)
    await state.update_data(wish_list_name=action.text)

@minifigurs_router.message(States.waiting_minifigure_picture_to_add)
async def process_name(action,state: FSMContext):
    minifigure_photo = (action.photo[-1])
    pprint(minifigure_photo)
    user_picture = await mybot.get_file(minifigure_photo.file_id)
    full_data = await state.get_data()
    number_my_pic = len(os.listdir(f"users_minifigures_photos/{action.from_user.id}/{full_data['wish_list_name']}"))
    await mybot.download_file(user_picture.file_path,f"users_minifigures_photos/{action.from_user.id}/{full_data['wish_list_name']}/{number_my_pic}.png")
    crop_to_rectangle(source_picture_path=f"users_minifigures_photos/{action.from_user.id}/{full_data['wish_list_name']}/{number_my_pic}.png", result_picture_path=f"users_minifigures_photos/{action.from_user.id}/{full_data['wish_list_name']}/{number_my_pic}.png")

    paste_picture_to_wishlist(
        path_to_picture=f"users_minifigures_photos/{action.from_user.id}/{full_data['wish_list_name']}/{number_my_pic}.png",
        number=number_my_pic,
        path_to_wishlist=f"users_minifigures_photos/{action.from_user.id}/{full_data['wish_list_name']}/wishlist.png")

    await state.clear()
    await action.answer(f"Минифигурка успешно добавлена в виш-лист «{full_data['wish_list_name']}»! ")