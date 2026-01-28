# -*- coding: utf-8 -*-
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from core import get_bot_reply

# Ambil token dari Railway Variables
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN belum diset di environment variable")

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo 👋\n"
        "Saya bot Grosir Cahya.\n\n"
        "Silakan tanya seputar:\n"
        "• Jam buka dan tutup\n"
        "• Lokasi toko\n"
        "• Barang yang tersedia\n"
    )

# Handler pesan biasa
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = get_bot_reply(user_text)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    print("🤖 Bot Telegram Grosir Cahya berjalan...")
    app.run_polling()

if __name__ == "__main__":
    main()
