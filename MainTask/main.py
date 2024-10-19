from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from botDef import *


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("start", hello))
    app.add_handler(CommandHandler("help", help))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('upload', upload_command)],
        states={
            RQ_NUM: [MessageHandler(filters.TEXT & ~filters.COMMAND, rq_numbers)],
            FILE_UPLOAD: [MessageHandler(filters.Document.ALL, file_upload)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    app.add_handler(conv_handler)

    app.run_polling()



