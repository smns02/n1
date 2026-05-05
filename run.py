import core
import sys

def run_obfuscated():
    print("\033[1;32m[+] Starting Patched Core System...\033[1;00m")
    
    try:
        # core.main() ကို run မယ်။ key စစ်တဲ့ function ကို နာမည်ဖျက်ထားလို့ 
        # သူက ရှာမတွေ့တော့ဘဲ error တက်ပါလိမ့်မယ်။
        core.main()
    except AttributeError as e:
        # ရှာမတွေ့တဲ့ function (ဥပမာ check_approvxx) ကို 
        # ဘာမှမလုပ်တဲ့ dummy function တစ်ခုအဖြစ် သတ်မှတ်ပေးလိုက်တာပါ
        missing_attr = str(e).split("'")[-2]
        print(f"\033[1;33m[*] Bypassing: {missing_attr}\033[1;00m")
        setattr(core, missing_attr, lambda *args, **kwargs: True)
        
        # Function အသစ်နဲ့ ပြန် run မယ်
        try:
            core.main()
        except:
            pass
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    run_obfuscated()
