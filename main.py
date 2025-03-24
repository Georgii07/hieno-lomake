from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/")
def root():
    nimi = request.cookies.get('nimi')
    if nimi:
        return render_template('vastaus.html', nimi=nimi)

    return render_template('lomake.html')

@app.route("/vastaus", methods=["POST"])
def vastaus():
    nimi = request.form.get('nimi')
    email = request.form.get('email')

    if not nimi or not email:
        return "Täytä kaikki kentät!", 400

    resp = make_response(render_template('vastaus.html', nimi=nimi, email=email))
    resp.set_cookie('nimi', nimi, max_age=60*60*24)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
