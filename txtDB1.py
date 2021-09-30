#
# Python dB Assignment
#
# Author:   Beatrice Owens

#import sqlite3 and form a connection to the dB
import sqlite3
conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtDoc(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_txtFile TEXT)")
    conn.commit()

conn = sqlite3.connect('test2.db')

#fileList tuple
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#Loop through tuple objects to find those ending in ".txt"
for doc in fileList:
    if doc.endswith('.txt'):#only complete the following code if each doc ending in .txt
        with conn:
            cur = conn.cursor()
            #(doc,) denotes a one element tuple for each file ending in .txt
            #insert files into dB
            cur.execute("INSERT INTO tbl_txtDoc (col_txtFile) VALUES (?)", (doc,))
            print(doc)

conn.close()
