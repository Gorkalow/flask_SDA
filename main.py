from flask import Flask, render_template, request, redirect

app = Flask('flask_SDA')


@app.route('/hey')
def hey():
    return "Hey!"


@app.route("/home")
def home():
    return render_template('home.html', title='Home', user='Mateusz', texts=['Jesteś', 'szlachetnym', 'człowiekiem'])


@app.route("/")
def form():
    return render_template('formularz.html')


@app.route("/send", methods=["GET", "POST"])
def send():
    imie = request.form['name']
    wiek = request.form['age']
    ocena = request.form['score']
    file = request.files['picture']
    file.save(f'C:/Users/sasha/PycharmProjects/flask_SDA/saved_files/{file.filename}')
    # Poprawny(bezpieczny) sposób przekierowania zamiast if POST else albo powonego renderingu.
    # Najpierw wysyła POST request, później GET, przekierowując z powrotem
    return redirect('/')



imiona = []
print(imiona)

@app.route("/base", methods=["GET", "POST"])
def form_xss():
    if request.method == "POST":  # jeśli wysłano formularz
        imiona.append(request.form['name'])  # dopisz imię do listy imion
        return redirect('/show_names')  # i przekieruj na listę imion
    return render_template("base.html")


@app.route("/show_names")
def send_xss():
    return render_template('users.html', imiona=imiona)

print(imiona)
if __name__ == "main":
    app.run(debug=True)
