from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Mets ici ton NOUVEAU token BotFather
TOKEN = "8819045301:AAEj02pEZbsjRaHfX21vGSEe1ikGaQbOaLo"


def menu():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📱 Écrivez-moi sur WhatsApp",
                url="https://wa.me/237699486375"
            )
        ],

        [
            InlineKeyboardButton(
                "🚀 S'inscrire sur Earnlix Digital",
                url="https://earnlixdigital.com/register/michel11"
            )
        ]
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤖 *Bienvenue sur Earnlix Digital !*\n\n"
        "💰 Développe tes compétences en marketing d'affiliation.\n"
        "📚 Découvre des formations.\n"
        "🚀 Lance ton activité en ligne.\n\n"
        "👇 Choisis une option ci-dessous."
    )

    await update.message.reply_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=menu()
    )


async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Écrivez-moi directement sur WhatsApp :\n"
        "https://wa.me/237699486375"
    )


async def inscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💵 Inscription : 4 500 FCFA\n\n"
        "🚀 Clique ici :\n"
        "https://earnlixdigital.com/register/michel11"
    )


async def aide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\n"
        "/whatsapp\n"
        "/inscription\n"
        "/aide"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("whatsapp", whatsapp))
app.add_handler(CommandHandler("inscription", inscription))
app.add_handler(CommandHandler("aide", aide))

print("Bot lancé...")
app.run_polling()
