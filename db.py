from flask import Flask,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
 
    query =  'SELECT * FROM data'
    con =sqlite3.connect('drowsiness_detection.db')
    cursorObj = con.cursor()
    cursorObj.execute(query)
    data = cursorObj.fetchall()

    con.commit()
    con.close()
    print('DB closed ')
    print(data[0])
    return render_template('index.html' , data = data)


if __name__ == '__main__':
    app.run(debug=True)