import pymysql

class Todo:
    def __init__(self,title,importance,tid=None):
        self.title=title
        self.importance=importance
        self.tid=tid
    def __str__(self):
        return f'{"+"*self.importance:10s} {self.title}'

def connect():
    connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            #password='root',
            database='todoapp',
            cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def find_all():
    todo_list=[]
    with connect() as con:
        with con.cursor() as cursor:
            sql ='SELECT * FROM todos ORDER BY importance DESC'
            cursor.execute(sql)
            rs = cursor.fetchall()

            for r in rs:
                todo_list.append(Todo(r['title'],r['importance'],r['tid']))
            
    return todo_list

def insert_one(todo):
    with connect() as con:
        with con.cursor() as cursor:
            sql='INSERT INTO todos(title,importance) VALUES(%s,%s)'
            cursor.execute(sql,(todo.title,todo.importance))
        con.commit()

def update_one(todo):
    with connect() as con:
        with con.cursor() as cursor:
            sql='UPDATE todos SET title=%s,importance=%s WHERE tid = %s'
            cursor.execute(sql,(todo.title,todo.importance,todo.tid))
        con.commit()

def delete_one(todo):
    with connect() as con:
        with con.cursor() as cursor:
            sql='DELETE FROM todos WHERE tid = %s'
            cursor.execute(sql,(todo.tid))
        con.commit()

