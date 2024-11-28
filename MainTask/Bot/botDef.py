from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
import os
from PDFModule.PDFChecker import PDFChecker
from PDFModule.QuestionsCheckerAI import QuestionsChecker
from PDFModule.PDFFile import PDF


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n'
                                    f"I'm a Reading Questions review bot.\n"
                                    f"I will try to help you improve your future grade and also point "
                                    f"out the flaws I saw in your work.\n"
                                    f"Write /help to learn how to use a bot",)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('To start checking your work write the /upload command and follow the instructions.'
                                    'Your RQ should match the following '
                                    '[template](https://drive.google.com/drive/folders/11hyrJl_fWnK9zqjehSj7tw_ImVztiGn-?usp=sharing)'
                                    ', if not, please change', parse_mode='Markdown')


# upload commands
RQ_NUM, FILE_UPLOAD = range(2)


async def upload_command(update, context):
    await update.message.reply_text('Please enter the Reading Question (RQ) number:')
    return RQ_NUM


async def rq_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['rqNumber'] = update.message.text
    if 0 < int(context.user_data['rqNumber']) < 8:
        await update.message.reply_text(
            f'Thank you! Now upload the file with your RQ assignment {context.user_data["rqNumber"]}. '
            f'If you made a mistake with the RQ number, write /cancel')
        return FILE_UPLOAD
    else:
        await update.message.reply_text('There is no such RQ number.')
        return ConversationHandler.END


async def gpt_checker_start(update, context):
    await update.message.reply_text('Now upload the file with your RQ assignment.'
                                    'If you made mistake, write /cancel.')
    return FILE_UPLOAD


async def gpt_checker_end(update, context):
    file = update.message.document
    if file and file.mime_type == 'application/pdf':
        await update.message.reply_text('Wait for checks...')

        fileId = file.file_id
        new_file = await context.bot.get_file(fileId)
        file_path = os.path.join('../MainTask/downloads', f"{file.file_name}")
        await new_file.download_to_drive(file_path)

        pdf_file = PDF(file_path, int(1))

        pdf_file.parsingQuestions()

        ai_checker = QuestionsChecker(pdf_file)

        res = ai_checker.gpt_generating_checking()

        os.remove(file_path)

        print(res)
        res = int(res)

        if res == 0:
            await update.message.reply_text('✅ Everything is fine!')
        elif res == 1:
            await update.message.reply_text('✅ Most likely your text has not been generated.')
        elif res == 2:
            await update.message.reply_text('⚠️ Your text may have been generated, try editing it.')
        elif res == 3:
            await update.message.reply_text('⛔ Your text has been generated, please edit it.')


async def file_upload(update, context):
    file = update.message.document
    if file and file.mime_type == 'application/pdf':
        await update.message.reply_text('Expect to be graded...')

        # Download the file
        fileId = file.file_id
        new_file = await context.bot.get_file(fileId)
        file_path = os.path.join('../MainTask/downloads', f"{file.file_name}")
        await new_file.download_to_drive(file_path)

        # Initialize PDFChecker and QuestionsChecker
        checkerFile = PDFChecker()
        pdf_file = PDF(file_path, int(context.user_data['rqNumber']))
        pdf_file.parsingQuestions()

        # Check the evaluation
        result = checkerFile.checkEv(pdf_file)
        print(result)

        for elem in result:
            await update.message.reply_text(elem)

        await update.message.reply_text("After reviewing your RQ check, take a short "
                                        "[survey](https://forms.gle/tP6tCpGYLze1E9tQ7) to improve"
                                        " the bot's performance", parse_mode='Markdown')

        os.remove(file_path)
    else:
        await update.message.reply_text('Please upload a file with the assignment or convert your file to PDFModule. ')
    return ConversationHandler.END


async def cancel(update: Update, context):
    await update.message.reply_text('Ok...')
    return ConversationHandler.END
