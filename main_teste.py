from flask import Flask, render_template, request, redirect
import Interface_teste
Interface_teste.teste()
app = Flask(__name__)

#paginas
@app.route('/')
def homepage():
    return render_template('index_teste.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    global formContato
    if request.method == 'POST':
        formContato = {"nome": request.form["nome"],
                       "fonte": request.form["dc"]}
    print(formContato)
    print(type(formContato["nome"]))
    print(type(formContato["fonte"]))
    if formContato["fonte"] == 'on':
        formContato["fonte"] = True
    else:
        formContato["fonte"] = False
    print(formContato)
    print(type(formContato["nome"]))
    print(type(formContato["fonte"]))
    return redirect('/')


#execução
if __name__ == "__main__":
    app.run(debug=True)

    """ formCirc_tipo = {"RLs": request.form["RLs"],
                         "RLp": request.form["RLp"],
                         "RCs": request.form["RCs"],
                         "RCp": request.form["RCp"],
                         "RLCs": request.form["RLCs"],
                         "RLCp": request.form["RLCp"]
                         }
    print(formCirc_tipo)
    print(type(formCirc_tipo["RLp"]))
    for i in formCirc_tipo:
        if i == 'on':
            i = True
        else:
            i = False
    print(formCirc_tipo)
    print(type(formCirc_tipo["RLp"]))"""
