import requests
import time

DB_BASE_URL = "a0zai-56c3a-default-rtdb.europe.west1.firebasedatabase.app-A0Z_CORE" 
CMD_URL = f"{DB_BASE_URL}/current_command.json"

def send_command(command_text):
    """دالة لإرسال الأمر إلى السيرفر"""
    payload = {
        "text": command_text,
        "timestamp": int(time.time() * 1000)
    }
    try:
        response = requests.put(CMD_URL, json=payload)
        if response.status_code in [200, 201, 204]:
            print(f"\n[+] تم إرسال الأمر بنجاح: {command_text}")
        else:
            print(f"\n[-] فشل الإرسال (رمز الاستجابة: {response.status_code})")
    except Exception as e:
        print(f"\n[-] حدث خطأ أثناء الاتصال بالسيرفر: {e}")

def main_menu():
    while True:
        print("\n=================================")
        print("    Shadow Control Panel v1.0    ")
        print("=================================")
        print("1. إعادة تشغيل الجهاز (Restart)")
        print("2. إيقاف تشغيل الجهاز (Shutdown)")
        print("3. تشغيل أغنية / فيديو على يوتيوب")
        print("4. فتح برنامج الرسام (Paint)")
        print("5. فتح المفكرة (Notepad)")
        print("6. فتح متصفح جوجل كروم (Chrome)")
        print("7. إرسال أمر موجّه أوامر خاص (Custom CMD)")
        print("8. الضغط على اختصار مفاتيح (Hotkey Press)")
        print("0. خروج")
        print("---------------------------------")
        
        choice = input("اختر رقم الخيار: ").strip()

        if choice == "1":
            send_command("/cmd shutdown /r /t 5")

        elif choice == "2":
            send_command("/cmd shutdown /s /t 5")

        elif choice == "3":
            url = input("أدخل رابط الأغنية/الفيديو (أو اضغط Enter للتشغيل الافتراضي): ").strip()
            if not url:
                url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            send_command(f"/cmd start {url}")

        elif choice == "4":
            send_command("/cmd mspaint")

        elif choice == "5":
            send_command("/cmd notepad")

        elif choice == "6":
            send_command("/cmd start chrome")

        elif choice == "7":
            cmd = input("أدخل أمر النظام الخاص الذي تريد تنفيذه: ").strip()
            if cmd:
                send_command(f"/cmd {cmd}")

        elif choice == "8":
            keys = input("أدخل المفاتيح تفصل بينها مسافات (مثال: ctrl alt delete أو space): ").strip()
            if keys:
                send_command(f"/press {keys}")

        elif choice == "0":
            print("إغلاق لوحة التحكم...")
            break
        else:
            print("خيار غير صحيح، حاول مجدداً.")

        time.sleep(1)

if __name__ == "__main__":
    main_menu()
