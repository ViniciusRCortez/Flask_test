from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# paginas

@app.route('/')
def homepage():
    global aux
    aux = 0
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    global formCirc_tipo
    global formCirc_saida
    global formCirc_carga
    global aux
    '''
    :param aux: Variavel auxiliar para determinar em qual pagina estamos, seguindo o padrão
            aux = 0, para pagina inicial
            aux = 1, para a pagina onde pede o tipo de resposta
            aux = 2, para a pagina que pede sovre qual elemento é dada a resposta
    '''

    if aux == 0:
        if request.method == 'POST':
            try:
                RLs = request.form["RLs"]
            except:
                RLs = False
            else:
                RLs = True

            try:
                RLp = request.form["RLp"]
            except:
                RLp = False
            else:
                Rlp = True

            try:
                RCs = request.form["RCs"]
            except:
                RCs = False
            else:
                RCs = True

            try:
                RCp = request.form["RCp"]
            except:
                RCp = False
            else:
                RCp = True

            try:
                RLCs = request.form["RLCs"]
            except:
                RLCs = False
            else:
                RLCs = True

            try:
                RLCp = request.form["RLCp"]
            except:
                RLCp = False
            else:
                RLCp = True
        formCirc_tipo = {"RLs": RLs,
                         "RLp": RLp,
                         "RCs": RCs,
                         "RCp": RCp,
                         "RLCs": RLCs,
                         "RLCp": RLCp
                         }
        aux = 1
        return redirect('/V_ou_I')
    elif aux == 1:
        if request.method == 'POST':
            try:
                V = request.form["V"]
            except:
                V = False
            else:
                V = True

            try:
                I = request.form["I"]
            except:
                I = False
            else:
                I = True
        formCirc_saida = {'V': V, 'I': I}
        aux = 2
        return redirect('/L_ou_C')
    elif aux == 2:
        if request.method == 'POST':
            try:
                C = request.form["C"]
            except:
                C = False
            else:
                C = True

            try:
                L = request.form["L"]
            except:
                L = False
            else:
                L = True

            # execução
        formCirc_carga = {'C': C, 'L': L}
        print(formCirc_tipo)
        print(formCirc_saida)
        print(formCirc_carga)
        aux = 3
        return redirect('/')
    else:
        return redirect('/')


@app.route('/V_ou_I')
def next_V():
    return render_template('V_ou_I.html')


@app.route('/L_ou_C')
def next_C():
    return render_template('L_ou_C.html')


if __name__ == "__main__":
    app.run(debug=True)
