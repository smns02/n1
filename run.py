import Sell
import sys

# ရှာတွေ့သမျှ check_key နာမည်အသစ်တွေကို ဒီမှာ dummy ပေးထားပါ
# (ဥပမာ - နာမည် ၃ နေရာတွေ့ရင် ၃ ခုလုံးကို override လုပ်ပါမယ်)
def bypass_setup():
    dummy = lambda *a, **k: True
    
    # Sell module ထဲမှာရှိတဲ့ function တွေကို စစ်ထုတ်ပြီး auto-patch လုပ်တာပါ
    for attr in dir(Sell):
        if "check_k" in attr:  # သင်ပြောင်းလိုက်တဲ့ နာမည်အစနဲ့ တိုက်စစ်ပါ
            setattr(Sell, attr, dummy)
            print(f"[*] Patched internal function: {attr}")

if __name__ == "__main__":
    bypass_setup()
    print("[+] Launching Sell Tool with patches...")
    try:
        # main loop ကို စခိုင်းပါမယ်
        # dir(Sell) ထဲမှာ main() မပါရင် အခြား function တစ်ခုခုကို ခေါ်ကြည့်ပါ
        Sell.main() 
    except Exception as e:
        print(f"[!] Error: {e}")
