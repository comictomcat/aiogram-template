from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Creating an inline keyboard
source_markup = InlineKeyboardMarkup()

# Inserting the source code button with a specific url
source_markup.insert(InlineKeyboardButton('My Sources!', url='https://gitlab.com/comictomcat/aiogram-template'))
