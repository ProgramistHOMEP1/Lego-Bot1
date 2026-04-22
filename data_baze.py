import pymongo
from aiogram.fsm.state import State, StatesGroup
client = pymongo.MongoClient("localhost",port=27017)
db = client["Lego-Bot"]
db_users = db["Users"]

class States(StatesGroup):
    waiting_wishlist_name_to_add = State()
    waiting_wishlist_name_to_delete = State()
    waiting_wishlist_name_to_add_minifigure =  State()
    waiting_wishlist_name_to_delite_minifigure =  State()
    waiting_minifigure_picture_to_add =  State()
    waiting_wishlist_name_to_check = State()