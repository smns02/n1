import sys
import os

# ၁။ လိုအပ်တဲ့ core ကို အရင်သွင်းမယ်
try:
    import core
except ImportError:
    print("[!] core.so not found!")
    sys.exit()

# ၂။ Key စစ်တဲ့ နေရာမှာ Error မတက်အောင် လိမ်ညာမယ့် Class
class BypassData:
    def __getattr__(self, name):
        return lambda *args, **kwargs: True

# ၃။ core module ထဲက အရာအားလုံးကို override လုပ်ဖို့ ကြိုးစားခြင်း
target_names = ['check_approval', 'validate_key', 'verify_key', 'is_auth', 'check_status']
for name in target_names:
    try:
        setattr(core, name, lambda *args, **kwargs: True)
    except:
        pass

if __name__ == "__main__":
    print("\033[1;32m[+] Forcing Bypass Engine...\033[1;00m")
    
    try:
        # AttributeError ကို ကျော်ဖို့ main() ကို try ထဲမှာ run ပါမယ်
        # key စစ်တဲ့ function က error တက်ရင်တောင် program ဆက်သွားအောင် လုပ်တာပါ
        
        # core.main() က attribute တွေ အများကြီး လိုနေတတ်လို့ 
        # အောက်ကအတိုင်း dummy objects တွေ ပေးကြည့်ပါမယ်
        try:
            core.status = "VERIFIED"
            core.expiry = "LIFETIME"
            core.authorized = True
        except:
            pass

        # အဓိက main logic ကို ခေါ်ခြင်း
        core.main()

    except AttributeError as e:
        # AttributeError တက်လာရင် ဘယ် function ကို ရှာမတွေ့တာလဲဆိုတာ ကြည့်ပြီး 
        # အဲ့ဒီ function ကို dummy အနေနဲ့ ထပ်ဖြည့်ပေးပါမယ်
        missing_attr = str(e).split("'")[-2]
        print(f"\033[1;33m[*] Fixing missing attribute: {missing_attr}\033[1;00m")
        setattr(core, missing_attr, lambda *args, **kwargs: None)
        
        # တတိယအကြိမ် ပြန် run ခြင်း
        try:
            core.main()
        except:
            print("\033[1;31m[!] Critical Error: Logic is hardcoded inside .so file.\033[1;00m")
            print("\033[1;36m[i] ဒီ .so က binary level မှာ protection တော်တော်မြင့်လို့ run.py နဲ့တင် မရတာပါ။\033[1;00m")

    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Stopped.\033[1;00m")
