import os
import threading
import time

import globals
from auth import *
from batch import *
from storage import *
from utils import *

from googleapiclient.discovery import build

def main():
    threading.Thread(target=pause_listener, daemon=True).start()

    load_save_json()
    creds = get_credentials()
    service = build('gmail', 'v1', credentials=creds)

    while True:
        if globals.paused:
            time.sleep(1)
            continue
        
        print(f"{GREY}---------------------------------------------------------{RESET}")
        print(f"{GREY}---------------------------------------------------------{RESET}")

        messages = get_message_batch(service)

        if(len(messages) == 0):
            print("Email's purged successfully")
            print(f"{CYAN}Emails deleted: {globals.total_del}{RESET}")
            print(f"{GREEN}Total bytes deleted: {globals.total_size/ (1024*1024):.2f} MB {RESET}")
            break

        msg_ids = batch_info(service, messages)

        print(f"{GREY}---------------------------------------------------------{RESET}")

        batch_delete_messages(service, msg_ids)

        os.system('cls')

        print(f"{GREY}---------------------------------------------------------{RESET}")
        print(f"{GREY}---------------------------------------------------------{RESET}")
        print(f"{CYAN}Emails deleted: {globals.total_del}{RESET}")
        print(f"{GREEN}Total bytes deleted: {globals.total_size/ (1024*1024):.2f} MB {RESET}")
        save_progress()

if __name__ == "__main__":
  main()






