# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# 🔗 Ambil logika chatbot dari core.py
from core import get_bot_reply

# 🔑 Ganti dengan TOKEN dari BotFather
TOKEN = "8482121566:AAFVdXo7KwZ977cCx-nEU3dbxTY7zBSEz40"

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋\n"
        "Saya bot grosir cahya .\n\n"
        "Silakan tanya seputar:\n"
        "- Jam bukan dan jam tutup\n"
        "- Lokasi toko\n"
        "- barang yang tersedia\n"
    )


# Menangani semua pesan teks
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    jawaban = get_bot_reply(user_text)  # 🔥 HUBUNG KE core.py
    await update.message.reply_text(jawaban)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("Bot Telegram grosir cahya sedang berjalan...")
    app.run_polling()


if __name__ == "__main__":
    main()