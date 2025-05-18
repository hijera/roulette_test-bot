import os

# Словарь для хранения балансов игроков
player_balances = {}

# Константы для ставок
STRAIGHT_UP = "straight_up"  # Ставка на одно число
SPLIT = "split"  # Ставка на два числа
STREET = "street"  # Ставка на три числа
CORNER = "corner"  # Ставка на четыре числа
SIX_LINE = "six_line"  # Ставка на шесть чисел
DOZEN = "dozen"  # Ставка на дюжину
COLUMN = "column"  # Ставка на колонку
EVEN_ODD = "even_odd"  # Ставка на чет/нечет
RED_BLACK = "red_black"  # Ставка на красное/черное
HIGH_LOW = "high_low"  # Ставка на высокое/низкое

# Коэффициенты выигрыша
PAYOUTS = {
    STRAIGHT_UP: 35,
    SPLIT: 17,
    STREET: 11,
    CORNER: 8,
    SIX_LINE: 5,
    DOZEN: 2,
    COLUMN: 2,
    EVEN_ODD: 1,
    RED_BLACK: 1,
    HIGH_LOW: 1
}

# Красные числа на рулетке
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36} 