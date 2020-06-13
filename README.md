# Sistema de Transparencia Presupuestal
### Universidad Nacional Autónoma de México
### Facultad de Ingeniería
### Criptografía. Grupo: 2
### Integrantes:
Aguilar Luna Gabriel Daniel
Chavira Tapia Andrés Uriel
Jiménez Juárez Jesús
Joya Venegas Jehosua Alan
Ramírez Villa Brandon Alberto

Basada en la implementación [provista por IBM](https://github.com/satwikkansal/python_blockchain_app/tree/ibm_blockchain_post).

## Instrucciones

Clonar el proyecto,

```sh
$ git clone https://github.com/Jehosua97/Cripto.git
```

Luego de colocarse en la direccion donde se descargo el reposirtorio instalar las dependencias,

```sh
$ cd python_blockchain_app
$ pip install -r requirements.txt
```

Para iniciar un blockchain node server,

```sh
# Para ejecutar desde Windows: https://flask.palletsprojects.com/en/1.1.x/cli/#application-discovery
$ export FLASK_APP=node_server.py
$ flask run --port 8000
```

Ejecutar la aplicación en una terminal diferente,

```sh
$ python run_app.py
```

Listo. Para operar la aplicación entre en el enlace: [http://localhost:5000](http://localhost:5000).

##Ejemplos

1. Pantalla principal

![image.png](https://github.com/Jehosua97/Cripto/tree/master/screenshots/Screen1.png)

2. Transacción

![image.png](https://github.com/Jehosua97/Cripto/tree/master/screenshots/transaccion.png)

3. Selección de entidad a verificar

![image.png](https://github.com/Jehosua97/Cripto/tree/master/screenshots/selectVerify.png)

4. Verificación

![image.png](https://github.com/Jehosua97/Cripto/tree/master/screenshots/verification.png)
