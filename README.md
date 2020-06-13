# Sistema de Transparencia Presupuestal
### Universidad Nacional Autónoma de México
### Facultad de Ingeniería
### Criptografía. Grupo: 2
### Integrantes:
#### Aguilar Luna Gabriel Daniel
#### Chavira Tapia Andrés Uriel
#### Jiménez Juárez Jesús
#### Joya Venegas Jehosua Alan
#### Ramírez Villa Brandon Alberto

Basada en la implementación [provista por IBM](https://github.com/satwikkansal/python_blockchain_app/tree/ibm_blockchain_post).

## Instrucciones de ejecución

Clonar el proyecto,

```sh
$ git clone https://github.com/Jehosua97/Cripto.git
```

Luego de colocarse en la direccion donde se descargo el reposirtorio instalar las dependencias,

```sh
$ cd Cripto
$ pip install -r requirements.txt
```

Para iniciar un blockchain node server,

```sh
# Para ejecutar desde Linux:
$ export FLASK_APP=node_server.py
$ flask run --port 8000
# Para ejecutar desde Windows:
> set FLASK_APP=node_server.py
> flask run --port 8000
```

Ejecutar la aplicación en una terminal diferente,

```sh
$ python run_app.py
```

Listo. Para operar la aplicación entre en el enlace: [http://localhost:5000](http://localhost:5000).

## Ejemplos

1. Pantalla principal

![image.png](https://github.com/Jehosua97/Cripto/blob/master/screenshots/Screen1.png)

2. Transacción

![image.png](https://github.com/Jehosua97/Cripto/blob/master/screenshots/transaccion.png)

3. Selección de entidad a verificar

![image.png](https://github.com/Jehosua97/Cripto/blob/master/screenshots/selectVerify.png)

4. Verificación

![image.png](https://github.com/Jehosua97/Cripto/blob/master/screenshots/verification.png)

## Conectar diferentes dispositivos

Es posible crear Publicaciones desde otros  dispositivos conectados en la misma red LAN, es necesario conocer la ip del dispositivo que actua como servidor. Para conocer la dirección ip del dispositivo en el que se  esta ejecutando la aplicacion. Se puede hacer de las siguientes maneras:

```sh
# Desde Linux
$ ifconfig
# Desde Windows
> ipconfig
```

Finalmente desde el navegador del otro dispositivo se ingresa al puerto 5000 de dicha ip (se muestra un ejemplo desde un dispositivo movil)

![image.png](https://github.com/Jehosua97/Cripto/blob/master/screenshots/movil.jpeg)

Estos dispositivos solo pueden hacer Publicaciones y Sincronizar su información con la cadena, sin embargo no pueden ni Verificar ni solicitar Minar, esto solo es posible desde el equipo que ejecuta la aplicación.