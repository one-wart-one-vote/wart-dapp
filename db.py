import sqlite3


class DB:
    def __init__(self):
        self.con = sqlite3.connect("wartwallet.db", check_same_thread=False)
        with self.con:
            self.con.execute("""CREATE TABLE IF NOT EXISTS wallets (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            address TEXT,
                            pk TEXT,
                            salt TEXT,
                            last_balance TEXT NOT NULL DEFAULT '0'
                        );""")
            self.con.execute("""CREATE TABLE IF NOT EXISTS friends (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            address TEXT,
                            friend TEXT
                        );""")
            self.con.execute("""CREATE TABLE IF NOT EXISTS data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            key TEXT,
                            value TEXT
                        );""")
            r = self.con.execute("SELECT COUNT() FROM data;")
            c = r.fetchone()[0]
            if c == 0:
                self.con.execute("INSERT INTO data (key, value) VALUES ('peer', 'http://localhost:3000');")

    def get_wallets(self):
        with self.con:
            r = self.con.execute("SELECT * FROM wallets;")
            data = r.fetchall()
            return data

    def get_name(self, friend):
        with self.con:
            r = self.con.execute(f"SELECT * FROM friends WHERE friend='{friend}';")
    def get_friends(self):
        with self.con:
            r = self.con.execute("SELECT * FROM friends;")
            data = r.fetchall()
            print(data)
            return data

    def insert_friend(self,addr, friend):
        with self.con:
            self.con.execute(f"INSERT INTO friends (address,friend) VALUES ('{addr}', '{friend}');")

    def get_wallet_by_address(self, addr):
        with self.con:
            r = self.con.execute(f"SELECT * FROM wallets WHERE address='{addr}';")
            data = r.fetchone()
            return data

    def insert_wallet(self, addr, pk, salt):
        with self.con:
            self.con.execute(f"INSERT INTO wallets (address, pk, salt) VALUES ('{addr}', '{pk}', '{salt}');")

    def update_balance(self, addr, balance):
        with self.con:
            self.con.execute(f"UPDATE wallets SET last_balance='{balance}' WHERE address='{addr}';")

    def delete_wallet(self, addr):
        with self.con:
            self.con.execute(f"DELETE FROM wallets WHERE address='{addr}';")

    def update_peer(self, peer):
        with self.con:
            self.con.execute(f"UPDATE data SET value='{peer}' WHERE key='peer';")

    def get_peer(self):
        with self.con:
            r = self.con.execute(f"SELECT * FROM data WHERE key='peer';")
            data = r.fetchone()
            return data[2]
