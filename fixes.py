
FIXES = {

    # ===== HARDWARE (Updated Keys to match List) =====

    "Laptop no power": """🔧 Laptop လုံးဝမဖွင့်တော့တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Charger, Socket, Battery, Motherboard power rail.
🛠 ဖြေရှင်းနည်း:
1. Wall socket ပြောင်းစမ်းပါ။
2. Charger LED လင်းမလင်း စစ်ပါ။
3. USB devices အားလုံးဖြုတ်ပါ။
4. Power button ကို 15s နှိပ်ထားပါ။
5. တခြား charger နဲ့ စမ်းပါ။
⚠️ LED မလင်းရင် Board level issue ဖြစ်နိုင်ပါတယ်။""",

    "Laptop not charging": """🔋 Laptop ဘက်ထရီ မအားသွင်းနိုင်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Charger watt မကိုက်, Battery aging, Charging port fault.
🛠 ဖြေရှင်းနည်း:
1. Original/Watt ကိုက်တဲ့ charger သုံးပါ။
2. Connection ပြန်ချိတ်ပါ။
3. BIOS ထဲက Battery health စစ်ပါ။
⚠️ မအားသွင်းရင် Battery replace လိုနိုင်ပါတယ်။""",

    "Laptop no display": """🖥 Laptop ဖွင့်ပေမယ့် Screen မထွက်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: RAM, Display cable, LCD, GPU.
🛠 ဖြေရှင်းနည်း:
1. Brightness key (Fn + Brightness) နှိပ်ပါ။
2. External monitor ချိတ်စမ်းပါ။
3. RAM ဖြုတ်ပြီး ပြန်တပ်ပါ။
⚠️ External ထွက်ပြီး Internal မထွက်ရင် LCD ပြဿနာပါ။""",

    "Screen black but fan running": """⚠️ Screen မထွက်ဘဲ fan လည်နေခြင်း
📌 အကြောင်းရင်း: RAM, POST failure, BIOS.
🛠 ဖြေရှင်းနည်း:
1. RAM ဖြုတ်တပ် လုပ်ပါ။
2. External monitor ချိတ်စမ်းပါ။
3. Power reset (30 sec) လုပ်ပါ။
⚠️ Beep အသံထွက်ရင် RAM ကို စစ်ဆေးပါ။""",

    "Laptop overheating": """🔥 Laptop အပူလွန်ကဲခြင်း
📌 အကြောင်းရင်း: Dust, Fan, Airflow, Heavy apps.
🛠 ဖြေရှင်းနည်း:
1. Hard surface ပေါ်မှာတင်သုံးပါ။
2. Air vents သန့်ရှင်းပါ။
3. Cooling pad သုံးပါ။
⚠️ Auto shutdown ဖြစ်ရင် Urgent fix လိုပါတယ်။""",

    "Laptop auto shutdown": """⚠️ Laptop သူ့ဘာသာ ပိတ်သွားခြင်း
📌 အကြောင်းရင်း: Overheating, Battery fault, Motherboard short.
🛠 ဖြေရှင်းနည်း:
1. Laptop အေးအောင်ထားပါ။
2. Battery မပါဘဲ charger နဲ့စမ်းပါ။
3. Vents သန့်ရှင်းပါ။
⚠️ Charging တုန်းကပဲပိတ်ရင် charging circuit issue ဖြစ်ပါတယ်။""",

    "Laptop fan not spinning": """🌀 Laptop fan မလည်ခြင်း
📌 အကြောင်းရင်း: Dust, Fan motor fault, BIOS settings.
🛠 ဖြေရှင်းနည်း:
1. Heavy task run ပြီး temp တက်စေပါ။
2. Vents သန့်ရှင်းပါ။
3. BIOS fan speed စစ်ပါ။
⚠️ Load တင်ပြီး fan မလည်ရင် hardware failure ဖြစ်ပါတယ်။""",

    "Laptop keyboard not working": """⌨️ Keyboard မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Liquid spill, Ribbon loose, Driver.
🛠 ဖြေရှင်းနည်း:
1. USB keyboard ချိတ်စမ်းပါ။
2. Keyboard ကို သန့်ရှင်းပါ။
3. Device Manager မှ reinstall driver လုပ်ပါ။
⚠️ ရေစွတ်ထားရင် ချက်ချင်း power off လုပ်ပါ။""",

    "Laptop touchpad not working": """🖱 Touchpad မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Disabled hotkey, Driver, Settings.
🛠 ဖြေရှင်းနည်း:
1. Fn + Touchpad key နှိပ်စမ်းပါ။
2. Settings > Devices > Touchpad စစ်ပါ။
3. Driver update လုပ်ပါ။
⚠️ Mouse နဲ့အဆင်ပြေရင် touchpad hardware ပျက်နိုင်ပါတယ်။""",

    "Broken screen / cracked display": """💥 Screen ကွဲ/အက်နေတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Physical damage.
🛠 ဖြေရှင်းနည်း:
1. External monitor ချိတ်ပြီး data backup ယူပါ။
2. Software နည်းနဲ့ မပြေနိုင်ပါ။
⚠️ LCD Panel replacement လိုအပ်ပါတယ်။""",

    "External monitor no signal": """📺 External Monitor "No Signal"
📌 အကြောင်းရင်း: Input source မှား, Cable ပျက်.
🛠 ဖြေရှင်းနည်း:
1. Monitor input source ပြောင်းပါ (HDMI/DP).
2. Cable ချိတ်ပြန်စမ်းပါ။
3. Win+P နှိပ်ပြီး Duplicate/Extend လုပ်စမ်းပါ။
⚠️ တခြား cable နဲ့ စမ်းကြည့်ပါ။""",

    "Monitor flickering": """📺 Monitor တုံနှို့တ်ခြင်း
📌 အကြောင်းရင်း: Refresh rate, Cable, Panel fault.
🛠 ဖြေရှင်းနည်း:
1. Cable လဲလိုက်ပါ။
2. Refresh rate လျှော့ပါ (Settings > Display)။
3. Monitor built-in diagnostics လုပ်စမ်းပါ။
⚠️ Self-test မှာလည်း flicker ဖြစ်ရင် monitor ပျက်နေပါတယ်။""",

    "Monitor no power": """📺 Monitor မီးမဝင်ခြင်း
📌 အကြောင်းရင်း: Power cable, Outlet, Fuse.
🛠 ဖြေရှင်းနည်း:
1. Power cable ချိတ်ပြန်စမ်းပါ။
2. Wall socket စစ်ပါ။
3. Monitor rear button ဖွင့်ထားမထား စစ်ပါ။
⚠️ LED မတက်ရင် internal power board ပျက်နိုင်ပါတယ်။""",

    "PC not turning on": """🖥 Desktop PC မဖွင့်ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: PSU, Cable, Motherboard connection.
🛠 ဖြေရှင်းနည်း:
1. Rear PSU switch စစ်ပါ။
2. Power cable လဲပါ။
3. Motherboard 24-pin နှင့် CPU power cable စစ်ပါ။
⚠️ Motherboard LED မီးတစ်မျိုးမျိုး မလင်းရင် PSU ပျက်နေပါတယ်။""",

    "PC turns on then off immediately": """⚠️ PC ဖွင့်တ်နဲ့ ချက်ချင်းပိတ်သွားခြင်း
📌 အကြောင်းရင်း: Short, PSU protection, CPU cooler.
🛠 ဖြေရှင်းနည်း:
1. Power cord ဖြုတ်ပါ။
2. USB devices အားလုံးဖြုတ်ပါ။
3. RAM တစ်ခုတည်းနဲ့ စမ်းပါ။
4. CPU cooler ချိတ်ထားမထား စစ်ပါ။
⚠️ ဒီပြဿနာက Hardware ကို အလွန်ထိခိုက်စေနိုင်ပါတယ်။""",

    "No POST (no beep, no display)": """🔧 No POST ဖြစ်ခြင်း
📌 အကြောင်းရင်း: RAM, CPU, Motherboard.
🛠 ဖြေရှင်းနည်း:
1. RAM ဖြုတ်ပြီး တစ်ခုချင်းစီနဲ့ စမ်းပါ။
2. GPU ဖြုတ်ပြီး (ရှိသလို) iGPU နဲ့ စမ်းပါ။
3. Clear CMOS လုပ်ပါ။
⚠️ Debug LED ရှိရင် အရောင်ကို ကြည့်ပါ။""",

    "Continuous beeping sound": """🔊 PC ဖွင့်တိုင်း Beep အသံထွက်ခြင်း
📌 အကြောင်းရင်း: RAM issue (Continuous), GPU issue (Beep code).
🛠 ဖြေရှင်းနည်း:
1. Beep pattern ကို မှတ်ထားပါ။
2. RAM ဖြုတ်တပ် လုပ်ပါ။
3. Motherboard manual နဲ့ တိုက်စစ်ပါ။
⚠️ Pattern မှန်မှန်သိရင် ဖြေရှင်းရ လွယ်ပါတယ်။""",

    "RAM not detected": """💾 RAM မသိတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Seated incorrectly, Slot dirty, Incompatible.
🛠 ဖြေရှင်းနည်း:
1. PC ပိတ်ပြီး RAM ပြန်တပ်ပါ။
2. Slot ပြောင်းစမ်းပါ။
3. တစ်ချောင်းတည်းနဲ့ စမ်းပါ။
⚠️ တစ်ချောင်းနဲ့ရပြီး တစ်ချောင်းမရရင် RAM ပျက်နေပါတယ်။""",

    "Faulty RAM (random crashes)": """⚠️ RAM ချို့ယွင်းပြီး Crash ဖြစ်ခြင်း
📌 အကြောင်းရင်း: Memory defect.
🛠 ဖြေရှင်းနည်း:
1. MemTest86 / Windows Memory Diagnostic run လုပ်ပါ။
2. XMP/Overclocking ပိတ်ပါ။
⚠️ Data corruption ဖြစ်နိုင်လို့ Backup ယူပါ။""",

    "Hard disk not detected": """💽 HDD မသိတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: SATA cable, Power, BIOS setting.
🛠 ဖြေရှင်းနည်း:
1. BIOS ထဲမှာ Drive မင်မမင် စစ်ပါ။
2. Cables ချိတ်ပြန်ပါ။
3. Disk Management မှာ ပါမပါ စစ်ပါ။
⚠️ Cable လဲလိုက်ပေမယ့် မမင်ရင် Drive ပျက်နိုင်ပါတယ်။""",

    "HDD clicking noise": """🚨 HDD က Click အသံထွက်ခြင်း
📌 အကြောင်းရင်း: Mechanical failure (Head crash).
🛠 ဖြေရှင်းနည်း:
1. ⛔ ချက်ချင်း Power off လုပ်ပါ။
2. Data backup ယူဖို့ ကြိုးစားပါ။
⚠️ ဆက်သုံးရင် Data အားလုံးဆုံးရှုံးနိုင်ပါတယ်။""",

    "SSD not recognized": """💾 SSD မသိတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: M.2 connection, Driver, Firmware.
🛠 ဖြေရှင်းနည်း:
1. Disk Management မှာ Initialize လုပ်နိုင်မလား စစ်ပါ။
2. BIOS ထဲမှာ ပါမပါ စစ်ပါ။
3. Chipset driver update လုပ်ပါ။
⚠️ New SSD ဆိုရင် Disk Management မှာ ပထမဆုံး Initialize လုပ်ရပါမည်။""",

    "Slow hard disk performance": """🐢 HDD အလွန်နှေးခြင်း
📌 အကြောင်းရင်း: Aging HDD, Bad sectors, Fragmentation.
🛠 ဖြေရှင်းနည်း:
1. Disk Defrag လုပ်ပါ (HDD အတွက်သာ)။
2. ChkDsk လုပ်ပြီး Bad sector စစ်ပါ။
⚠️ SSD ပြောင်းသုံးရင် အများကြီး အမြန်မြင်မြင် တိုးတက်ပါမည်။""",

    "CPU overheating": """🔥 CPU အပူလွန်ကဲခြင်း
📌 အကြောင်းရင်း: Thermal paste, Cooler, Airflow.
🛠 ဖြေရှင်းနည်း:
1. Case fans လည်နေမလည်နေ စစ်ပါ။
2. Thermal paste လဲပါ။
3. Cooler ကို တိကျစွာတပ်ပါ။
⚠️ Thermal throttling ဖြစ်နေရင် စွမ်းဆောင်ရည် ကျနေပါတယ်။""",

    "CPU fan error": """⚙️ CPU Fan Error
📌 အကြောင်းရင်း: Header connection, Fan speed.
🛠 ဖြေရှင်းနည်း:
1. CPU_FAN header မှာ ချိတ်ထားမထား စစ်ပါ။
2. Cable တိကျစွာနှိပ်ပါ။
⚠️ Fan မပါဘဲ ignore လုပ်သုံးရင် CPU လောင်နိုင်ပါတယ်။""",

    "GPU not detected": """🎮 GPU မသိတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: PCIe power cables, Slot, Driver.
🛠 ဖြေရှင်းနည်း:
1. PCIe 6/8 pin power cables ချိတ်ထားမထား စစ်ပါ။
2. GPU ကို တစ်ချက်နှိပ်စမ်းပါ။
3. Device Manager မှာ scan လုပ်ပါ။
⚠️ Power မရောက်ရင် GPU အလုပ်မလုပ်ပါ။""",

    "GPU overheating": """🔥 GPU အပူလွန်ကဲခြင်း
📌 အကြောင်းရင်း: Fans, Dust, Thermal pads.
🛠 ဖြေရှင်းနည်း:
1. GPU fans သန့်ရှင်းပါ။
2. Overclocking ပိတ်ပါ။
3. Case airflow ကောင်းအောင်လုပ်ပါ။
⚠️ Temp 90C+ ရောက်ရင် အလွန်ပူနေပါတယ်။""",

    "No display from GPU": """🖥 GPU မှာ Screen မထွက်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Cable မတပ်မှန်, Port ပျက်.
🛠 ဖြေရှင်းနည်း:
1. Monitor cable ကို GPU ရဲ့ port မှာ တပ်ပါ (Motherboard မှာ မဟုတ်ပါ)။
2. Monitor input source ပြောင်းပါ။
3. Cable လဲလိုက်ပါ။
⚠️ တခြား Monitor နဲ့ စမ်းကြည့်ပါ။""",

    "Motherboard failure": """⚠️ Motherboard ချို့ယွင်းခြင်း
📌 အကြောင်းရင်း: Capacitor blown, Short circuit.
🛠 ဖြေရှင်းနည်း:
1. Visual inspection လုပ်ပြီး damage ရှာပါ။
2. Minimal boot test လုပ်ပါ။
⚠️ Motherboard repair ဆိုတာ complex ပါ။ Expert လိုပါတယ်။""",

    "BIOS not booting": """🔧 BIOS မတက်ခြင်း
📌 အကြောင်းရင်း: Corrupted BIOS, Failed update.
🛠 ဖြေရှင်းနည်း:
1. Clear CMOS (Battery remove) လုပ်ပါ။
2. BIOS Flashback feature သုံးပါ (ရှိသလို)။
⚠️ Update လုပ်နေတုန်းက မပိတ်ရပါဘူး။""",

    "CMOS battery dead": """🔋 CMOS Battery အားကုန်ခြင်း
📌 အကြောင်းရင်း: Time/Date reset ဖြစ်နေခြင်း။
🛠 ဖြေရှင်းနည်း:
1. CR2032 battery အသစ်ဖြင့် အစားထိုးပါ။
2. BIOS ထဲမှာ အချိန်ပြန်ချိန်ညှိပါ။
⚠️ ဒီ battery က BIOS settings မှတ်ထားပေးပါတယ်။""",

    "USB port not working": """🔌 USB Port မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Driver, Physical damage, Loose header.
🛠 ဖြေရှင်းနည်း:
1. Device Manager > Uninstall driver > Restart လုပ်ပါ။
2. တခြား port မှာ စမ်းပါ။
⚠️ Port ထဲက pin တစ်ခု ကျိုးနေရင် မသုံးသင့်ပါဘူး။""",

    "USB device not recognized (hardware)": """🔌 USB Device မသိတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Device ပျက်, Cable ပျက်.
🛠 ဖြေရှင်းနည်း:
1. Device ကို တခြား PC မှာ စမ်းပါ။
2. Cable လဲလိုက်ပါ။
3. PC restart လုပ်ပါ။
⚠️ တခြား PC မှာလည်း မမင်ရင် Device ပျက်နေပါတယ်။""",

    "Power supply failure (PSU dead)": """⚡ PSU ပျက်ခြင်း
📌 အကြောင်းရင်း: Capacitor failure, Short.
🛠 ဖြေရှင်းနည်း:
1. Power cord ဖြုတ်ပြီး မိနစ်အနည်းငယ် စောင့်ပါ။
2. Smell တစ်ခုခု ရှိမရှိ နမ်းကြည့်ပါ။
⚠️ PSU ဖွင့်ပြီး အတွင်းပိုင်းကို မကြည့်ရပါဘူး။""",

    "Random restarts (hardware issue)": """⚠️ Random Restarts
📌 အကြောင်းရင်း: PSU unstable, Overheating, RAM.
🛠 ဖြေရှင်းနည်း:
1. Temp မြင့်နေမရင် RAM/PSU စစ်ပါ။
2. RAM test လုပ်ပါ။
3. PSU swap test လုပ်ပါ။
⚠️ Idle မှာ restart ဖြစ်ရင် PSU သံသယရှိပါတယ်။""",

    "Laptop battery draining fast": """🔋 Battery အားစားမနှေးခြင်း
📌 အကြောင်းရင်း: Background apps, Brightness, Battery aging.
🛠 ဖြေရှင်းနည်း:
1. Brightness လျှော့ပါ။
2. Battery Saver mode ဖွင့်ပါ။
3. Battery Health Report ထုတ်ပါ။
⚠️ Battery သက်တမ်း ကုန်နေရင် Replace လိုပါမည်။""",

    "Battery not detected": """🔋 Battery မသိတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Connector loose, Battery dead.
🛠 ဖြေရှင်းနည်း:
1. Battery ဖြုတ်ပြီး ပြန်တပ်ပါ။
2. BIOS update လုပ်ပါ။
⚠️ Battery မပါဘဲ AC adapter နဲ့သာ အသုံးပြုရန် စဉ်းစားပါ။""",

    "Charger not working": """⚡ Charger မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Cable cut, Adapter dead.
🛠 ဖြေရှင်းနည်း:
1. Cable စစ်ကြည့်ပါ။
2. တခြား cable သုံးစမ်းပါ။
⚠️ Original charger သုံးရင် အကောင်းဆုံးပါ။""",

    "Loose charging port": """⚠️ Charging Port လှုပ်နေတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: DC Jack solder broken.
🛠 ဖြေရှင်းနည်း:
1. Pin ကို ကောင်းကောင်းနှိပ်ပြီး စမ်းပါ။
⚠️ ဆက်သုံးရင် Motherboard short ဖြစ်နိုင်ပါတယ်။""",

    "Speaker not working (hardware)": """🔊 Speaker Hardware မထွက်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Speaker blown, Cable disconnected.
🛠 ဖြေရှင်းနည်း:
1. Headphone ချိတ်ပြီး စမ်းပါ။
2. Driver reinstall လုပ်ပါ။
⚠️ Headphone မှာလည်း မထွက်ရင် Hardware ဖြစ်ပါတယ်။""",

    "No sound from speakers": """🔊 အသံလုံးဝမထွက်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Audio device disabled, Service stopped.
🛠 ဖြေရှင်းနည်း:
1. Speaker icon နှိပ်ပြီး Volume စစ်ပါ။
2. Audio service (Windows Audio) restart လုပ်ပါ။
⚠️ Update လုပ်ပြီး driver ပျောက်တတ်ပါတယ်။""",

    "Headphone jack not working": """🎧 Headphone Jack မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Dust, Broken contact.
🛠 ဖြေရှင်းနည်း:
1. Jack ထဲကို သန့်ရှင်းပစ်ပါ။
2. တခြား headphone နဲ့ စမ်းပါ။
⚠️ တဖက်သာကြားရင် Jack ပျက်နေပါတယ်။""",

    "Webcam not working (hardware)": """📷 Webcam Hardware မထွက်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Privacy shutter, Cable loose.
🛠 ဖြေရှင်းနည်း:
1. Lens shutter ပိတ်ထားမထား စစ်ပါ။
2. Device Manager မှာ Camera ပါမပါ စစ်ပါ။
⚠️ Software နည်းနဲ့ မပြေရင် cable ပြတ်နိုင်ပါတယ်။""",

    "Microphone not working (hardware)": """🎤 Microphone Hardware မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Hole blocked, Loose connection.
🛠 ဖြေရှင်းနည်း:
1. Mic hole သန့်ရှင်းပစ်ပါ။
2. External mic ချိတ်စမ်းပါ။
⚠️ Laptop internal mic ပျက်ရင် ပြင်ရခက်ပါတယ်။""",

    "Ethernet port not working": """🌐 LAN Port မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Cable cut, Driver issue.
🛠 ဖြေရှင်းနည်း:
1. Cable လဲလိုက်ပါ။
2. Port LED မီးမီးနေမထား စစ်ပါ။
3. Driver reinstall လုပ်ပါ။
⚠️ Port pin များ ကျိုးနေရင် မသုံးသင့်ပါဘူး။""",

    "WiFi card failure": """📶 WiFi Card ပျက်ခြင်း
📌 အကြောင်းရင်း: Antenna loose, Card dead.
🛠 ဖြေရှင်းနည်း:
1. Card နောက်က antenna cables စစ်ပါ။
2. USB WiFi ချိတ်စမ်းပါ။
⚠️ Device Manager မှာ Yellow mark တွေ့ရင် Card ပျက်နေပါတယ်။""",

    "Bluetooth not working (hardware)": """📶 Bluetooth Hardware ပျက်ခြင်း
📌 အကြောင်းရင်း: Module failure, Driver missing.
🛠 ဖြေရှင်းနည်း:
1. Device Manager မှာ ပါမပါ စစ်ပါ။
2. USB Bluetooth dongle သုံးစမ်းပါ။
⚠️ WiFi/BT combo card မျိုးဆိုရင် တစ်ခုပျက်ရင် နှစ်ခုလုံးပျက်တတ်ပါတယ်။""",

    "Overheating while charging": """🔥 အားသွင်းနေရင် အပူတက်ခြင်း
📌 အကြောင်းရင်း: Heavy usage + Charging, Low wattage charger.
🛠 ဖြေရှင်းနည်း:
1. Gaming လုပ်နေရင် charger မချိတ်ပါ။
2. Original charger သုံးပါ။
3. Laptop ကို ပြားပေါ်တင်ထားပါ။
⚠️ Battery ပူလွန်းရင် သက်တမ်း ကြာရှည်ခံနိုင်ပါတယ်။""",

    "Burning smell from PC": """🚨 မီးလောင်နံ့ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Short circuit, PSU blown.
🛠 ဖြေရှင်းနည်း:
1. ⛔ ချက်ချင်း Power ခလုတ်ဖြုတ်ပါ။
2. Wall socket ကနေ plug ဖြုတ်ပါ။
⚠️ ကြိုးစားပြီး ပြန်ဖွင့်စရာမလိုပါဘူး။""",

    "Physical damage (water spill / shock)": """⚠️ Physical Damage
📌 အကြောင်းရင်း: Drop, Water spill.
🛠 ဖြေရှင်းနည်း:
1. ရေဝင်ရင် - ချက်ချင်း power off လုပ်ပါ။
2. Drop ရင် - Screen/Hinge စစ်ပါ။
⚠️ Internal short က Data ဆုံးရှုံးစေနိုင်ပါတယ်။""",


    # ===== SOFTWARE (Updated Keys to match List) =====

    "Windows not booting": """💻 Windows မတက်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: System file corrupted, Update error.
🛠 ဖြေရှင်းနည်း:
1. Automatic Repair / Startup Repair လုပ်ပါ။
2. Safe Mode ဝင်ပြီး Restore လုပ်ပါ။
3. CMD > chkdsk /f /r လုပ်ပါ။
⚠️ မရသေးရင် Repair Install လိုပါတယ်။""",

    "Blue Screen of Death (BSOD)": """💙 Blue Screen (BSOD)
📌 အကြောင်းရင်း: Driver error, Hardware fault.
🛠 ဖြေရှင်းနည်း:
1. Stop Code မှတ်ထားပါ။
2. Safe Mode ဝင်ပြီး Recent driver ကို uninstall လုပ်ပါ။
3. Windows Update လုပ်ပါ။
⚠️ RAM fault ဆိုရင် BSOD ပိုဖြစ်တတ်ပါတယ်။""",

    "Windows stuck on loading screen": """⏳ Loading Screen မှာ တိုင်နေခြင်း
📌 အကြောင်းရင်း: Driver issue, Disk error.
🛠 ဖြေရှင်းနည်း:
1. Force Restart လုပ်ပါ။
2. Startup Repair လုပ်ပါ။
3. External bootable drive နဲ့ Command Prompt ဖွင့်ပြီး fix လုပ်ပါ။
⚠️ HDD ပျက်နေတာဖြစ်နိုင်ပါတယ်။""",

    "Windows update failed": """🔄 Windows Update မအောင်မြင်ဘဲ ပြဿနာ
📌 အကြောင်းရင်း: Corrupted cache, Service stopped.
🛠 ဖြေရှင်းနည်း:
1. Troubleshooter run လုပ်ပါ။
2. Services (wuauserv) restart လုပ်ပါ။
3. SoftwareDistribution folder ကို delete လုပ်ပါ။
⚠️ Update လုပ်နေတုန်းက မပိတ်ရပါဘူး။""",

    "Windows activation error": """🔑 Activation Error
📌 အကြောင်းရင်း: Hardware change, Key expired.
🛠 ဖြေရှင်းနည်း:
1. Settings > Activation > Troubleshooter ကို click လုပ်ပါ။
2. Product Key ပြန်ထည့်စမ်းပါ။
⚠️ Pirated key မသုံးပါနှင့် (Security risk)။""",

    "Slow Windows performance": """🐢 Windows နှေးနေတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Startup apps, Full storage, HDD.
🛠 ဖြေရှင်းနည်း:
1. Task Manager > Startup apps disable လုပ်ပါ။
2. Disk Cleanup လုပ်ပါ။
3. SSD upgrade စဉ်းစားပါ။
⚠️ HDD နဲ့ Windows 10/11 ဆိုရင် နှေးတတ်ပါတယ်။""",

    "System freeze / not responding": """❄️ System Freeze
📌 အကြောင်းရင်း: Driver conflict, Overheating.
🛠 ဖြေရှင်းနည်း:
1. PC Restart လုပ်ပါ။
2. Clean boot (msconfig) လုပ်ပြီး culprit app ရှာပါ။
3. Drivers update လုပ်ပါ။
⚠️ Mouse လည်ပေမယ့် Keyboard မလုပ်ရင် Driver ပြဿနာဖြစ်နိုင်ပါတယ်။""",

    "App not opening": """📱 App မဖွင့်ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: App corrupted, Compatibility.
🛠 ဖြေရှင်းနည်း:
1. Settings > Apps > App ရွေး > Advanced options > Reset လုပ်ပါ။
2. App ကို Reinstall လုပ်ပါ။
⚠️ Store app ဆိုရင် `wsreset` command သုံးနိုင်ပါတယ်။""",

    "Program crash": """⚠️ Program ခဏခဏ crash ဖြစ်ခြင်း
📌 အကြောင်းရင်း: File corrupted, Compatibility.
🛠 ဖြေရှင်းနည်း:
1. App update လုပ်ပါ။
2. Compatibility mode စမ်းပါ (Properties > Compatibility)။
3. Reinstall လုပ်ပါ။
⚠️ Event Viewer မှာ Error logs ကြည့်ပါ။""",

    "Software installation failed": """📦 Software Install မအောင်မြင်ဘဲ ပြဿနာ
📌 အကြောင်းရင်း: Corrupted installer, Permission.
🛠 ဖြေရှင်းနည်း:
1. Installer ကို Run as Administrator နဲ့ ဖွင့်ပါ။
2. Antivirus ယာယီပိတ်ပြီး စမ်းပါ။
3. Temp files ရှင်းပါ။
⚠️ Download လုပ်ရင်် ပြီးသားလားစစ်ပါ။""",

    "Driver not installed": """⚙️ Driver မတင်ထားဘဲ ပြဿနာ
📌 အကြောင်းရင်း: Unknown device.
🛠 ဖြေရှင်းနည်း:
1. Device Manager > Scan for hardware changes လုပ်ပါ။
2. Windows Update မှ Optional drivers ရှာပါ။
3. Manufacturer website ကနေ driver download လုပ်ပါ။
⚠️ Auto install မဖြစ်ရင် Manual install လုပ်ရပါမည်။""",

    "Driver outdated": """⬆️ Driver ဟောင်းနေတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Performance issues, Compatibility.
🛠 ဖြေရှင်းနည်း:
1. Device Manager > Update driver လုပ်ပါ။
2. Manufacturer tool သုံးပါ (e.g., GeForce Experience)။
3. Beta/Preview driver မသုံးပါနှင့်။
⚠️ Update လုပ်ပြီး BSOD ဖြစ်ရင် Rollback လုပ်ပါ။""",

    "Driver conflict": """⚠️ Driver Conflict
📌 အကြောင်းရင်း: Two devices using same resources.
🛠 ဖြေရှင်းနည်း:
1. Problematic driver ကို Uninstall လုပ်ပါ။
2. Restart လုပ်ပြီး Windows က အလိုအလျောက် install လုပ်စေပါ။
⚠️ Recent change ပြန်ဖျက်ပါ။""",

    "WiFi connected but no internet": """🌐 WiFi ချိတ်ထားပေမယ့် Net မရ
📌 အကြောင်းရင်း: DNS, Router issue, ISP problem.
🛠 ဖြေရှင်းနည်း:
1. Router restart လုပ်ပါ။
2. WiFi forget လုပ်ပြီး Reconnect လုပ်ပါ။
3. CMD > ipconfig /flushdns လုပ်ပါ။
4. DNS server change (8.8.8.8) လုပ်စမ်းပါ။
⚠️ Mobile hotspot သုံးပြီး စမ်းကြည့်ပါ။""",

    "Network limited access": """📶 Network Limited Access
📌 အကြောင်းရင်း: IP conflict, DHCP issue.
🛠 ဖြေရှင်းနည်း:
1. Network reset လုပ်ပါ (Settings)။
2. CMD > ipconfig /renew လုပ်ပါ။
3. Router restart လုပ်ပါ။
⚠️ Static IP သုံးထားရင် Address ကိုစစ်ပါ။""",

    "DNS error": """🌍 DNS Error
📌 အကြောင်းရင်း: DNS server down, Cache corrupted.
🛠 ဖြေရှင်းနည်း:
1. CMD > ipconfig /flushdns လုပ်ပါ။
2. DNS ကို Google (8.8.8.8) သို့ Cloudflare (1.1.1.1) ပြောင်းပါ။
3. Router restart လုပ်ပါ။
⚠️ Website နာမည်ထည့်ပြီး မရရင် DNS ပြဿနာဖြစ်ပါတယ်။""",

    "IP conflict": """🔁 IP Address Conflict
📌 အကြောင်းရင်း: ကွန်ပျူတာနှစ်လုံး တူညီသော IP သုံးနေခြင်း။
🛠 ဖြေရှင်းနည်း:
1. CMD > ipconfig /release နောက် /renew လုပ်ပါ။
2. Router restart လုပ်ပါ။
3. Static IP သုံးထားရင် ပြောင်းပါ။
⚠️ ကွန်ပျူတာအများစုက ပြဿနာဖြစ်နိုင်ပါတယ်။""",

    "Browser not loading pages": """🌐 Browser Page မဖွင့်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Internet issue, Extension problem.
🛠 ဖြေရှင်းနည်း:
1. Internet connection ရှိမရှိ စစ်ပါ။
2. Incognito/Private mode မှာ စမ်းပါ။
3. DNS flush လုပးပါ။
⚠️ Incognito မှာ အဆင်ပြေရင် Extension ကို စစ်ဆေးပါ။""",

    "Chrome not opening": """🧩 Chrome မဖွင့်ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Profile corrupted, Background process stuck.
🛠 ဖြေရှင်းနည်း:
1. Task Manager မှာ Chrome processes အားလုံး End task လုပ်ပါ။
2. Desktop shortcut ကို --no-sandbox နဲ့ run လုပ်စမ်းပါ။
3. Profile ပြန်ဖန်တီထွင်ရန် (Reinstall) စဉ်းစားပါ။
⚠️ Malware scan လုပ်ရန်လည်း လိုနိုင်ပါတယ်။""",

    "App keeps crashing": """⚠️ App ခဏခဏ Crash ဖြစ်ခြင်း
📌 အကြောင်းရင်း: Update ပြဿနာ, Cache.
🛠 ဖြေရှင်းနည်း:
1. App Update လုပ်ပါ (သို့) Rollback လုပ်ပါ။
2. App Cache clear လုပ်ပါ။
3. App Repair လုပ်ပါ (Settings > Apps)။
⚠️ Windows တိုးတက်ပြီးမှ ဖြစ်နေရင် Compatibility issue ဖြစ်နိုင်ပါတယ်။""",

    "High CPU usage": """🔥 High CPU Usage
📌 အကြောင်းရင်း: Malware, Background process, Driver issue.
🛠 ဖြေရှင်းနည်း:
1. Task Manager မှာ High CPU စားတဲ့ Process ကို End task လုပ်ပါ။
2. Antivirus scan လုပးပါ။
3. Drivers update လုပ်ပါ။
⚠️ System Interrupts က စားနေရင် Hardware driver ပြဿနာဖြစ်ပါတယ်။""",

    "High RAM usage": """🧠 High RAM Usage
📌 အကြောင်းရင်း: Background apps, Memory leak.
🛠 ဖြေရှင်းနည်း:
1. Task Manager > Memory tab မှာ အများဆုံးစားသူကို ပိတ်ပါ။
2. Startup apps disable လုပ်ပါ။
3. RAM upgrade စဉ်းစားပါ။
⚠️ 8GB အောက်ဆိုရင် High usage ဖြစ်တတ်ပါတယ်။""",

    "Disk usage 100%": """💽 Disk Usage 100%
📌 အကြောင်းရင်း: System process (SysMain/Superfetch), HDD fault.
🛠 ဖြေရှင်းနည်း:
1. Services.msc မှ Superfetch/SysMain service ကို Disable လုပ်ပါ။
2. Virtual Memory (Page file) ကို Manage လုပ်ပါ။
3. ChkDsk လုပ်ပါ။
⚠️ HDD ဆိုရင် SSD ပြောင်းသုံးပါ (Best solution)။""",

    "Malware infection": """🦠 Malware ဝင်နေခြင်း
📌 အကြောင်းရင်း: Suspicious download, Phishing.
🛠 ဖြေရှင်းနည်း:
1. Internet ချိတ်ဆက်မှု ဖြတ်ပါ။
2. Windows Defender Offline scan လုပ်ပါ။
3. Malwarebytes တပ်ပြီး Scan လုပ်ပါ။
⚠️ Password များကို ပြောင်းသင့်ပါတယ်။""",

    "Virus detected": """🛡 Virus တွေ့ရှိခြင်း
📌 အကြောင်းရင်း: Real-time protection found threat.
🛠 ဖြေရှင်းနည်း:
1. Antivirus မှ Quarantine လုပ်ပါ (သို့) Remove လုပ်ပါ။
2. Full System Scan ထပ်လုပ်ပါ။
3. Detected file ကို သေချာပစ်ပစ်ပါ။
⚠️ False positive မဟုတ်မရင် ကောင်းသေားပါ။""",

    "Antivirus blocking apps": """⚠️ Antivirus က App ကို တားနေခြင်း
📌 အကြောင်းရင်း: False positive, Security policy.
🛠 ဖြေရှင်းနည်း:
1. Antivirus Exclusion list မှာ App path ထည့်ပါ။
2. App folder ကို Restore လုပ်ပါ။
⚠️ မသေချာသော File ကို Exclusion ထည့်ရင် Risk ရှိပါတယ်။""",

    "File corrupted": """📂 File Corrupted
📌 အကြောင်းရင်း: Bad sectors, Virus, Improper shutdown.
🛠 ဖြေရှင်းနည်း:
1. Previous Version (Restore) မှ ပြန်ယူစမ်းပါ။
2. ChkDsk လုပ်ပါ။
3. Backup ရှိရင် restore လုပ်ပါ။
⚠️ System file ဆိုရင် SFC /scannow လုပ်ပါ။""",

    "Missing DLL error": """⚙️ Missing DLL Error
📌 အကြောင်းရင်း: App uninstall, System file missing.
🛠 ဖြေရှင်းနည်း:
1. App ကို Reinstall လုပ်ပါ (အကောင်းဆုံး)။
2. System File Checker (SFC) လုပ်ပါ။
3. DLL ကို online ကနေ download မလုပ်ရပါနှင့်။
⚠️ Malware ကြောင့် ဖြစ်နိုင်ပါတယ်။""",

    "Software license error": """🔑 License Error
📌 အကြောင်းရင်း: Key expired, Activation server down.
🛠 ဖြေရှင်းနည်း:
1. Software Activation wizard ကို run ပါ။
2. Key ကို ပြန်ထည့်ပါ။
3. Vendor Support ကို ဆက်သွယ်ပါ။
⚠️ Cracked version သုံးရင် ဒီပြဿနာ မကြာခဏ ဖြစ်ပါတယ်။""",

    "Permission denied error": """⛔ Permission Denied
📌 အကြောင်းရင်း: Admin rights missing, File ownership.
🛠 ဖြေရှင်းနည်း:
1. Run as Administrator လုပ်ပါ။
2. File/Folder Properties > Security > Edit > Full Control ပေးပါ။
⚠️ System folder ထဲက file ကို Edit လုပ်တာ မဖြစ်နိုင်ပါဘူး။""",

    "Admin rights required error": """👤 Admin Rights Required
📌 အကြောင်းရင်း: UAC (User Account Control).
🛠 ဖြေရှင်းနည်း:
1. Right click > Run as administrator ရွေးပါ။
2. User Account က Admin account ဖြစ်မဖြစ် စစ်ပါ။
⚠️ Corporate PC ဆိုရင် IT Admin ကို တိုင်ပင်ရပါမည်။""",

    "Windows explorer not responding": """🧩 Windows Explorer Not Responding
📌 အကြောင်းရင်း: File error, Corrupt shell extension.
🛠 ဖြေရှင်းနည်း:
1. Task Manager မှ `explorer.exe` ကို Restart လုပ်ပါ။
2. PC Restart လုပ်ပါ။
3. Folder Options > View > Launch folder windows in a separate process ကို check လုပ်ပါ။
⚠️ ထပ်ခါတလဲလဲ ဖြစ်ရင် Update လုပ်ပါ။""",

    "Taskbar not working": """🖥 Taskbar မအလုပ်လုပ်တဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Explorer stuck.
🛠 ဖြေရှင်းနည်း:
1. Task Manager > Run new task > `powershell` ရိုက်ပါ။
2. `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}` command run လုပ်ပါ (Reinstall Taskbar apps).
⚠️ Restart လုပ်ရင် ပြေမြင်တတ်ပါတယ်။""",

    "Start menu not working": """🪟 Start Menu မဖွင့်ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Corrupted system apps.
🛠 ဖြေရှင်းနည်း:
1. Sign out ပြီး Sign in ပြန်လုပ်ပါ။
2. Powershell (Admin) ဖွင့်ပြီး `sfc /scannow` run လုပ်ပါ။
3. Create a new user account လုပ်စမ်းပါ။
⚠️ Windows Update bug ကြောင့်ဖြစ်နိုင်ပါတယ်။""",

    "Sound not working (software)": """🔊 Sound Software Issue
📌 အကြောင်းရင်း: Wrong output device, Audio service stopped.
🛠 ဖြေရှင်းနည်း:
1. Sound icon > Output device > Correct speakers ရွေးပါ။
2. Audio Troubleshooter run လုပးပါ။
3. `services.msc` > Windows Audio service restart လုပ်ပါ။
⚠️ Driver uninstall လုပ်ပြီး restart လုပ်ရင် ပြေမြင်တတ်ပါတယ်။""",

    "No audio output device installed": """🔊 No Audio Output Device
📌 အကြောင်းရင်း: Driver missing, Device disabled.
🛠 ဖြေရှင်းနည်း:
1. Device Manager > Sound... > Show hidden devices > Enable လုပ်ပါ။
2. Scan for hardware changes လုပ်ပါ။
3. Audio driver reinstall လုပ်ပါ။
⚠️ Update လုပ်ပြီး driver ပျောက်တတ်ပါတယ်။""",

    "Microphone not detected (software)": """🎤 Mic Not Detected (Software)
📌 အကြောင်းရင်း: Privacy settings, Driver.
🛠 ဖြေရှင်းနည်း:
1. Settings > Privacy > Microphone > Allow apps access ဖွင့်ပါ။
2. Device Manager မှာ driver တင်ထားမထား စစ်ပါ။
3. Sound settings > Input > Test microphone လုပ်ပါ။
⚠️ Disable ထားတာ ဖြစ်နိုင်ပါတယ်။""",

    "Webcam not detected (software)": """📷 Webcam Not Detected (Software)
📌 အကြောင်းရင်း: Privacy settings, App access blocked.
🛠 ဖြေရှင်းနည်း:
1. Settings > Privacy > Camera > Allow apps access ဖွင့်ပါ။
2. Device Manager မှ Camera ရှိမရှိ စစ်ပါ။
3. Camera app အစားတခြား app (Zoom, Teams) မှာ စမ်းပါ။
⚠️ Privacy shutter ပိတ်ထားမရှိစစ်ပါ။""",

    "Printer not printing": """🖨 Printer မပရင့်ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Offline, Paper jam, Driver.
🛠 ဖြေရှင်းနည်း:
1. Printer ကို Offline မှ Online ပြောင်းပါ။
2. Print Spooler service restart လုပ်ပါ (`services.msc`)။
3. USB ဖြုတ်တပ် လုပ်ပါ။
⚠️ Printer queue မှာ job များနေရင် Clear all လုပ်ပါ။""",

    "Printer driver error": """🖨 Printer Driver Error
📌 အကြောင်းရင်း: Corrupted driver, Wrong version.
🛠 ဖြေရှင်းနည်း:
1. Device Manager မှ Printer driver uninstall လုပ်ပါ။
2. PC restart လုပ်ပါ။
3. Manufacturer website ကနေ Latest driver download လုပ်ပါ။
⚠️ Generic driver သုံးတာထက် Specific driver က ပိုကောင်းပါတယ်။""",

    "Bluetooth not working (software)": """📶 Bluetooth Software Issue
📌 အကြောင်းရင်း: Service stopped, Discovery issue.
🛠 ဖြေရှင်းနည်း:
1. Bluetooth Support Service restart လုပ်ပါ။
2. Device hidden ဖြစ်နေရင် Show hidden devices မှာ Enable လုပ်ပါ။
3. Device ကို Remove လုပ်ပြီး Pair again လုပ်ပါ။
⚠️ Driver update လုပ်ရင် ပြေတတ်ပါတယ်။""",

    "USB driver error": """🔌 USB Driver Error
📌 အကြောင်းရင်း: Corrupted USB stack, Host controller issue.
🛠 ဖြေရှင်းနည်း:
1. Device Manager မှ Universal Serial Bus controllers အားလုံး Uninstall လုပ်ပါ။
2. PC restart လုပ်ပါ (Windows က re-install လုပ်ပေးမယ်)။
3. USB Selective Suspend turn off လုပ်ပါ (Power options)။
⚠️ Update လုပ်ပြီးမှ ပြဿနာဖြစ်ရင် Rollback လုပ်ပါ။""",

    "Game not launching": """🎮 Game မဖွင့်ရတဲ့ ပြဿနာ
📌 အကြောင်းရင်း: Driver, Runtime components missing.
🛠 ဖြေရှင်းနည်း:
1. GPU Driver update လုပ်ပါ (Clean install)။
2. DirectX / VC++ Redistributables reinstall လုပ်ပါ။
3. Game folder မှာ `Verify integrity of game files` လုပ်ပါ (Steam)။
⚠️ Overlay apps (Discord/Steam) ပိတ်စမ်းပါ။""",

    "Game lag / low FPS": """🎮 Game Lag / Low FPS
📌 အကြောင်းရင်း: High settings, Thermal throttling, VSync.
🛠 ဖြေရှင်းနည်း:
1. Graphics settings လျှော့ချပါ။
2. VSync ဖွင့်ပါ (သို့) Off လုပ်စမ်းပါ။
3. Game Mode (Windows) ဖွင့်ပါ။
4. Laptop temp ကို စစ်ပါ။
⚠️ 60Hz monitor မှာ 100+ FPS ယူရန် မလိုပါ။""",

    "Compatibility issue": """⚠️ Compatibility Issue
📌 အကြောင်းရင်း: ဆော့ဖ်ဝဲဟောင်း, ကွန်ပျူတာသစ်နှင့် မကိုက်ခြင်း။
🛠 ဖြေရှင်းနည်း:
1. Right click > Properties > Compatibility tab > Run this program in compatibility mode for (Win 7/8) ရွေးပါ။
2. Run as administrator ကို check လုပ်ပါ။
⚠️ 64-bit OS မှာ 16-bit software မဖွင့်နိုင်ပါ။""",

    "Update loop error": """🔄 Update Loop (Reverting Changes)
📌 အကြောင်းရင်း: Corrupted update files.
🛠 ဖြေရှင်းနည်း:
1. Safe Mode (Networking) ဝင်ပါ။
2. CMD > `dism /online /cleanup-image /revertpendingactions` run လုပ်ပါ။
3. SoftwareDistribution folder delete လုပ်ပါ။
⚠️ System Restore point ရှိရင် Restore လုပ်ပါ။""",

    "Login error / password issue": """🔐 Login Error / Password Issue
📌 အကြောင်းရင်း: Caps lock, Wrong password, Account lock.
🛠 ဖြေရှင်းနည်း:
1. Caps Lock ဖွင့်ထားမထား စစ်ပါ။
2. Keyboard layout (Eng/MM) စစ်ပါ။
3. Reset disk / Microsoft reset link သုံးပါ။
⚠️ ကျော်လွန်ရေးပြုလုပ်ရင် Account lock ဖြစ်နိုင်ပါတယ်။""",

    "Sync error (cloud apps)": """☁️ Sync Error (OneDrive/Drive)
📌 အကြောင်းရင်း: Internet issue, Credential problem.
🛠 ဖြေရှင်းနည်း:
1. Sync app ကို Quit/Close လုပးပြီး ပြန်ဖွင့်ပါ။
2. Account sign out ပြီး Sign in ပြန်လုပ်ပါ။
3. Selective sync folders ကို စစ်ပါ။
⚠️ File name မှာ illegal characters (e.g. < > : " / \ | ? *) မပါရန် စစ်ပါ။""",

    "Email not sending/receiving": """📧 Email Issue
📌 အကြောင်းရင်း: Wrong password, Server settings, Offline mode.
🛠 ဖြေရှင်းနည်း:
1. Work Offline mode ဖွင့်ထားမထား စစ်ပါ။
2. Email password ပြောင်းပြီးရင် App မှာ ပြန်ထည့်ပါ။
3. Inbox full ဖြစ်နေမရင် စစ်ပါ။
⚠️ Antivirus scanning email ကို disable လုပ်စမ်းပါ။""",

    "Software freezing randomly": """❄️ Software Randomly Freezing
📌 အကြောင်းရင်း: Background app conflict, RAM limit.
🛠 ဖြေရှင်းနည်း:
1. PC Restart လုပ်ပါ။
2. Clean boot လုပ်ပြီး App တစ်ခုချင်းစီ enable လုပ်ပြီး စမ်းကြည့်ပါ။
3. RAM upgrade စဉ်းစားပါ။
⚠️ HDD ပေါ်မှာ ကြီးမားတဲ့ App install လုပ်ရင် freeze ဖြစ်တတ်ပါတယ်။""",

}