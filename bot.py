from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8704293303:AAE1nlIFVXAMW7OGm1Jgebcj59dOmvVuCKY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 به Pixsim خوش آمدید 🎬")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
