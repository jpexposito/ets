<div align="justify">

# ¿Qué es Entorno de desarrollo?

Generalmente, cuando comenzamos a desarrollar, nos nombran el concepto de entorno de
desarrollo integrado (ide):
__Es un sistema de software para el diseño de aplicaciones que combina herramientas del
desarrollador comunes en una sola interfaz gráfica de usuario (GUI), que reúne
diferentes características.__
Fuente: Redhat

_Sin embargo, un entorno de desarrollo es mucho más que eso. Lo podemos definir como:
El conjunto de herramientas e instalaciones que los programadores necesitamos durante
el desarrollo y diseño de software._

A la hora de seleccionar nuestro entorno de desarrollo debemos tener en cuenta varios
factores, o necesidades para lograr nuestros objetivos. Estos podemos resumirlos en:
- Lenguaje de desarrollo.
- Frontend/Backend/Fullstack.
- Integración con otros sistemas (BBDD/API ́s, etc)
- Otros.

Actualmente hacemos referencia a un entorno de desarrollo al proceso integral de
gestión del desarrollo de software, desde su diseño, hasta su puesta en explotación,
pasando por diferentes fases.

De un modo más coloquial, lo definimos como nuestro espacio de trabajo en el que los cambios
se implementan en diferentes entornos hasta que se ponen en marcha en la versión real.

## Objetivo Principal

En el momento de desarrollo, se prima:
- El control de versiones.
- La realización de pruebas.
- La documentación del proyecto.
- ...

Con este tipo de metodología permitiremos que el desarrollo de software se realice de forma
más ágil, acortando los tiempos, y mejorando el producto final.

## Fases o Etapas

En el desarrollo de software existen diferentes etapas o fases por las que pasan nuestros
desarrollos. Estas fases/etapas o más comúnmente conocido como entornos se ejecutan desde
el inicio del proyecto, primeras etapas de desarrollo, hasta la fase final y posteriormente el
mantenimiento del mismo. Estos entornos son:

## Entorno de desarrollo

El entorno de desarrollo propiamente dicho se refiere a la creación del software. Este entorno
puede ser manejado a nivel local en el ordenador del programador o en un servidor local.

En este momento el trabajo se centra en la codificación, la realización de pruebas
iniciales y la ejecución correcta del código.

### Entorno de Integración

El entorno de integración facilita la unión de los diferentes desarrollos y permite comprobar que
los diferentes trabajos no interfieren entre sí. Se hace uso del control de versiones y
herramientas como git.

### Entorno de pruebas o testing

Haremos uso generalmente de la nube, y de herramientas alojadas en ésta. En un futuro no
muy lejano espero realizar un post sobre ello, con un ejemplo real. Permite a los miembros del
equipo y clientes interactuar con el software para realizar tests de funcionalidades del sistema.
Además, un uso común es el lanzamiento de pruebas automatizadas para verificar el correcto
funcionamiento de la rama principal, así como de pruebas de carga, estrés, etc.

### Entorno de pre-producción

__Pre-Producción o Staging__, permite trabajar en un entorno con una configuración exactamente
igual a la que existe en el entorno de producción. La finalidad de usar este tipo de servidor
es simular el entorno de producción para validar su usabilidad en un entorno real.


### Entorno de producción

Entorno donde finalmente se ejecuta el software, el cual es utilizado por el usuario. Este
servidor, a diferencia del servidor de pre-producción, debería tener una mayor infraestructura
y mayor capacidad de manejo de tráfico.
Para finalizar hemos de recordar que:
Elegir un entorno de desarrollo adecuado puede suponer un gran cambio en la
productividad de los desarrolladores de la empresa y en la ejecución ágil de los
proyectos.
Es por ello que se deben tener en cuenta todos los requerimientos necesarios y que los
desarrolladores consideran imprescindibles para su trabajo, con el fin de satisfacerlos y
utilizar la herramienta adecuada para el equipo.

</div>