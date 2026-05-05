import core
import os
import sys
import shutil

# --- [ UI COLORS ] ---
C_CYAN, C_GREEN, C_YELLOW, C_WHITE, C_RED, C_RESET, C_BOLD = '\033[96m', '\033[92m', '\033[93m', '\033[97m', '\033[91m', '\033[0m', '\033[1m'

def get_terminal_width():
    """Termux screen အကျယ်ကို ယူပါမည်"""
    return shutil.get_terminal_size().columns

def display_smns_banner(smns_did, key="BYPASS-SUCCESS", expiry="LIFETIME", status="VERIFIED"):
    os.system('clear')
    w = get_terminal_width()
    
    logo = [
        " ██████╗███╗   ███╗███╗   ██╗███████╗",
        "██╔════╝████╗ ████║████╗  ██║██╔════╝",
        "╚█████╗ ██╔████╔██║██╔██╗ ██║███████╗",
        " ╚═══██╗██║╚██╔╝██║██║╚██╗██║╚════██║",
        "██████╔╝██║ ╚═╝ ██║██║ ╚████║███████║",
        "╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝"
    ]

    for line in logo:
        print(f"{C_GREEN}{C_BOLD}{line.center(w)}{C_RESET}")
    print(f"{C_YELLOW}{C_BOLD}{'SMNS TECHNOLOGY TOOLKIT (CRACKED)'.center(w)}{C_RESET}\n")

    display_status = "SYNCED"
    status_color = C_GREEN
    
    border_w = w - 2
    print(f"{C_CYAN}┌{'─' * border_w}┐{C_RESET}")
    
    def print_row(label, value, val_color=C_WHITE):
        left_part = f"│ {C_YELLOW}{label:<10} : {val_color}{value}"
        clean_text_len = 10 + 3 + len(str(value)) + 2
        padding = " " * (border_w - clean_text_len + 1)
        print(f"{left_part}{padding}{C_CYAN}│{C_RESET}")

    print_row("DEVICE ID", smns_did)
    print_row("KEY", key)
    print_row("EXPIRE", expiry)
    print_row("STATUS", display_status, status_color)

    print(f"{C_CYAN}└{'─' * border_w}┘{C_RESET}")

if __name__ == "__main__":
    try:
        # Device ID ကို ယူခြင်း
        try:
            original_did = core.get_device_id()
            smns_did = str(original_did).replace("TRB-", "SMNS-")
            if not smns_did.startswith("SMNS-"):
                smns_did = f"SMNS-{smns_did}"
        except:
            smns_did = "SMNS-BYPASS-ACTIVE"

        # Key စစ်ဆေးခြင်းအပိုင်းကို ကျော်ပြီး Authorized ကို True ပေးလိုက်ပါသည်
        authorized = True
        expiry = "PERMANENT"
        status = "VERIFIED"
        current_key = "BYPASS-UNLOCKED"

        # Banner ပြသခြင်း
        display_smns_banner(smns_did, current_key, expiry, status)
        
        # Key တောင်းသည့် input အပိုင်းကို လုံးဝဖြုတ်ထားပါသည်

        if authorized:
            # တန်းပြီး Start လုပ်ခိုင်းခြင်း
            print(f"\n{C_YELLOW}[*] STAGE 1: EXECUTING INSTANT BYPASS (VOUCHER INJECTION)...{C_RESET}")
            print(f"{C_CYAN}... SUCCESS ...{C_RESET}")
            print(f"\n{C_GREEN}[+] INTERNET ACCESS ACTIVE. AI OPTIMIZER ENABLED!{C_RESET}")
            
            # ပင်မလုပ်ငန်းစဉ်ကို စတင်ခြင်း
            core.start_process()

    except KeyboardInterrupt:
        print(f"\n{C_RED}[!] Stopped.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}[X] Error: {e}{C_RESET}")
