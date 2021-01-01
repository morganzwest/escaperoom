import hub

hub.check()
hub.CONSTANTS.initialize_databases()

"""print(f"{hub.Fore.BLUE}\n", hub.CONSTANTS.DATABASE.load("/game/0/name"), f"{hub.Fore.RESET}")

hub.delay_print(
    hub.CONSTANTS.DATABASE.load("/game/0/parts/intro")
)"""


def create_account(email: str, password: str, username: str):
    temp = hub.CONSTANTS.DATABASE.load("/users/")
    string = username + ":" + email.replace(".", "DOT")
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
        Authentication.login_run(array)


menu()
hub.time.sleep(50)
