import os
import sys

# ၁။ လိုအပ်တဲ့ Library ရှိမရှိ အရင်စစ်မယ်
try:
    import requests
except ImportError:
    print("[*] Installing requests library...")
    os.system("pip install requests")
    import requests

# ၂။ .so ဖိုင်ကို Import လုပ်မယ်
try:
    import device34Neko
except ImportError as e:
    print(f"\n[!] Error: .so ဖိုင်ကို Import လုပ်လို့မရပါ။")
    sys.exit()

# ၃။ အစီအစဉ်ကို စတင်မယ်
if __name__ == "__main__":
    try:
        print("\033[1;32m[+] Bypassing Key System...\033[1;00m")
        
        # device34Neko.check_approval() ကို ကျော်ပြီး 
        # Bypass လုပ်တဲ့ function ကို တိုက်ရိုက်ခေါ်ပါမယ်
        
        try:
            # Key စစ်တဲ့ function ကို မခေါ်တော့ဘဲ အလုပ်လုပ်မယ့် function ကို တန်းခေါ်ခြင်း
            device34Neko.start_bypass()
            
        except Exception as e:
            print(f"[!] တိုက်ရိုက် Run ရာတွင် အဆင်မပြေပါ: {e}")
            
    except KeyboardInterrupt:
        print("\n[!] အစီအစဉ်ကို ရပ်ဆိုင်းလိုက်ပါပြီ။")
        sys.exit()
