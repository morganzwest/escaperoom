from libs import hub

hub.check()
hub.CONSTANTS.initialize_databases()


def create_account(email: str, password: str, username: str):
    while True:
        try:
            string = username + ":" + email.replace(".", "DOT")
            print(string, password, username)
            hub.CONSTANTS.DATABASE.update("/users/", {
                string: {
                    "billing": "#",
                    "games":
                        {
                            "paid": "#",
                            "progress": {
                                "0": "FILLER"
                            }
                        },
                    "password": password,
                    "username": username
                }
            })
            break
        except:
            hub.mzw.error_output("Invalid username. Make sure your username does not contain any symbols.")
            username = input("Username: ")
            continue

def loggedmenu():
    pass

def menu():
    Authentication = hub.mzw.Auth()
    Authentication.setup(
        main_menu = None,
        password_restrictons = {"len": 5,
                                "uppercase": False,
                                "lowercase": False,
                                "symbols": False,
                                "numbers": True},
        data = hub.CONSTANTS.DATABASE.load("/users/"),
        sqldatabase = None,
        database_post = create_account
    )

    print("MAIN MENU")
    print("- Login")
    print("- Signup")
    x = input(" > ")

    if x.lower().strip() == "signup":
        Authentication.signup()
        print("Signup complete. Now login with the same credentials.")
        hub.time.sleep(.5)
        menu()

    if x.lower().strip() == "login":

        # Create EMAIL TUPLE 2D Array
        array = []
        keys = list(hub.CONSTANTS.DATABASE.load("/users/"))

        for key in keys:
            email = key.split(":")[-1].replace("DOT", ".")
            password = hub.CONSTANTS.DATABASE.load(f"/users/{key}")["password"]
            array.append(
                (email, password, f"/users/{key}/")
            )
        # End
        hub.CONSTANTS.PATH = Authentication.login_run(array)
        hub.CONSTANTS.ACCOUNT_DATA = hub.CONSTANTS.DATABASE.load(hub.CONSTANTS.PATH)
        loggedmenu()

menu()
hub.time.sleep(50)
