import pymongo
from aiogram.fsm.state import State, StatesGroup
from config import mongo_port
client = pymongo.MongoClient("localhost",mongo_port)
db = client["Lego-Bot"]
db_users = db["Users"]



class States(StatesGroup):
    waiting_wishlist_name_to_add = State()
    waiting_wishlist_name_to_delete = State()
    waiting_wishlist_name_to_add_minifigure =  State()
    waiting_wishlist_name_to_delite_minifigure =  State()
    waiting_minifigure_picture_to_add =  State()
    waiting_wishlist_name_to_check = State()
    waiting_wishlist_name_to_delite_minifigure = State()
    waiting_minifigure_number_to_delite = State()