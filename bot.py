import telebot
from telebot import types
from fixes import FIXES  

# Replace with your actual Bot Token
bot = telebot.TeleBot("8689664926:AAFkgFbwGXwX0Iknl1VrXfs6OnEgBYf3b7I")

# ===== STEP 1: Start Handler =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🖥 Hardware Error", "💻 Software Error")

    bot.send_message(message.chat.id, """
👋 Welcome

💡 Tip:
PC problem တစ်ခုဖြစ်တိုင်း ဒီ bot ကိုသုံးနိုင်ပါတယ်

🔁 /menu နှိပ်ပြီးစတင်ပါ
""", reply_markup=markup)

# ===== STEP 2: Menu Handler =====
@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🖥 Hardware Error", "💻 Software Error")

    bot.send_message(
        message.chat.id,
        "🔁 Menu ပြန်ဖွင့်လိုက်ပါ:",
        reply_markup=markup
    )

# ===== STEP 3: Hardware & Software Lists =====
hardware_errors = [
    "Laptop no power",
    "Laptop not charging",
    "Laptop no display",
    "Screen black but fan running",
    "Laptop overheating",
    "Laptop auto shutdown",
    "Laptop fan not spinning",
    "Laptop keyboard not working",
    "Laptop touchpad not working",
    "Broken screen / cracked display",
    "External monitor no signal",
    "Monitor flickering",
    "Monitor no power",
    "PC not turning on",
    "PC turns on then off immediately",
    "No POST (no beep, no display)",
    "Continuous beeping sound",
    "RAM not detected",
    "Faulty RAM (random crashes)",
    "Hard disk not detected",
    "HDD clicking noise",
    "SSD not recognized",
    "Slow hard disk performance",
    "CPU overheating",
    "CPU fan error",
    "GPU not detected",
    "GPU overheating",
    "No display from GPU",
    "Motherboard failure",
    "BIOS not booting",
    "CMOS battery dead",
    "USB port not working",
    "USB device not recognized (hardware)",
    "Power supply failure (PSU dead)",
    "Random restarts (hardware issue)",
    "Laptop battery draining fast",
    "Battery not detected",
    "Charger not working",
    "Loose charging port",
    "Speaker not working (hardware)",
    "No sound from speakers",
    "Headphone jack not working",
    "Webcam not working (hardware)",
    "Microphone not working (hardware)",
    "Ethernet port not working",
    "WiFi card failure",
    "Bluetooth not working (hardware)",
    "Overheating while charging",
    "Burning smell from PC",
    "Physical damage (water spill / shock)"
]

software_errors = [
    "Windows not booting",
    "Blue Screen of Death (BSOD)",
    "Windows stuck on loading screen",
    "Windows update failed",
    "Windows activation error",
    "Slow Windows performance",
    "System freeze / not responding",
    "App not opening",
    "Program crash",
    "Software installation failed",
    "Driver not installed",
    "Driver outdated",
    "Driver conflict",
    "WiFi connected but no internet",
    "Network limited access",
    "DNS error",
    "IP conflict",
    "Browser not loading pages",
    "Chrome not opening",
    "App keeps crashing",
    "High CPU usage",
    "High RAM usage",
    "Disk usage 100%",
    "Malware infection",
    "Virus detected",
    "Antivirus blocking apps",
    "File corrupted",
    "Missing DLL error",
    "Software license error",
    "Permission denied error",
    "Admin rights required error",
    "Windows explorer not responding",
    "Taskbar not working",
    "Start menu not working",
    "Sound not working (software)",
    "No audio output device installed",
    "Microphone not detected (software)",
    "Webcam not detected (software)",
    "Printer not printing",
    "Printer driver error",
    "Bluetooth not working (software)",
    "USB driver error",
    "Game not launching",
    "Game lag / low FPS",
    "Compatibility issue",
    "Update loop error",
    "Login error / password issue",
    "Sync error (cloud apps)",
    "Email not sending/receiving",
    "Software freezing randomly"
]

@bot.message_handler(func=lambda m: m.text == "🖥 Hardware Error")
def show_hardware(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for err in hardware_errors:
        markup.add(types.InlineKeyboardButton(err, callback_data=err))
    
    bot.send_message(message.chat.id, "🔧 Hardware Error ကိုရွေးပါ:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "💻 Software Error")
def show_software(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for err in software_errors:
        markup.add(types.InlineKeyboardButton(err, callback_data=err))

    bot.send_message(message.chat.id, "💻 Software Error ကိုရွေးပါ:", reply_markup=markup)

# ===== STEP 4: Callback Handler (Show Fix) =====
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    error = call.data
    if error in FIXES:
        bot.send_message(call.message.chat.id, FIXES[error], parse_mode="Markdown")
        bot.send_message(
            call.message.chat.id,
            "❓ အဆင်ပြေလား?\n\nမရသေးရင် /contact နှိပ်ပါ"
        )
    else:
        bot.send_message(
            call.message.chat.id,
            "❌ ဒီ error အတွက် data မရှိသေးပါ (fixes.py ထဲထည့်သွင်းရန်လိုအပ်သည်)"
        )

# ===== Contact Handler =====
@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(
        message.chat.id,
        "📞 Technician ချိတ်ချင်ရင် @gafvkk ကိုဆက်သွယ်ပါ"
    )

# Start the bot
print("Bot is running...")
bot.polling()
