import os
import telebot
from telebot import types
# Assuming you have a file named fixes.py in the same directory
from fixes import FIXES

# FIXED: Assign the token directly as a string
BOT_TOKEN = "8689664926:AAFkgFbwGXwX0Iknl1VrXfs6OnEgBYf3b7I"

bot = telebot.TeleBot(BOT_TOKEN)

ITEMS_PER_PAGE = 8

hardware_errors = [
    "Laptop no power", "Laptop not charging", "Laptop no display",
    "Screen black but fan running", "Laptop overheating", "Laptop auto shutdown",
    "Laptop fan not spinning", "Laptop keyboard not working",
    "Laptop touchpad not working", "Broken screen / cracked display",
    "External monitor no signal", "Monitor flickering", "Monitor no power",
    "PC not turning on", "PC turns on then off immediately",
    "No POST (no beep, no display)", "Continuous beeping sound",
    "RAM not detected", "Faulty RAM (random crashes)", "Hard disk not detected",
    "HDD clicking noise", "SSD not recognized", "Slow hard disk performance",
    "CPU overheating", "CPU fan error", "GPU not detected", "GPU overheating",
    "No display from GPU", "Motherboard failure", "BIOS not booting",
    "CMOS battery dead", "USB port not working",
    "USB device not recognized (hardware)", "Power supply failure (PSU dead)",
    "Random restarts (hardware issue)", "Laptop battery draining fast",
    "Battery not detected", "Charger not working", "Loose charging port",
    "Speaker not working (hardware)", "No sound from speakers",
    "Headphone jack not working", "Webcam not working (hardware)",
    "Microphone not working (hardware)", "Ethernet port not working",
    "WiFi card failure", "Bluetooth not working (hardware)",
    "Overheating while charging", "Burning smell from PC",
    "Physical damage (water spill / shock)"
]

software_errors = [
    "Windows not booting", "Blue Screen of Death (BSOD)",
    "Windows stuck on loading screen", "Windows update failed",
    "Windows activation error", "Slow Windows performance",
    "System freeze / not responding", "App not opening", "Program crash",
    "Software installation failed", "Driver not installed", "Driver outdated",
    "Driver conflict", "WiFi connected but no internet",
    "Network limited access", "DNS error", "IP conflict",
    "Browser not loading pages", "Chrome not opening", "App keeps crashing",
    "High CPU usage", "High RAM usage", "Disk usage 100%",
    "Malware infection", "Virus detected", "Antivirus blocking apps",
    "File corrupted", "Missing DLL error", "Software license error",
    "Permission denied error", "Admin rights required error",
    "Windows explorer not responding", "Taskbar not working",
    "Start menu not working", "Sound not working (software)",
    "No audio output device installed", "Microphone not detected (software)",
    "Webcam not detected (software)", "Printer not printing",
    "Printer driver error", "Bluetooth not working (software)",
    "USB driver error", "Game not launching", "Game lag / low FPS",
    "Compatibility issue", "Update loop error", "Login error / password issue",
    "Sync error (cloud apps)", "Email not sending/receiving",
    "Software freezing randomly"
]


def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("🖥 Hardware Error", "💻 Software Error")
    markup.row("🔍 Search Error", "📞 Contact Technician")
    return markup


