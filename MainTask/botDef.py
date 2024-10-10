from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters, ConversationHandler


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n'
                                    f"I'm a Reading Questions review bot.\n"
                                    f"I will try to help you improve your future grade and also point "
                                    f"out the flaws I saw in your work.")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('To start checking your work write the /upload command and follow the instructions')


# upload commands
RQ_NUM, FILE_UPLOAD = range(2)


async def upload_command(update, context):
    await update.message.reply_text('Please enter the Reading Question (RQ) number:')
    return RQ_NUM


async def rq_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data['rqNumber'] = update.message.text
    await update.message.reply_text(
        f'Thank you! Now upload the file with your RQ assignment {context.user_data["rqNumber"]}.')
    return FILE_UPLOAD


async def file_upload(update, context):
    file = update.message.document
    if file:
        file_id = file.file_id
        await update.message.reply_text('Expect to be graded...')
        # checking RQ
        await update.message.reply_text('Your comment: "It will be soon"\n'
                                  'Your grade: "It will be soon"\n'
                                  'You are sunshine!')
    else:
        await update.message.reply_text('Please upload a file with the assignment.')
    return ConversationHandler.END


async def cancel(update: Update, context):
    await update.message.reply_text('Ok...')
    return ConversationHandler.END
