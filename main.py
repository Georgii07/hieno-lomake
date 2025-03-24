from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("lomake.html")

#name = input("Anna nimesi: ")
#age = input("Anna ikäsi: ")
#print(f"Hei {name}, olet {age} vuotta vanha!")

if __name__ == '__main__':
    app.run(debug=True)