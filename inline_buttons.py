from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="Функции виш-листов", callback_data="btn_wish_list", style="success"),InlineKeyboardButton(text="Функции минифигурок")],


])




wishlists_keyboard = InlineKeyboardMarkup(keyboard=[
[InlineKeyboardButton(text="Добавить виш-лист"),InlineKeyboardButton(text="Удалить виш-лист")],
[InlineKeyboardButton(text="Просмотр виш-листа")],
[InlineKeyboardButton(text="Главное меню")]



])

minifigures_keyboard = InlineKeyboardMarkup(keyboard=[
[InlineKeyboardButton(text="Добавить фигурку в виш-лист"),InlineKeyboardButton(text="Удалить фигурку из виш-листа")],
[InlineKeyboardButton(text="Главное меню")]



])

cansel = InlineKeyboardMarkup(keyboard=[
[InlineKeyboardButton(text="Отмена действия")]

])