import telebot
from telebot import types
from fixes import FIXES

# Replace with your actual Bot Token
bot = telebot.TeleBot("8689664926:AAFkgFbwGXwX0Iknl1VrXfs6OnEgBYf3b7I")

# ===== FUNCTIONS FOR BETTER UX =====

def get_main_menu_keyboard():
    """Main Menu ခလုတ်များ ထုတ်ပေးသည့် Function"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🖥 Hardware Error", "💻 Software Error")
    return markup

def get_back_keyboard():
    """Fix အောက်မှာ ပြန်သွားဖို့ ခလုတ်များ"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_main"),
        types.InlineKeyboardButton("📞 Contact Support", callback_data="contact_us")
    )
    return markup

# ===== STEP 1: Start & Menu Handler =====
@bot.message_handler(commands=['start', 'menu'])
def start(message):
    welcome_text = """
<b>👋 Welcome to PC Support Bot</b>

💡 <i>PC ပြဿနာရှိရင် အောက်မှာ ရွေးချယ်ပါ</i>
    """
    bot.send_message(
        message.chat.id,
        welcome_text,
        parse_mode="HTML",
        reply_markup=get_main_menu_keyboard()
    )

# ===== STEP 2: Hardware & Software Lists =====
hardware_errors = [
    "Laptop no power", "Laptop not charging", "Laptop no display",
    "Screen black but fan running", "Laptop overheating", "Laptop auto shutdown",
    "Laptop fan not spinning", "Laptop keyboard not working", "Laptop touchpad not working",
    "Broken screen / cracked display", "External monitor no signal", "Monitor flickering",
    "Monitor no power", "PC not turning on", "PC turns on then off immediately",
    "No POST (no beep, no display)", "Continuous beeping sound", "RAM not detected",
    "Faulty RAM (random crashes)", "Hard disk not detected", "HDD clicking noise",
    "SSD not recognized", "Slow hard disk performance", "CPU overheating",
    "CPU fan error", "GPU not detected", "GPU overheating",
    "No display from GPU", "Motherboard failure", "BIOS not booting",
    "CMOS battery dead", "USB port not working", "USB device not recognized (hardware)",
    "Power supply failure (PSU dead)", "Random restarts (hardware issue)",
    "Laptop battery draining fast", "Battery not detected", "Charger not working",
    "Loose charging port", "Speaker not working (hardware)", "No sound from speakers",
    "Headphone jack not working", "Webcam not working (hardware)",
    "Microphone not working (hardware)", "Ethernet port not working",
    "WiFi card failure", "Bluetooth not working (hardware)", "Overheating while charging",
    "Burning smell from PC", "Physical damage (water spill / shock)"
]

software_errors = [
    "Windows not booting", "Blue Screen of Death (BSOD)",
    "Windows stuck on loading screen", "Windows update failed", "Windows activation error",
    "Slow Windows performance", "System freeze / not responding", "App not opening",
    "Program crash", "Software installation failed", "Driver not installed",
    "Driver outdated", "Driver conflict", "WiFi connected but no internet",
    "Network limited access", "DNS error", "IP conflict", "Browser not loading pages",
    "Chrome not opening", "App keeps crashing", "High CPU usage", "High RAM usage",
    "Disk usage 100%", "Malware infection", "Virus detected",
    "Antivirus blocking apps", "File corrupted", "Missing DLL error",
    "Software license error", "Permission denied error", "Admin rights required error",
    "Windows explorer not responding", "Taskbar not working", "Start menu not working",
    "Sound not working (software)", "No audio output device installed",
    "Microphone not detected (software)", "Webcam not detected (software)",
    "Printer not printing", "Printer driver error", "Bluetooth not working (software)",
    "USB driver error", "Game not launching", "Game lag / low FPS",
    "Compatibility issue", "Update loop error", "Login error / password issue",
    "Sync error (cloud apps)", "Email not sending/receiving", "Software freezing randomly"
]

@bot.message_handler(func=lambda m: m.text == "🖥 Hardware Error")
def show_hardware(message):
    # UI: Loading message ပေးသင့်ပါတယ် (သို့သော်လည်း လျင်မြန်စေဖို့ တိုက်ရိုက်ပို့ပါမည်)
    markup = types.InlineKeyboardMarkup(row_width=1) # စာရင်းကြီးဖြစ်တာကြောင့် row_width 1 (Vertical)
    for err in hardware_errors:
        # Button အမည်ကို အနည်းငယ်တိတ်ချုပ်ပြီး ပြသပါ (မလိုလျှင် err ကိုသာသုံးပါ)
        markup.add(types.InlineKeyboardButton(f"🔧 {err}", callback_data=err))
    
    bot.send_message(
        message.chat.id,
        "<b>🔧 Hardware Error ရွေးပါ</b>\n\n<i>အောက်ပါစာရင်းထဲမှ သင့်ခံစားရတဲ့ ပြဿနာကို ရွေးပါ...</i>",
        parse_mode="HTML",
        reply_markup=markup
    )

