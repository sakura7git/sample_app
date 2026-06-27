from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# 入力画面
@app.route('/')
def form():
    return render_template('form.html')

# 確認画面
@app.route('/confirm', methods=['POST'])
def confirm():
    gender = request.form.get('gender')
    age = request.form.get('age')
    comment = request.form.get('comment')

    return render_template(
        'confirm.html',
        gender=gender,
        age=age,
        comment=comment
    )

# 送信完了＋DB保存
@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if request.method == 'POST':
        gender = request.form.get('gender')
        age = request.form.get('age')
        comment = request.form.get('comment')

        conn = sqlite3.connect('survey.db')
        c = conn.cursor()

        c.execute(
            "INSERT INTO survey (gender, age, comment) VALUES (?, ?, ?)",
            (gender, age, comment)
        )

        conn.commit()
        conn.close()

    return render_template('thanks.html')

# 一覧表示（今回追加）
@app.route('/list')
def list():
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()

    c.execute("SELECT * FROM survey")
    data = c.fetchall()

    conn.close()

    return render_template('list.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
