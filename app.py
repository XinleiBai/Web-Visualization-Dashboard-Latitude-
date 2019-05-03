from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my API!"

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Name and current location"


@app.route("/contact")
def contact():
    print("Server received request for 'contact' page...")
    return "please email to baixinlei2008@gmail.com"

if __name__ == "__main__" :
    # print('test')
    app.run(debug=True,port=5001)

