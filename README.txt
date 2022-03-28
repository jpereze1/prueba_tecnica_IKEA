Entregable.
	
	* Resumen de la app: esta app esta configurada para ingresar clientes con sus datos requeridos.
	  los guarda en la base de datos, puedes ver una lista  con sus respuestas en JSON de todos los datos de los clientes.
	  puedes Crear, Leer, Actualizar, Eliminar.

	* Librerias utilizadas en esta app son:
		flask de Flask: esta sirve para crear la pagina con el framework Flask.
			flash: hutilizada para crear los mensajes de informacion al hacer CRUD con la base de datos.
			render_templade: se utiliza para enlazar las plantillas con la app y crear plantillas mas comodamente.
			redirect: esta libreria se utiliza para redirigir las paginas.
			url_for: tambien utilizada para definir una redirecion de una pagina.
			request: se utiliza para hacer las peticiones con los methods=['GET', 'POST']
			datatime: se utiliza para hacer un contex_procesor y poder mostrar la hora y fecha en tiempo real.
			config: cree este para importar los datos de la base de datos y la configuracion del servidor flask.
			flas_mysql: se tulizo para hacer las conecciones con la base de datos. 
	
	* Pasos para montar la APP en un entorno: el archivo principal donde se encuentra el APP se llama main.py al posicionarce en la carpeta contenedora podemos llamarla y ensender el servido con el comando python main.py.
		importando el archivo config.py donde tenemos la configuracion del servidor flask y la coneccion a la base de datos.
		la carpeta static contiene todos el estilo de la pagina con el archivo styles.css
		todas las templades estan en una carpeta llamada tempades ubicada en la carpeta de la APP  
	
	*URL de accion
		Leer = GET 		url: /clientes and /vista/<cliente_id>    def index(): render_templade('index.html')
		Crear = POST 	url: /registrar-clientes			def formulario(): si el cliente ya esta creado se hace un redirecr(url_for('index')) y si no es ta creado se crea el usuario y se dirije a la template ('formulario.html)
		Actualizar = POST url: /editar/<cliente_id>			def editar_cliente(cliente_id) con el dato cliente_id se selecciona un cliente de la base de datos para actualizarlo y es que ya existe te envia a crearlo 
		Eliminar = DELETE url: /borrar/<cliente_id> 			def borrar_cliente(cliente_id) con el dato cliente_id para identificar cual registro se borrara luego de hacer el proceso en la base de datos manda un mensaje que el cliente a sido eliminado y te redirije a index con redirect(url_for)

	las url estan todas con sus funciones y con un retur de render_templade par acargar las vistas de los datos
	todas las funciones toman los datos de la base de datos de los clientes y las proporcionan por las vistas creadas con flask
