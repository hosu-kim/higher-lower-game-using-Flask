from flask import Flask
from random import randint
app = Flask(__name__)


@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWZ3ZGM1OWg1anp3MmczM3RzcHZ0aHg3MnJ6eGxoNXkw"
            "OXg2ZnE5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Kehzyp9EFa2IYDte8P/giphy.gif'>")


rannum = randint(0, 10)


@app.route("/<int:number>")
def your_guess(number):

    if number < rannum:
        return "<h1 style='color: red'>Too low, try again.<h1><img " \
               "src='https://giphy.com/clips/originals-drag-teacher-math-is-a-nFOHkp7mvJCSA5rFCt'>"
    elif number == rannum:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnEwY25menJzenJ3d2M" \
               "wYXAwY3QxbnBsajgxa3liamhyZGI5OW10aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QyK8gRzGW2fV6qo8Hm/giphy.gif'>"

    else:
        return "<h1 style='color: red'>Too high, try again.<h1>" \
               "<img src'https://media.giphy.com/media/2tR6cOaZeXzR6x5z6S/giphy.gif?ci" \
               "d=790b7611zxdwghgpdghbwpjz74im4xh5nq5z689hp2x7krdw&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

if __name__ == "__main__":
    app.run(debug=True)
