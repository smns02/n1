import asyncio
import sys
import sky

async def main():
    """
    Key စစ်ဆေးခြင်း အဆင့်များကို ကျော်ဖြတ်ပြီး 
    Core function ဖြစ်သော InternetAccess ကို တိုက်ရိုက် run သည့် Main function
    """
    try:
        # Device ID သို့မဟုတ် System Key ယူသည့် အပိုင်း (လိုအပ်လျှင်)
        # ၎င်းသည် Key တောင်းခြင်းမဟုတ်ဘဲ System Identity အတွက်ဖြစ်နိုင်သဖြင့် ထားခဲ့ပါမည်
        try:
            device_id = sky.get_system_key()
        except Exception:
            pass

        print("\033[1;32m[+] Bypassing authentication...\033[1;00m")
        print("\033[1;32m[+] Starting Internet Access Engine...\033[1;00m")

        # Key validation system ကို ကျော်ပြီး execute လုပ်ခြင်း
        bypass_engine = sky.InternetAccess() 
        await bypass_engine.execute()

    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[1;00m")

if __name__ == "__main__":
    try:
        # Low-end device များပါ အဆင်ပြေစေရန် loop ကို တိုက်ရိုက် run ခြင်း
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Stopped by user.\033[1;00m")
        sys.exit()
