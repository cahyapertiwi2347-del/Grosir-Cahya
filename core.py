import json
from pathlib import Path
import re

BASE_DIR = Path(__file__).resolve().parent
FAQ_FILE = BASE_DIR / "faq_toko.json"

with FAQ_FILE.open("r", encoding="utf-8") as f:
    DATA = json.load(f)

FAQS = DATA["faq"]
BAD_WORDS = DATA["bad_words"]


def contains_bad_word(text: str) -> bool:
    text = text.lower()
    for word in BAD_WORDS:
        if re.search(rf"\b{re.escape(word)}\b", text):
            return True
    return False


def get_bot_reply(user_message: str) -> str:
    text = (user_message or "").lower().strip()

    # 1️⃣ Filter kata kasar
    if contains_bad_word(text):
        return (
            "🙏 Mohon maaf, kami tidak dapat memproses pesan dengan bahasa kasar.\n\n"
            "Kami siap membantu dengan senang hati jika menggunakan bahasa yang sopan 😊\n"
            "Silakan tanyakan tentang produk, jam buka, atau cara order."
        )

    # 2️⃣ Sapaan
    if any(s in text for s in ["halo", "hai", "assalamualaikum", "pagi", "siang", "sore", "malam"]):
        return (
            "Halo 👋 Selamat datang di Toko Grosir cahya\n"
            "Silakan tanyakan seputar produk, jam operasional, alamat, atau cara order 😊"
        )

    # 3️⃣ Cek FAQ (keyword matching)
    for faq in FAQS:
        for kw in faq["keywords"]:
            if kw in text:
                return faq["answer"]

    # 4️⃣ Fallback cerdas
    return (
        "Maaf, saya belum memahami pertanyaan tersebut 🤔\n\n"
        "Coba tanyakan dengan kata lain, misalnya:\n"
        "• Jam buka toko\n"
        "• Produk yang dijual\n"
        "• Cara order\n"
        "• Alamat toko"
    )