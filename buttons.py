from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

glavnie_knopotki = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
[KeyboardButton(text="Функции виш-листов"),KeyboardButton(text="Функции минифигурок")],


])

funkcii_vish_list = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
[KeyboardButton(text="Добавить виш-лист"),KeyboardButton(text="Удалить виш-лист")],
[KeyboardButton(text="Просмотр виш-листа")],
[KeyboardButton(text="Главное меню")]



])

funkcii_figurki = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
[KeyboardButton(text="Добавить фигурку в виш-лист"),KeyboardButton(text="Удалить фигурку из виш-листа")],
[KeyboardButton(text="Главное меню")]



])