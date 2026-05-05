import sys
import types

# ၁။ core ကို အရင် import မလုပ်ခင် dummy function တချို့ ပြင်ဆင်မယ်
def dummy_true(*args, **kwargs):
    return True

# ၂။ core ကို import လုပ်မယ်
try:
    import core
except ImportError:
    print("[!] core.so ကို ရှာမတွေ့ပါ။ ဖိုင်လမ်းကြောင်း မှန်မမှန် စစ်ပါ။")
    sys.exit()

def bypass():
    print("\033[1;36m[*] Target: Ruijie Voucher Bypass\033[1;00m")
    print("\033[1;32m[*] Patching compiled logic...\033[1;00m")

    # Cython module ထဲက variable တွေ သို့မဟုတ် function တွေကို override လုပ်မယ်
    # အဓိကအားဖြင့် approval စစ်တတ်တဲ့ function နာမည်တွေကို အမြဲ True ပေးလိုက်တာပါ
    target_hooks = [
        'check_approval', 'validate_key', 'check_status', 
        'is_registered', 'auth_check', 'verify'
    ]

    for hook in target_hooks:
        if hasattr(core, hook):
            setattr(core, hook, dummy_true)
            print(f"\033[1;32m[+] Hooked: {hook}\033[1;00m")

    # ပြဿနာက .so ထဲမှာ Key logic က hardcoded ဖြစ်နေရင် direct function ကိုပဲ ခေါ်ရပါမယ်
    try:
        print("\033[1;33m[*] Attempting to trigger core bypass...\033[1;00m")
        
        # main() ကို မခေါ်ခင် လိုအပ်တဲ့ setup တွေကို လုပ်ကြည့်မယ်
        # Ruijie tool တွေမှာ များသောအားဖြင့် start_process() သို့မဟုတ် execute() ပါတတ်ပါတယ်
        
        if hasattr(core, 'start_process'):
            core.start_process()
        elif hasattr(core, 'execute'):
            core.execute()
        else:
            # တကယ်လို့ ဘာမှမရှိရင် main() ကိုပဲ Patch လုပ်ထားတဲ့ function တွေနဲ့ run မယ်
            core.main()
            
    except Exception as e:
        print(f"\033[1;31m[!] Execution Error: {e}\033[1;00m")

if __name__ == "__main__":
    try:
        bypass()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Stopped.\033[1;00m")
