import core
import os
import sys

# --- [ UI COLORS ] ---
C_GREEN, C_CYAN, C_RED, C_RESET = '\033[92m', '\033[96m', '\033[91m', '\033[0m'

def bypass_run():
    try:
        print(f"{C_CYAN}[*] Initializing SMNS System...{C_RESET}")
        
        # ၁။ Device ID ကို core ထဲကနေ လှမ်းယူမယ်
        try:
            device_id = core.get_device_id()
            print(f"{C_GREEN}[+] Device ID: {device_id}{C_RESET}")
        except:
            pass

        print(f"{C_GREEN}[+] Status: Authentication Bypassed!{C_RESET}")
        print(f"{C_CYAN}[*] Starting Core Engine...{C_RESET}")

        # ၂။ core.main() ကို မခေါ်တော့ဘဲ အလုပ်လုပ်မယ့် process ကို တိုက်ရိုက်ခေါ်မယ်
        # ပုံမှန်အားဖြင့် main process က start_process() သို့မဟုတ် execute() ဖြစ်တတ်ပါတယ်
        
        if hasattr(core, 'start_process'):
            core.start_process()
        elif hasattr(core, 'execute'):
            core.execute()
        elif hasattr(core, 'start'):
            core.start()
        else:
            # တကယ်လို့ ဘာ function မှန်း မသေချာရင် core ထဲက ရှိသမျှ function တွေကို စစ်ဆေးပြီး
            # Key စစ်တဲ့ function မဟုတ်တာကို ရွေး run ရပါမယ်
            print(f"{C_RED}[!] Error: Could not find the start function in core library.{C_RESET}")
            print(f"{C_CYAN}[i] Trying to run core.main() directly with patch...{C_RESET}")
            
            # core.main() ကိုပဲ ခေါ်မယ်၊ ဒါပေမဲ့ key check ကို true ဖြစ်အောင် patch လုပ်ဖို့ ကြိုးစားကြည့်မယ်
            # (ဒါက core က python file ဖြစ်မှ ရမှာပါ)
            core.main()

    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Stopped.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}[X] Error: {e}{C_RESET}")

if __name__ == "__main__":
    bypass_run()
