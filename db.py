import pandas as pd
import sqlite3


conn = sqlite3.connect('vocab.db')

c = conn.cursor()

c.execute("""CREATE TABLE vocab(
          word text,
          meaning text,
          shortdef text,
          longdef text,
          url text,
          done integer,
          mysentense text
          )""")

df = pd.read_csv('Data/wordlist-1000.csv')
for index, row in df.iterrows():
    c.execute("INSERT INTO vocab VALUES (:word, :meaning, :shortdef, :longdef, :url, :done, :mysentense)",
              {
                  'word': row['word'],
                  'meaning': row['meaning'],
                  'shortdef': row['short definition'],
                  'longdef': row['long definition'],
                  'url': row['url'],
                  'done': 0,
                  'mysentense': ''
              })

# c.execute("INSERT INTO vocab VALUES (:word, :meaning, :shortdef, :longdef, :url)",
#           {
#               'word': 'onasdfe',
#               'meaning': 'sdwefwffa',
#               'shortdef': 'saweef232df',
#               'longdef': 'dwwerwerwfd',
#               'url': 'sdiwfw2342234nwsd'
#           })

# arr = []
# c.execute("SELECT *, oid FROM vocab WHERE done = 1")
# arr = c.fetchall()
# print(len(arr))



conn.commit()
conn.close()
