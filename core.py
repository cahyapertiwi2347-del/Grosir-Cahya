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

    # Filter kata kasar
    if contains_bad_word(text):
        return (
            "🙏 Mohon gunakan bahasa yang sopan.\n\n"
            "Saya siap membantu info produk, jam buka, atau alamat toko 😊"
        )

    # Sapaan
    if any(s in text for s in ["halo", "hai", "assalamualaikum", "pagi", "siang", "sore", "malam"]):
        return (
            "Halo 👋 Selamat datang di Grosir Cahya.\n"
            "Silakan tanya tentang produk, jam buka, atau lokasi toko 😊"
        )

    # Cek FAQ
    for faq in FAQS:
        for kw in faq["keywords"]:
            if kw in text:
                return faq["answer"]

    # Fallback
    return (
        "Maaf, saya belum memahami pertanyaan tersebut 🤔\n\n"
        "Contoh pertanyaan:\n"
        "• Jam buka toko\n"
        "• Alamat toko\n"
        "• Produk yang dijual"
    )
