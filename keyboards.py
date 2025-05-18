from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import STRAIGHT_UP, SPLIT, STREET, CORNER, SIX_LINE, DOZEN, COLUMN, EVEN_ODD, RED_BLACK, HIGH_LOW

def get_bet_type_keyboard():
    keyboard = [
        [InlineKeyboardButton("Одно число (x35)", callback_data=f"bet_type_{STRAIGHT_UP}")],
        [InlineKeyboardButton("Два числа (x17)", callback_data=f"bet_type_{SPLIT}"),
         InlineKeyboardButton("Три числа (x11)", callback_data=f"bet_type_{STREET}")],
        [InlineKeyboardButton("Четыре числа (x8)", callback_data=f"bet_type_{CORNER}"),
         InlineKeyboardButton("Шесть чисел (x5)", callback_data=f"bet_type_{SIX_LINE}")],
        [InlineKeyboardButton("Дюжина (x2)", callback_data=f"bet_type_{DOZEN}"),
         InlineKeyboardButton("Колонка (x2)", callback_data=f"bet_type_{COLUMN}")],
        [InlineKeyboardButton("Чет/Нечет (x1)", callback_data=f"bet_type_{EVEN_ODD}"),
         InlineKeyboardButton("Красное/Черное (x1)", callback_data=f"bet_type_{RED_BLACK}")],
        [InlineKeyboardButton("Высокое/Низкое (x1)", callback_data=f"bet_type_{HIGH_LOW}")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_number_keyboard(bet_type):
    keyboard = []
    if bet_type == STRAIGHT_UP:
        for i in range(0, 37, 10):
            row = []
            for j in range(10):
                if i + j < 37:
                    row.append(InlineKeyboardButton(str(i + j), callback_data=f"number_{i + j}"))
            keyboard.append(row)
    elif bet_type == SPLIT:
        for i in range(0, 36, 3):
            row = []
            for j in range(3):
                if i + j < 36:
                    row.append(InlineKeyboardButton(f"{i+j}-{i+j+1}", callback_data=f"split_{i+j}_{i+j+1}"))
            keyboard.append(row)
    elif bet_type == STREET:
        for i in range(0, 36, 3):
            row = []
            for j in range(3):
                if i + j < 34:
                    row.append(InlineKeyboardButton(f"{i+j}-{i+j+1}-{i+j+2}", callback_data=f"street_{i+j}_{i+j+1}_{i+j+2}"))
            keyboard.append(row)
    elif bet_type == CORNER:
        for i in range(0, 32, 3):
            row = []
            for j in range(3):
                base = i + j
                if base % 3 < 2 and base + 3 < 36:
                    nums = [base, base + 1, base + 3, base + 4]
                    label = f"{nums[0]}-{nums[1]}-{nums[2]}-{nums[3]}"
                    callback = f"corner_{nums[0]}_{nums[1]}_{nums[2]}_{nums[3]}"
                    row.append(InlineKeyboardButton(label, callback_data=callback))
            if row:
                keyboard.append(row)
    elif bet_type == SIX_LINE:
        for i in range(0, 33, 3):
            row = []
            for j in range(3):
                if i + j < 31:
                    nums = [i+j, i+j+1, i+j+2, i+j+3, i+j+4, i+j+5]
                    row.append(InlineKeyboardButton(f"{nums[0]}-{nums[1]}-{nums[2]}-{nums[3]}-{nums[4]}-{nums[5]}", 
                                                  callback_data=f"six_line_{nums[0]}_{nums[1]}_{nums[2]}_{nums[3]}_{nums[4]}_{nums[5]}"))
            keyboard.append(row)
    elif bet_type == DOZEN:
        keyboard = [
            [InlineKeyboardButton("1-12", callback_data="dozen_1")],
            [InlineKeyboardButton("13-24", callback_data="dozen_2")],
            [InlineKeyboardButton("25-36", callback_data="dozen_3")]
        ]
    elif bet_type == COLUMN:
        keyboard = [
            [InlineKeyboardButton("1-4-7-...-34", callback_data="column_0")],
            [InlineKeyboardButton("2-5-8-...-35", callback_data="column_1")],
            [InlineKeyboardButton("3-6-9-...-36", callback_data="column_2")]
        ]
    elif bet_type == EVEN_ODD:
        keyboard = [
            [InlineKeyboardButton("Чет", callback_data="even_odd_even")],
            [InlineKeyboardButton("Нечет", callback_data="even_odd_odd")]
        ]
    elif bet_type == RED_BLACK:
        keyboard = [
            [InlineKeyboardButton("Красное", callback_data="red_black_red")],
            [InlineKeyboardButton("Черное", callback_data="red_black_black")]
        ]
    elif bet_type == HIGH_LOW:
        keyboard = [
            [InlineKeyboardButton("1-18", callback_data="high_low_low")],
            [InlineKeyboardButton("19-36", callback_data="high_low_high")]
        ]
    keyboard.append([InlineKeyboardButton("« Назад", callback_data="back_to_bet_types")])
    return InlineKeyboardMarkup(keyboard) 