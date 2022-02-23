from aiogram import Bot, Dispatcher, executor, types

from word_list import WordList
import config
import logging
import keyboards as kb
import random

# log level
logging.basicConfig(level=logging.INFO)

# bot int
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
jokes = WordList()
player_cheat = 4


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Короче, Меченый\nСейчас будем играть в кости, благородства не будет!\n"
                         "Чтобы узнать правила пиши /help ;)", reply_markup=kb.kb_start)


@dp.message_handler(commands=['help'])
async def process_help_cmd(message: types.Message):
    await message.answer("В этой игре будем соревноваться: у кого выпадет больше число"
                         " от 4 до 24 (четыре игральных кубика)\n Хайпанем?", reply_markup=kb.kb_start)


@dp.message_handler(content_types=['text'], text='Бросай кости!')
async def start_game(message: types.Message):
    global player_cheat
    player_num = random.randint(player_cheat, 24)
    bot_num = random.randint(4, 24)
    keyboard = kb.kb_main
    if player_cheat == 4:
        keyboard = kb.kb_hard
    elif player_cheat == 20:
        keyboard = kb.kb_easy

    await message.answer(f"Мне выпало: {bot_num}\nТебе выпало: {player_num}")
    if player_num < bot_num:
        await message.answer(random.choice(jokes.win_lst), reply_markup=keyboard)
    elif player_num > bot_num:
        await message.answer(random.choice(jokes.lose_lst), reply_markup=keyboard)
    else:

        await message.answer("Ничья", reply_markup=keyboard)


@dp.message_handler(content_types=['text'], text='Не хочу больше играть!!!')
async def end_game(message: types.Message):
    global player_cheat
    player_cheat = 4
    await message.answer("Давай до свидания", reply_markup=kb.kb_start)


@dp.message_handler(content_types=['text'], text='Cложность \"+\"')
async def diff_up(message: types.Message):
    global player_cheat
    if player_cheat > 4:
        player_cheat -= 4
        await message.reply(f"Готово\nТекущий уровень сложности {6 - int(player_cheat * 0.25)} из 5")
    else:
        await message.reply("Уже максимальная сложность, теперь мы на равных\nЧистый рандом!!!", reply_markup=kb.kb_hard)


@dp.message_handler(content_types=['text'], text='Cложность \"-\"')
async def diff_down(message: types.Message):
    global player_cheat
    if player_cheat < 20:
        player_cheat += 4
        await message.reply(f"Готово\nТекущий уровень сложности {6 -int(player_cheat * 0.25)} из 5")
    else:
        await message.reply("Уже минимальная сложность! Куда тебе еще легче, жулик?", reply_markup=kb.kb_easy)


@dp.message_handler(content_types=['text'])
async def cash(message: types.Message):
    await message.answer("Нажимай только на кнопки специальной клавиатуры, я других слов не понимаю!\n"
                         "чтобы начать пиши /start")

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
