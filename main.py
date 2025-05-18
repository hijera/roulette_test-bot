import os
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from dotenv import load_dotenv
from handlers import start, handle_bet_type, handle_number_selection, handle_message

def main():
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("Не найден токен Telegram бота. Убедитесь, что файл .env существует и содержит TELEGRAM_TOKEN")
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_bet_type, pattern="^bet_type_"))
    application.add_handler(CallbackQueryHandler(handle_number_selection, pattern="^(split|street|corner|six_line|dozen|column|even_odd|red_black|high_low|back_to_bet_types)"))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main() 