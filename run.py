import sys
import asyncio
import threading
import sky

if __name__ == "__main__":
    # check_approval() နေရာမှာ True လို့ တိုက်ရိုက်ပြောင်းပါ
    if True: 
        # threading line ကို လိုအပ်ရင် comment ပိတ်ထားနိုင်ပါတယ် (Error တက်ခဲ့ရင်)
        # threading.Thread(target=sky.continuous_auth_check, daemon=True).start()
        
        try:
            asyncio.run(sky.InternetAccess().execute())
        except KeyboardInterrupt:
            print("\n\033[1;31m[!] Stopped.\033[1;00m")
    else:
        sys.exit()
