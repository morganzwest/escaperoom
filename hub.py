import os
import time
from libs import errors
import db.mzw as mzw


# Check imports
def check():
    try:
        print("Loading...")
        time.sleep(0.3)

        import hashlib
        print("[-] Installing HashLib")
        time.sleep(0.1)

        import uuid
        print("[-] Installing UUID")
        time.sleep(0.1)

        import firebase_admin
        print("[-] Installing firebase-admin")
        time.sleep(0.1)

        from colorama import Fore, init
        print("[-] Installing Colorama and Children Nodes")
        time.sleep(0.1)

        from firebase_admin import db
        print("[-] Installing firebase-DB")
        time.sleep(0.1)

        init()

        print(f"{Fore.GREEN}\nLoad Completed.{Fore.RESET}")
        time.sleep(.5)
        os.system("cls")

    except ModuleNotFoundError:
        print("Error: Prerequisites missing. Attempting to install them now.", end = "")
        for x in range(5):
            time.sleep(.4)
            print(".", end = "")

        try:
            arr = ["hashlib", "uuid", "re", "mysql", "firebase_admin", "colorama", "firebase-admin"]
            for x in arr:
                os.system(f"pip install {x}")

            try:
                import hashlib, uuid, firebase_admin
                from colorama import Fore, init
                from firebase_admin import db

            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    "Python is not installed correctly. Please reinstall with Python added to path with Pip.")

        except:
            raise EnvironmentError(
                "Python is not installed correctly. Please reinstall with Python added to path with Pip.")


class CONSTANTScls:
    def __init__(self):
        self.DATABASE = {}

        # Private URL key
        with open("db/prv.lcs") as f:
            self.url = f.readlines()[0]

    def initialize_databases(self):
        self.DATABASE = mzw.Firebase(self.url, "db/key.json")


CONSTANTS = CONSTANTScls()


def delay_print(s):
    import sys
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)
