from flask import Flask, render_template, url_for, make_response, request

##WSGI - приложение
app = Flask(__name__)

##Конфиг
SECRET_KEY = "4901396ecd45e9142b7d5369a3157eba3cca0c46c449dace5f7b35197c5c"
app.config.from_object(__name__) ##Грузим конфиг в приложение

##Обработчик главной страницы
@app.route("/", methods=["POST", "GET"])
def index():
    content = render_template("index.html", title="Главная")
    response = make_response(content, 200)

    return response

##Точка входа
if __name__ == "__main__":
    app.run("localhost", port=5001, debug=True)