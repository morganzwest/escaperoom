import libs.db.mzw
from libs import hub

"""with open("db/prv.lcs") as f:
    url = f.readlines()[0]

DATABASE = db.mzw.Firebase(url, "db/key.json")

DATABASE.update("/", {
    "game": {
        "0": {
            "answers": {
                "clue1": "Drury Lane",
                "clue2": "Kings Cross"
            },
            "failedanswers": {
                "clue1": ["Filler"],
                "clue2": ["Filler"]
            }
        }
    }
})"""

hub.CONSTANTS.initialize_databases()


Authentication = libs.db.mzw.Auth()
Authentication.setup(
    main_menu = None,
    password_restrictons = {"len": 5,
                                "uppercase": False,
                                "lowercase": False,
                                "symbols": False,
                                "numbers": True},
    data = None,
    sqldatabase = None,
    database_post = None
)

# Create EMAIL TUPLE 2D Array
array = []
keys = list(hub.CONSTANTS.DATABASE.load("/users/"))

for key in keys:
    email = key.split(":")[-1].replace("DOT", ".")
    password = hub.CONSTANTS.DATABASE.load(f"/users/{key}")["password"]
    array.append(
        (email, password)
    )
# End
for x in array: print(x)
Authentication.login_run(array)