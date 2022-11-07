# rrender_templateのインストール
from flask import Flask, redirect, render_template, request, url_for

from setting import Customer, session

app = Flask(__name__)


@app.route("/index")
def index():
    # customers = Customer.select()
    customers = session.query(Customer).all()
    return render_template("index.html", customers=customers)


# ユーザー追加のルーティング(POSTでアクセス限定)
@app.route("/add", methods=["POST"])
def add_customer():
    """新規顧客を追加する関数"""
    # フォーム入力されたnameとageを値に受け取る
    name = request.form["name"]
    age = request.form["age"]

    customer = Customer()
    customer.name = name
    customer.age = age
    session.add(customer)
    session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)
