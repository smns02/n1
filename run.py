import sys
import os

# ၁။ လိုအပ်တဲ့ Library တွေကို Mock လုပ်ဖို့ ပြင်ဆင်ခြင်း
class MockResponse:
    def __init__(self):
        self.status_code = 200
        self.text = '{"status": "success", "expiry": "2099-12-31"}'
    def json(self):
        return {"status": "success", "expiry": "2099-12-31", "authorized": True}

def mock_get(*args, **kwargs):
    return MockResponse()

def mock_input(*args, **kwargs):
    return "BYPASS-KEY-12345"

# ၂။ Python ရဲ့ built-in function တွေကို Override လုပ်ပြီး လိမ်ညာမယ်
import builtins
builtins.input = mock_input  # Key တောင်းရင် ဒီ fake key ကို အလိုလို ထည့်ပေးမယ်

try:
    import requests
    requests.get = mock_get    # Server ဆီ Key စစ်ရင် Success ပဲ ပြန်ခိုင်းမယ်
    requests.post = mock_get
except:
    pass

# ၃။ core module ကို import လုပ်ပြီး run မယ်
try:
    print("\033[1;32m[+] Patching Ruijie Protection...\033[1;00m")
    import core
    
    # .so ထဲမှာ ပါလေ့ရှိတဲ့ variable တွေကို force ပြောင်းမယ်
    try:
        core.authorized = True
        core.status = "VERIFIED"
    except:
        pass

    print("\033[1;32m[+] Attempting to launch core...\033[1;00m")
    
    # core.main() ထဲမှာ logic အကုန်ရှိနေတာမို့ သူ့ကိုပဲ ခေါ်ရမှာပါ
    core.main()

except KeyboardInterrupt:
    print("\n\033[1;31m[!] Stopped.\033[1;00m")
except Exception as e:
    # တကယ်လို့ core.main() က attribute error တက်ရင် core.start_process() စမ်းပါ
    try:
        core.start_process()
    except:
        print(f"\033[1;31m[!] Error: {e}\033[1;00m")