@bot.message_handler(func=lambda m: m.text == "💻 Software Error")
def show_software(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for err in software_errors:
        markup.add(types.InlineKeyboardButton(f"💻 {err}", callback_data=err))

    bot.send_message(
        message.chat.id,
        "<b>💻 Software Error ရွေးပါ</b>\n\n<i>အောက်ပါစာရင်းထဲမှ သင့်ခံစားရတဲ့ ပြဿနာကို ရွေးပါ...</i>",
        parse_mode="HTML",
        reply_markup=markup
    )

# ===== STEP 3: Callback Handler (Show Fix + Navigation) =====
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    # UX: Button နှိပ်ပြီးရင် Loading လှည့်ပြီး ရပ်သွားအောင်လုပ်ခြင်း
    bot.answer_callback_query(call.id)

    if call.data == "back_to_main":
        # UX: Back button နှိပ်ရင် Main Menu ကိုပြန်ပြပေးခြင်း
        bot.send_message(
            call.message.chat.id,
            "<b>🔙 Main Menu သို့ ပြန်သွားပါသည်</b>",
            parse_mode="HTML",
            reply_markup=get_main_menu_keyboard()
        )
        return

    if call.data == "contact_us":
        # UX: Contact ခလုတ်နှိပ်ရင် ဆက်သွယ်နည်းပြခြင်း
        bot.send_message(
            call.message.chat.id,
            "📞 <b>Technician ချိတ်ဆက်ရန်</b>\n\n👤 @gafvkk ကို Message ပို့ပါ။",
            parse_mode="HTML"
        )
        return

    # Error ရွေးချယ်မှု
    error = call.data
    if error in FIXES:
        # Fix ကိုပို့ခြင်း
        bot.send_message(
            call.message.chat.id,
            FIXES[error],
            parse_mode="Markdown" # Fixes.py ထဲမှာ Markdown style သုံးထားတာကြောင့်
        )
        
        # UX: Action Buttons (Back to Menu / Contact) ပို့ခြင်း
        bot.send_message(
            call.message.chat.id,
            "<i>❓ အကူအညီလိုသေးသလား?</i>",
            parse_mode="HTML",
            reply_markup=get_back_keyboard()
        )
    else:
        # Data မရှိရင် Error Message
        bot.send_message(
            call.message.chat.id,
            "❌ <b>ခေတ်မှီးတဲ့ Data မတွေ့ပါ</b>",
            parse_mode="HTML"
        )

# ===== STEP 4: Text Handler for /contact command =====
@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(
        message.chat.id,
        "📞 <b>Technician ချိတ်ဆက်ရန်</b>\n\n👤 @gafvkk ကို Message ပို့ပါ။",
        parse_mode="HTML"
    )

# Start Bot
print("Bot is running with improved UI/UX...")
bot.polling() 
import telebot
from telebot import types
from fixes import FIXES  # fixes.py ကို import လုပ်ထားပါသည်

# Replace with your actual Bot Token
bot = telebot.TeleBot("8689664926:AAFkgFbwGXwX0Iknl1VrXfs6OnEgBYf3b7I")

# ===== STEP 1: Start Handler =====
@bot.message_handler(commands=['start'])
def start(message):
    # markup ကို ဤနေရာတွင် အရင်သတ်မှတ်ထားပါသည်
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
    markup = types.InlineKeyboardMarkup(row_width=1) # row_width=1 makes buttons list vertically
    for err in hardware_errors:
        markup.add(types.InlineKeyboardButton(err, callback_data=err))
    
    # send_message တွင် message.chat.id နောက် ကွန်မာ `,` ပါရန်လိုပါသည်
    bot.send_message(message.chat.id, "🔧 Hardware Error ကိုရွေးပါ:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "💻 Software Error")
def show_software(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    for err in software_errors:
        markup.add(types.InlineKeyboardButton(err, callback_data=err))

    # send_message တွင် message.chat.id နောက် ကွန်မာ `,` ပါရန်လိုပါသည်
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
            "❌ ဒီ error အတွက် data မရှိသေးပါ"
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
