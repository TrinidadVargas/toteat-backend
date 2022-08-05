# Toteat - Desafío Técnico 
## By Trinidad Vargas

Aplicación web en producción: https://toteat-front-lczyyc6jm-trinidadvargas.vercel.app/

Backend: https://github.com/TrinidadVargas/toteat-backend

Frontend: https://github.com/TrinidadVargas/toteat-front

### Problema a resolver

- En base al contexto provisto, propongo desarrollar una aplicación para generar información para facilitar la toma de decisiones para gestión del negocio.
- Métricas propuestas: total de ventas por mes y día de la semana. El backend genera datos filtrados por mesero, cajero, zona de la mesa y horario, pero en esta etapa no se visualizan los filtros.

### Resolución del problema y Diseño técnico

#### Análisis de datas
Primero se analizó los datos entregados por Toteat para elegir las métricas que generan información útil. Estas son los totales de venta por día, mes, día de la semana y con distintos filtros como se mencionó. Y las métricas de venta de los productos que se dejó para una segunda etapa.

#### Backend
- Se usó un templete de Flask hecho por Microsoft que viene con un setup simple para una Api y con las configuraciones para testing y deploy en distintas plataformas.
- Para la capa de datos se decidió utilizar el json provisto (se validó con los entrevistadores), ya que la aplicación propuesta se requiere acceso de solo lectura y leer los datos directamente desde el file system es una solución simple y temporal que permitirá entender mejor el negocio, para luego buscar una alternativa más adecuada.  Las alternativas son usar una base de datos no-sql que mantiene la estructura, pero no trae mayores beneficios o usar una base de datos SQL que requiere normalizar los datos y cambiar la estructura.
- Se creó el endpoint ```estadísticas``` en la ruta ```routes``` y las funciones que permiten analizar los datos en ```use_cases```.
- Se crearon test de las funciones de análisis de datos
- Se hizo deploy de la aplicación en Heroku. 


#### Frontend
- Para el frontend se usó NextJs, un framework sobre NodeJs y React que incluye configuraciones simples y permite deployar en menos de 1 minuto en Vercel.
- Se crearon los requests de los datos con Axios.
- En ```routes``` se encuentra la vista principal de las estadísticas, donde se pueden elegir que se muestren los datos por día, mes o día de la semana.
- En ```components/Chart.js``` se creó el componente que entrega el gráfico de barras y recibe los datos procesados por las funciones definidas en ```utils/charts``` ya que el paquete ChartJs requiere los datos en una estructura definida.
- Se deployó la aplicación en Vercel.
- Algunos paquetes usados son Axios para los requests, ChartJs para los gráficos y Mantine para el estilo.

### Mejoras a futuro
Las principales mejoras que haría a futuro (sin limite de tiempo) son:
- Generar gráficos con los datos ya obtenidos filtrados por mesero, cajero, zona del restorán y horario.
- Generar los datos en el backend y la visualización en el frontend de las estadísticas de ventas de los diferentes productos.
- Generar tests para los endpoints de la Api en el backend.
- Definir una base de datos para poder agregar datos de nuevas ventas. Ya sea por un post de una venta o a través de un archivo.
- Mejorar el estilo de las vistas. Usar los componentes de Mantine para agregar layout y ajustar el parte de los gráficos.

**Nota:** la opción gratis de Heroku baja los servidores que no se están usando, por lo que el primer request al backend puede fallar y no se verán las estadísticas. Recargar la página si esto sucede.

## Para el desarrollador

* This sample contains the completed program from the tutorial, make sure to visit the link: [Using Flask in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask). Intermediate steps are not included.

* It also contains the *Dockerfile* and *uwsgi.ini* files necessary to build a container with a production server. The resulting image works both locally and when deployed to Azure App Service. See [Deploy Python using Docker containers](https://code.visualstudio.com/docs/python/tutorial-deploy-containers).

* To run the app locally:
  1. Run the command `cd hello_app`, to change into the folder that contains the Flask app.
  1. Run the command `set FLASK_APP=webapp` (Windows cmd) or `FLASK_APP=webapp` (macOS/Linux) to point to the app module.
  1. Start the Flask server with `flask run`. Or to run in debug mode ```FLASK_APP=webapp FLASK_DEBUG=1 flask run```

<!-- #### The startup.py file

In the root folder, the `startup.py` file is specifically for deploying to Azure App Service on Linux without using a containerized version of the app (that is, deploying the code directly, not as a container).

Because the app code is in its own *module* in the `hello_app` folder (which has an `__init__.py`), trying to start the Gunicorn server within App Service on Linux produces an "Attempted relative import in non-package" error.

The `startup.py` file, therefore, is a shim to import the app object from the `hello_app` module, which then allows you to use startup:app in the Gunicorn command line (see `startup.txt`). -->

<!-- pip3 install -r requirements.txt  
FLASK_APP=webapp flask run   
pytest 
git push -u origin master
source .env/bin/activate    
-->