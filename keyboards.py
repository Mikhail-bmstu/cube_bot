from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_start = KeyboardButton("Бросай кости!")
kb_start = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start)

button_end = KeyboardButton("Не хочу больше играть!!!")
button_hard = KeyboardButton("Cложность \"+\"")
button_easy = KeyboardButton("Cложность \"-\"")


kb_easy = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start).add(button_hard).add(button_end)
kb_hard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start).add(button_easy).add(button_end)
kb_main = ReplyKeyboardMarkup(resize_keyboard=True).add(button_start)\
    .row(button_easy, button_hard).add(button_end)