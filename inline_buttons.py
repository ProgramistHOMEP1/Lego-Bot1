from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="Функции виш-листов", callback_data="btn_wish_lists"),InlineKeyboardButton(text="Функции минифигурок", callback_data="btn_minifigures")],


])




wishlists_keyboard = InlineKeyboardMarkup(keyboard=[
[InlineKeyboardButton(text="Добавить виш-лист", callback_data="btn_add_wishlist", style="success"),InlineKeyboardButton(text="Удалить виш-лист", callback_data="btn_delete_wishlist", style="danger")],
[InlineKeyboardButton(text="Просмотр виш-листа", callback_data="btn_check_wishlist", style="primary")],
[InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu")]



])

minifigures_keyboard = InlineKeyboardMarkup(keyboard=[
[InlineKeyboardButton(text="Добавить фигурку в виш-лист", callback_data="btn_add_minifigure_to_wishlist", style="success"),InlineKeyboardButton(text="Удалить фигурку из виш-листа", callback_data="btn_delete_minifigure_from_wishlist", style="danger")],
[InlineKeyboardButton(text="Главное меню", callback_data="btn_main_menu")]



])

cansel = InlineKeyboardMarkup(keyboard=[
[InlineKeyboardButton(text="Отмена действия", callback_data="btn_cansel")]

])