from flask import Flask, render_template
app - flask (__name__)


@app.route("/")
def index():
    nombre = "Ricardo"
    edad = 16
    lista_cosas = ["programar","tocar algun instrumento", "jugar"]
    datos = {"curso": "Python pro", "duracion": "10 meses"}
    return render_template("index.html",nombre=nombre, edad=edad, lista=lista_cosas,datos=datos)

app.run(debug=True)
