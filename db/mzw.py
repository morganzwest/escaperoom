import hashlib, uuid, re, mysql.connector, firebase_admin, os
from colorama import Fore, init
from firebase_admin import db


def error_output(err):
    print(Fore.RED, err, Fore.RESET)


class Firebase(object):
    def __init__(self, url: str, key_path: str):
        """
        :url = The firebase url to connect to
        :key_path = the direct path going to the local system auth key for the database
        :return = null
        """
        cred = firebase_admin.credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred, {
            "databaseURL": url
        })

    @staticmethod
    def save(ref: str, dict_output):
        """
        Save dict input into the database with the F1API '.push()'
        :param ref: The root path for the save
        :param dict_output: The input
        :return: null
        """
        _t = firebase_admin.db.reference(ref).push(dict_output)

    @staticmethod
    def load(path="/"):
        """
        Load the data into a dict
        :param path: the root path
        :return: dict
        """
        return firebase_admin.db.reference(path).get()

    @staticmethod
    def update(path: str, dict_update):
        """
        Update a path continuous
        :param path: root path
        :param dict_update: dict to push
        :return: null
        """
        ref = firebase_admin.db.reference(path)
        ref.update(dict_update)


class SQL:
    def __init__(self, host, user, password, database=""):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        self.cursor = self.db.cursor()

    def execute(self, query: str, val = ""):
        """
        Execute the SQL Query
        :param query: the SQL query needed to execute
        :param val: any other variable input
        :return: null
        """
        if val == "":
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, val)

    def executemany(self, queries, val):
        """
        Execute an array of SQL queries
        :param queries: array of SQL queries
        :param val: other variable to input
        :return: null
        """
        self.cursor.executemany(queries, val)

    def commit(self):
        """
        Update the database
        :return: null
        """
        self.db.commit()

    def fetch(self):
        """
        fetch the results/records from the last execute
        :return: array of records
        """
        return self.cursor.fetchall()

    def rowcount(self):
        """
        Get the row count of the record update
        :return: int
        """
        return self.cursor.rowcount()

    def lastrowid(self):
        """
        gets the Row ID of the last commit change
        :return: int
        """
        self.cursor.lastrowid()


class Password:
    @staticmethod
    def check_password(hashed_password: str, user_password: str):
        """
        Compare the two passwords
        :param hashed_password: hashed string
        :param user_password: raw input
        :return: bool (true if same else false)
        """
        # splits the salt so the decrypt can find the original
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

    @staticmethod
    def hash_password(password: str):
        """
        Encrypts the password
        :param password: raw input
        :return: string
        """
        salt = uuid.uuid4().hex  # hex:bin represent
        # encode it to hashed hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


class Auth:
    def __init__(self, auto = False):
        """
        If auto is True then the class will automatically register and login via the menu
        """
        self.auto = auto

    def setup(self, main_menu, database_post, password_restrictons = {"len": 5, "uppercase": True, "lowercase": True, "symbols": True, "numbers": True}, data = {}, sqldatabase = None):
        self.main_menu = main_menu
        self.password_restrictons = password_restrictons

        self.data = data
        self.sqldatabase = sqldatabase

        self.database_post = database_post
        self.pass_hash = True

        # Connect to main menu
        # Enforce Password Restrictions
        # Switch between email or username
        # Switch databases

        # Adaptable to full preview or just returns
        # Get multiple return types

    def go_to_mainmenu(self):
        self.main_menu()

    def signup_email(self):
        i = 0
        while True:
            i = 0
            usemail = input("Email: ").strip().lower()
            if len(usemail) > 0:
                i += 1
                if usemail[-1] != ".":
                    i += 1
            if "@" in usemail:
                i += 1
            if "." in usemail:
                i += 1

            if i < 4:
                error_output("Invalid Email")
                continue

            for email in self.data:
                if email == usemail:
                    error_output("Account already created with the same email.")
            break
        return usemail

    def signup_password(self):
        while True:
            uspass = input("Password: ").strip()

            error, valid = "", True

            if len(uspass) < self.password_restrictons["len"]:
                valid, error = False, "Password must be {} chars or longer.".format(self.password_restrictons["len"])
            if self.password_restrictons["uppercase"] and not re.search("[A-Z]", uspass):
                valid, error = False, "Password must be {} chars or longer.".format(self.password_restrictons["len"])
            if self.password_restrictons["lowercase"] and not re.search("[a-z]", uspass):
                valid, error = False, "Password must include a lowercase char."
            if self.password_restrictons["numbers"] and not re.search("[0-9]", uspass):
                valid, error = False, "Password should include a digit"
            if self.password_restrictons["symbols"] and not re.search("[.-_]", uspass):
                valid, error = False, "Password should include a symbol"

            if valid:
                break
            if not valid:
                error_output("Invalid Password: " + error)
        return uspass

    def signup(self, ret = False):
        email = self.signup_email()
        password = self.signup_password()

        password_class = Password()
        password = password_class.hash_password(password) if self.pass_hash else password

        if ret:
            return email, password
        else:
            self.database_post(
                (email, password)
            )

    def login_run(self):
        i, b = 0, False
        while True:
            i = 0
            usemail = input("Email: ").strip().lower()
            if len(usemail) > 0:
                i += 1
                if usemail[-1] != ".":
                    i += 1
            if "@" in usemail:
                i += 1
            if "." in usemail:
                i += 1

            if i < 4:
                error_output("Invalid Email")
                continue

            for email in self.data:
                if email == usemail:
                    b = True
                    break
            if b:
                error_output("Account with that email does not exist.")


    def menu(self):
        os.system("cls")
        print("\n", "#","-"*16, " MENU ", "-"*16,"#\n")
        print("\t" * 4, "1.  LOGIN")
        print("\t" * 4, "2.  SIGNUP")
        print("\t" * 4, "3.  QUIT\n")
        print("#","-"*16,
              (" " * ((len(" MENU ") - len("FOOTER")) // 2)) + "FOOTER" + (" " * ((len(" MENU ") - len("FOOTER")) // 2))
            , "-"*16,"#\n")

        # Input checker
        trys = 0
        while trys < 2:
            choice = input(" > ")
            if choice == "1":
                self.login()
                break
            elif choice == "2":
                self.signup()
                break
            elif choice == "3":
                quit(2)
            else:
                trys += 1
                error_output("Invalid input: %s" % choice)
        else:
            self.menu()


if "__name__" == __name__:
    init()

