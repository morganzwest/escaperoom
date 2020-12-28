import db.mzw as mzw


class CONSTANTScls:
    def __init__(self):
        self.DATABASE = {}

        # Private URL key
        with open("db/prv.lcs") as f:
            self.url = f.readlines()[0]

    def initialize_databases(self):
        self.DATABASE = mzw.Firebase(self.url, "db/key.json")


CONSTANTS = CONSTANTScls()
