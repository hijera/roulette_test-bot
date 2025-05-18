import random
from telegram import Update
from telegram.ext import ContextTypes
from config import STRAIGHT_UP, player_balances
from keyboards import get_bet_type_keyboard, get_number_keyboard
from logic import check_win, calculate_payout, update_balance

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    player_balances[user_id] = 100
    await update.message.reply_text(
        f"Добро пожаловать в игру Рулетка! Ваш начальный баланс: 100 кредитов.\n"
        f"Выберите тип ставки:",
        reply_markup=get_bet_type_keyboard()
    )

async def handle_bet_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "back_to_bet_types":
        await query.edit_message_text(
            text="Выберите тип ставки:",
            reply_markup=get_bet_type_keyboard()
        )
        return
    bet_type = query.data.split("_")[-1]
    context.user_data["current_bet_type"] = bet_type
    if bet_type == STRAIGHT_UP:
        await query.edit_message_text(
            text="Введите число от 0 до 36:",
            reply_markup=get_bet_type_keyboard()
        )
        context.user_data["waiting_for_number"] = True
    else:
        await query.edit_message_text(
            text=f"Выбран тип ставки: {bet_type}\nВыберите числа:",
            reply_markup=get_number_keyboard(bet_type)
        )

async def handle_number_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    bet_type = context.user_data.get("current_bet_type")
    if not bet_type:
        await query.edit_message_text(
            text="Ошибка: тип ставки не выбран. Начните сначала.",
            reply_markup=get_bet_type_keyboard()
        )
        return
    numbers = []
    if bet_type == STRAIGHT_UP:
        numbers = [int(query.data.split("_")[1])]
    elif bet_type == "split":
        nums = query.data.split("_")[1:]
        numbers = [int(n) for n in nums]
    elif bet_type == "street":
        nums = query.data.split("_")[1:]
        numbers = [int(n) for n in nums]
    elif bet_type == "corner":
        nums = query.data.split("_")[1:]
        numbers = [int(n) for n in nums]
    elif bet_type == "six_line":
        nums = query.data.split("_")[1:]
        numbers = [int(n) for n in nums]
    elif bet_type == "dozen":
        dozen = int(query.data.split("_")[1])
        numbers = list(range((dozen-1)*12 + 1, dozen*12 + 1))
    elif bet_type == "column":
        col = int(query.data.split("_")[1])
        numbers = [n for n in range(col, 37, 3)]
    elif bet_type == "even_odd":
        numbers = [query.data.split("_")[-1]]
    elif bet_type == "red_black":
        numbers = [query.data.split("_")[-1]]
    elif bet_type == "high_low":
        numbers = [query.data.split("_")[-1]]
    context.user_data["selected_numbers"] = numbers
    winning_number = random.randint(0, 36)
    win = check_win(bet_type, numbers, winning_number)
    payout = calculate_payout(bet_type, win)
    user_id = update.effective_user.id
    update_balance(user_id, payout)
    result_message = (
        f"Выпало число: {winning_number}\n"
        f"Ваша ставка: {bet_type}\n"
        f"Выбранные числа: {numbers}\n"
        f"Результат: {'Выигрыш' if win else 'Проигрыш'}\n"
        f"Выигрыш: {payout} кредитов\n"
        f"Ваш баланс: {player_balances[user_id]} кредитов"
    )
    await query.edit_message_text(
        text=result_message,
        reply_markup=get_bet_type_keyboard()
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("waiting_for_number"):
        return
    try:
        number = int(update.message.text)
        if 0 <= number <= 36:
            context.user_data["selected_numbers"] = [number]
            context.user_data["waiting_for_number"] = False
            winning_number = random.randint(0, 36)
            win = check_win(STRAIGHT_UP, [number], winning_number)
            payout = calculate_payout(STRAIGHT_UP, win)
            user_id = update.effective_user.id
            update_balance(user_id, payout)
            result_message = (
                f"Выпало число: {winning_number}\n"
                f"Ваша ставка: {STRAIGHT_UP}\n"
                f"Выбранное число: {number}\n"
                f"Результат: {'Выигрыш' if win else 'Проигрыш'}\n"
                f"Выигрыш: {payout} кредитов\n"
                f"Ваш баланс: {player_balances[user_id]} кредитов"
            )
            await update.message.reply_text(
                text=result_message,
                reply_markup=get_bet_type_keyboard()
            )
        else:
            await update.message.reply_text(
                "Пожалуйста, введите число от 0 до 36:",
                reply_markup=get_bet_type_keyboard()
            )
    except ValueError:
        await update.message.reply_text(
            "Пожалуйста, введите корректное число от 0 до 36:",
            reply_markup=get_bet_type_keyboard()
        ) 