# Trabajo diario a través de git

<div align="justify">

<div align="center">
  <img src="https://git-scm.com/images/logo@2x.png" >
</div>


Crear un repositorio en vuestro GitHub llamado **my-proyecto-millonario**.

Clonar vuestro repositorio en local.

~~~
git clone git@github.com:alumno-XXX/my-proyecto-millonario.git
~~~

## README

Crear (si no lo habéis creado ya) en vuestro repositorio local
un documento **README.md**.

> Notas: en este documento tendreís que ir poniendo los **comandos**
> que habéis tenido que utilizar durante todos los ejercicios
> y las **explicaciones y capturas de pantalla** que consideréis **necesarias**.

~~~
touch README.md
~~~

## Commit inicial

Añadir al README.md los comandos utilizados hasta ahora
y hacer un commit inicial con el mensaje **commit inicial**.

~~~
git add .
git commit -m "commit inicial"
~~~

## Push inicial

Subir los cambios al repositorio remoto.

~~~
git push origin master
~~~

> Pregunta: ¿Si has clonado el repositorio, que parte del comando anterior podemos omitir? Justifica tu respuesta en el fichero **README.md**.

## Ignorar archivos

Crear en el repositorio local un fichero llamado **privado.txt**.

~~~
touch privado.txt
~~~

Crear en el repositorio local una carpeta llamada **privada**.

~~~
mkdir privada
~~~

Realizar los cambios oportunos para que tanto el archivo como
la carpeta sean ignorados por git.

~~~
echo "privado.txt" >> .gitignore
echo "/privada" >> .gitignore
git add .
git commit -m "añadido fichero .gitignore"
~~~

> Pregunta: ¿El fichero y el directorio privado podrían ser subidos al repositorio si se encuentran añadidos al fichero .gitignore? **[Si/No]**. Justifica tu respuesta en el fichero **README.md**.

## Añadir fichero 1.txt

1. Añadir fichero **1.txt** al repositorio local.

~~~
touch 1.txt
git add .
git commit -m "añadido 1.txt"
~~~

> Pregunta: Si has ejecutado las acciones **add** y **commit**, explica que realiza cada una sobre el/los ficheros. Justifica tu respuesta en el fichero **README.md**.

## Crear el tag v0.1

1. Crear un tag **v0.1**.

~~~
git tag v0.1
~~~

## Subir el tag v0.1

1. Subir los cambios al repositorio remoto.

~~~
git push --tag origin master
~~~

> Pregunta: *¿Qué es un tag sobre un repositorio git(en nuestro caso la plataforma Github)?.* Justifica tu respuesta en el fichero **README.md**.

## Crear una rama v0.2

1. Crear una rama **v0.2**.

~~~
git branch v0.2
~~~

1. Posiciona tu carpeta de trabajo en esta rama.

~~~
git checkout v0.2
~~~

## Añadir fichero 2.txt

1. Añadir un fichero **2.txt** en la rama **v0.2**.

~~~
touch 2.txt
git add .
git commit -m "añadido 2.txt"
~~~

> Pregunta: *¿Cuando estamos trabajando con ramas, cual es su fin y sentido en organizaciones pequeñas/medianas/grandes?* Justifica tu respuesta en el fichero **README.md**.

## Crear rama remota v0.2

1. Subir los cambios al repositorio remoto.

~~~
git push origin v0.2
~~~

## Merge directo

1. Posicionarse en la rama **master/main** según sea tu rama principal.

~~~
git checkout master
~~~

1. Hacer un merge de la rama **v0.2** en la rama **master/main**.

~~~
git merge v0.2 -m "merge v0.2 sin conflictos"
~~~

> Pregunta: *¿Se producirían conflictos trás realizar las acciones anteriores?* **[Si/No]** Justifica tu respuesta en el fichero **README.md**.

## Merge con conflicto

1. En la rama **maste/main** poner **Hola** en el fichero **1.txt** y hacer commit.

~~~
git checkout master
echo "Hola" >> 1.txt
git add .
git commit -m "hola en 1.txt"
~~~

1. Posicionarse en la rama **v0.2** y poner **Adios** en el fichero "1.txt" y hacer commit.

~~~
git checkout v0.2
echo "Adios" >> 1.txt
git add .
git commit -m "adios en 1.txt"
~~~

1. Posicionarse de nuevo en la rama **master/main** y hacer un merge con la rama **v0.2**

~~~
git checkout master
git merge v0.2
vim 1.txt
git add .
git commit -m "arreglado merge en 1.txt"
~~~

## Listado de ramas

1. Listar las ramas con merge y las ramas sin merge.

~~~
git branch --merged
git branch --no-merged
~~~

## Arreglar conflicto

1. Arreglar el conflicto anterior y hacer un commit.

~~~
vim 1.txt
git add .
git commit -m "arreglado merge en 1.txt"
~~~

## Borrar rama

1. Crear un tag **v0.2**

~~~
git tag v0.2
~~~

1. Borrar la rama **v0.2**

~~~
git branch -d v0.2
~~~

## Listado de cambios

1. Listar los distintos commits con sus ramas y sus tags.

~~~
git config --global alias.list 'log --oneline --decorate --graph --all'
git list
~~~
<!--
## Cuenta de GitHub

1. Poner una foto en vuestro perfil de GitHub.

## Uso social de GitHub

1. Preguntar los nombres de usuario de GitHub de tus compañeros de clase, búscalos, y sigueles.

1. Seguir los repositorios **my-proyecto-millonario** del resto de tus compañeros.

1. Añadir una estrella a los repositorios **my-proyecto-millonario** del resto de tus compañeros.

## Crear una tabla

1. Crear una tabla de este estilo en el fichero **README.md** con la información
de varios de tus compañeros de clase:

|        NOMBRE          |                     GITHUB                        |
|------------------------|---------------------------------------------------|
| Nombre del compañero 1 | [enlace a github 1](http://github.com/jpexposito) |
| Nombre del compañero 2 | [enlace a github 1](http://github.com/jpexposito) |
| Nombre del compañero 3 | [enlace a github 3](http://github.com/jpexposito) |

## Colaboradores

Poner a [jpexposito](http://github.com/jpexposito) como colaborador
del repositorio **my-proyecto-millonario**.

## Crear una organización

Crear una organización llamada **my-proyecto-millonario-tunombredeusuariodegithub**

## Crear equipos

Crear 2 equipos en la organización **my-proyecto-millonario-tunombredeusuariodegithub**,
uno llamado **analistas** con más permisos y otro **desarrolladores**.

1. Meter a [jpexposito](http://github.com/jpexposito) y a 2 de vuestros compañeros de clase en el equipo **analistas**.

1. Meter a [jpexposito](http://github.com/jpexposito) y a otros 2 de vuestros
compañeros de clase en el equipo **desarrolladores**.

## Crear un index.html

1. Crear un index.html que se pueda ver como página web en la organización.

## Crear Pull-requests

1. Hacer 2 forks de 2 repositorios **my-proyecto-millonario-tunombredeusuariodegithub.github.io**
de 2 organizaciones de las que no seais ni administradores ni desarrolladores.

1. Crearos una rama en cada fork.

1. En cada rama modificar el fichero **index.html** añadiendo vuestro nombre.

1. Con cada rama hacer un pull-request.

## Gestionar Pull-requests

1. Aceptar los pull-request que lleguen a los repositorios de tu organización.
-->
</div>