def error_menu(category, page=0):
    errors = hardware_errors if category == "hardware" else software_errors
    start = page * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    markup = types.InlineKeyboardMarkup(row_width=1)

    for index, err in enumerate(errors[start:end], start=start):
        emoji = "🔧" if category == "hardware" else "💻"
        markup.add(
            types.InlineKeyboardButton(
                f"{emoji} {err}",
                callback_data=f"fix|{category}|{index}"
            )
        )

    nav_buttons = []

    if page > 0:
        nav_buttons.append(
            types.InlineKeyboardButton("⬅️ Previous", callback_data=f"page|{category}|{page-1}")
        )

    if end < len(errors):
        nav_buttons.append(
            types.InlineKeyboardButton("Next ➡️", callback_data=f"page|{category}|{page+1}")
        )

    if nav_buttons:
        markup.row(*nav_buttons)

    markup.add(types.InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu"))

    return markup


@bot.message_handler(commands=["start", "menu"])
def start(message):
    bot.send_message(
        message.chat.id,
        """
👋 မင်္ဂလာပါ!

🛠 ဒီ Bot က Computer / Laptop Error တွေကို
Step-by-step ဖြေရှင်းပေးတဲ့ Troubleshooting Bot ပါ။

✅ Hardware Error
✅ Software Error
✅ Search Error
✅ Technician Contact

အောက်က menu ကနေ ရွေးပါ 👇
""",
        reply_markup=main_menu()
    )


@bot.message_handler(func=lambda m: m.text == "🖥 Hardware Error")
def show_hardware(message):
    bot.send_message(
        message.chat.id,
        "🔧 Hardware Error အမျိုးအစားကို ရွေးပါ:",
        reply_markup=error_menu("hardware", 0)
    )


@bot.message_handler(func=lambda m: m.text == "💻 Software Error")
def show_software(message):
    bot.send_message(
        message.chat.id,
        "💻 Software Error အမျိုးအစားကို ရွေးပါ:",
        reply_markup=error_menu("software", 0)
    )


@bot.message_handler(func=lambda m: m.text == "🔍 Search Error")
def ask_search(message):
    msg = bot.send_message(
        message.chat.id,
        "🔍 Error name ကိုရေးပါ။\n\nဥပမာ: `RAM`, `WiFi`, `Blue Screen`, `Printer`",
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(msg, search_error)


def search_error(message):
    keyword = message.text.lower()

    all_errors = []
    for err in hardware_errors:
        all_errors.append(("hardware", err))
    for err in software_errors:
        all_errors.append(("software", err))

    results = [(cat, err) for cat, err in all_errors if keyword in err.lower()]

    if not results:
        bot.send_message(
            message.chat.id,
            "❌ Search result မတွေ့ပါ။\n\n/menu နှိပ်ပြီး ပြန်စပါ။",
            reply_markup=main_menu()
        )
        return

    markup = types.InlineKeyboardMarkup(row_width=1)

    for cat, err in results[:10]:
        errors = hardware_errors if cat == "hardware" else software_errors
        index = errors.index(err)
        emoji = "🔧" if cat == "hardware" else "💻"
        markup.add(
            types.InlineKeyboardButton(
                f"{emoji} {err}",
                callback_data=f"fix|{cat}|{index}"
            )
        )

    markup.add(types.InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu"))

    bot.send_message(
        message.chat.id,
        f"🔎 `{message.text}` အတွက်တွေ့ရှိထားသော results:",
        parse_mode="Markdown",
        reply_markup=markup
    )


@bot.message_handler(func=lambda m: m.text == "📞 Contact Technician")
@bot.message_handler(commands=["contact"])
def contact(message):
    bot.send_message(
        message.chat.id,
        """
📞 Technician Contact

Error မဖြေရှင်းနိုင်သေးရင် ဆက်သွယ်ပါ။

👨‍🔧 Telegram: @gafvkk
🕒 Support: 9 AM - 6 PM
""",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    data = call.data.split("|")

    if call.data == "main_menu":
        bot.send_message(
            call.message.chat.id,
            "🏠 Main Menu ပြန်ဖွင့်လိုက်ပါ:",
            reply_markup=main_menu()
        )
        bot.answer_callback_query(call.id)
        return

    if data[0] == "page":
        category = data[1]
        page = int(data[2])

        title = "🔧 Hardware Error List" if category == "hardware" else "💻 Software Error List"

        bot.edit_message_text(
            title,
            call.message.chat.id,
            call.message.message_id,
            reply_markup=error_menu(category, page)
        )
        bot.answer_callback_query(call.id)
        return

    if data[0] == "fix":
        category = data[1]
        index = int(data[2])

        errors = hardware_errors if category == "hardware" else software_errors
        error = errors[index]

        fix_text = FIXES.get(error)

        if fix_text:
            bot.send_message(
                call.message.chat.id,
                f"✅ *Selected Error:*\n`{error}`\n\n{fix_text}",
                parse_mode="Markdown"
            )
            bot.send_message(
                call.message.chat.id,
                "❓ အဆင်ပြေလား?\n\nမရသေးရင် 📞 Contact Technician ကိုနှိပ်ပါ။",
                reply_markup=main_menu()
            )
        else:
            bot.send_message(
                call.message.chat.id,
                f"""
❌ ဒီ Error အတွက် fix data မရှိသေးပါ။

Selected Error:
`{error}`

fixes.py ထဲမှာ ဒီ error အတွက် solution ထည့်ရန်လိုအပ်ပါတယ်။
""",
                parse_mode="Markdown",
                reply_markup=main_menu()
            )

        bot.answer_callback_query(call.id)


@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(
        message.chat.id,
        "နားမလည်ပါဘူး။ /menu နှိပ်ပြီး menu ပြန်ဖွင့်ပါ။",
        reply_markup=main_menu()
    )


print("✅ Bot is running...")
bot.infinity_polling()
