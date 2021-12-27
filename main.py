from flask import Flask, render_template, request, redirect
import Interface
Interface.teste()
app = Flask(__name__)

#paginas
@app.route('/')
def homepage():
    return render_template('index.html')

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
