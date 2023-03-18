import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()
    def get_Time(self):
        query = 'SELECT * FROM Time'
        result = self.cursor.execute(query)
        Time = result = result.fetchall()
        return Time

    def add_new_Time(self, new_time):
        try:
            query = f'INSERT INTO Time(time) VALUES("{new_time}")'
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def remove_Time(self,time):
        try:
            query = f'DELETE FROM Time WHERE id = "{time}"'
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False

        
    def done_Time(self,new_time,last_time):
        try:
            query = f"UPDATE Time SET time='{new_time}' WHERE time ='{last_time}'"
            self.cursor.execute(query)
            self.con.commit()
            return True
        except:
            return False