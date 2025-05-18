from config import STRAIGHT_UP, SPLIT, STREET, CORNER, SIX_LINE, DOZEN, COLUMN, EVEN_ODD, RED_BLACK, HIGH_LOW, PAYOUTS, RED_NUMBERS, player_balances

def check_win(bet_type, selected_numbers, winning_number):
    if bet_type in [STRAIGHT_UP, SPLIT, STREET, CORNER, SIX_LINE]:
        return winning_number in selected_numbers
    elif bet_type == DOZEN:
        dozen = (winning_number - 1) // 12 + 1
        return dozen in selected_numbers
    elif bet_type == COLUMN:
        return winning_number % 3 == selected_numbers[0] % 3
    elif bet_type == EVEN_ODD:
        if winning_number == 0:
            return False
        return (winning_number % 2 == 0) == (selected_numbers[0] == "even")
    elif bet_type == RED_BLACK:
        if winning_number == 0:
            return False
        return (winning_number in RED_NUMBERS) == (selected_numbers[0] == "red")
    elif bet_type == HIGH_LOW:
        if winning_number == 0:
            return False
        return (winning_number > 18) == (selected_numbers[0] == "high")
    return False

def calculate_payout(bet_type, win):
    if win:
        return PAYOUTS[bet_type]
    return -1

def get_balance(user_id):
    return player_balances.get(user_id, 0)

def update_balance(user_id, amount):
    player_balances[user_id] = player_balances.get(user_id, 0) + amount 