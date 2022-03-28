from flask import Flask,flash,render_template,redirect ,url_for, request
from config import config
from datetime import datetime
from flask_mysqldb import MySQL




app =Flask(__name__)

app.secret_key = 'clave_secreta'


conexion = MySQL(app)

# Context processors

@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
    }


@app.route('/')
@app.route('/clientes')
def index():
    
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT * FROM cliente ORDER BY id DESC")
        clientes = cursor.fetchall()
        cursor.close()

        return render_template('index.html', clientes=clientes)
    

# Ruta para el formulario de ingresos de clientes
@app.route('/registrar-clientes', methods= ['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # conseguimos los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo =request.form['correo']
        edad = request.form['edad']
        direccion = request.form['direccion']
        comida = request.form['comida']
        observacion = request.form['observacion']

        
        cursor = conexion.connection.cursor()
        cursor.execute("INSERT INTO cliente VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s)", (nombre, apellido, telefono, correo, edad, direccion, comida, observacion)) 
        cursor.connection.commit()
        flash('el cliente se a agregado correctamente')

        return redirect(url_for('index'))

    return render_template('formulario.html')    

@app.route('/borrar/<cliente_id>')
def borrar_cliente(cliente_id):
    cursor=conexion.connection.cursor()
    cursor.execute(f"DELETE FROM cliente WHERE id = {cliente_id}")
    conexion.connection.commit()

    flash('el cliente ha sido eliminado')
    return redirect(url_for('index'))

@app.route('/editar/<cliente_id>', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    if request.method == 'POST':
        # conseguimos los datos para editarlos del formulario
        nombre      = request.form['nombre']
        apellido    = request.form['apellido']
        telefono    = request.form['telefono']
        correo      =request.form['correo']
        edad        = request.form['edad']
        direccion   = request.form['direccion']
        comida      = request.form['comida']
        observacion = request.form['observacion']

        cursor = conexion.connection.cursor()
        cursor.execute("""
            UPDATE cliente
            SET nombre      = %s,
                apellido    = %s,
                telefono    = %s,
                correo      = %s,
                edad        = %s,
                direccion   = %s,
                comida      = %s,
                observacion = %s
            WHERE id        = %s
        """, (nombre, apellido, telefono, correo, edad, direccion, comida, observacion, cliente_id)) 
        cursor.connection.commit()
        
        flash('El cliente ha sido editado correctamente')
        
        return redirect(url_for('index'))

    cursor = conexion.connection.cursor()
    cursor.execute("SELECT * FROM cliente WHERE id = %s", (cliente_id))
    cliente = cursor.fetchall()
    cursor.close()

    return render_template('formulario.html', cliente=cliente[0])


@app.route('/vista/<cliente_id>')
def vista(cliente_id):
    cursor = conexion.connection.cursor()
    cursor.execute(f"SELECT * FROM cliente WHERE id = {cliente_id}")
    cliente = cursor.fetchall()
    cursor.close()

    return render_template('vista.html', cliente=cliente[0])

 

def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe...</h1>", 404



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()