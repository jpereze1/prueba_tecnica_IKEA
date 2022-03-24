from flask import Flask, render_template,redirect ,url_for
from datetime import datetime
from flask_mysqldb import MySQL

app =Flask(__name__)

# Conexion con la base de datos


# Context processors

@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }

@app.route('/')
def index():
    return render_template('index.html',
                            dato1 = "Valor1",
                            dato2 = "valor2",
                            lista1 = ["uno", "dos", "tres"] 
                            )

@app.route('/form')
@app.route('/form/<redireccion>')
def formulario(redireccion = None):
    if redireccion is not None:
        return redirect(url_for('index'))
    return render_template('formulario.html')
    

if __name__ == '__main__':
    app.run(debug=True)