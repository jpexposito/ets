<div align="justify">

# Elaboración de Diagramas de casos de Uso

## Lenguaje de Modelado Unificado (UML)

<div align="center">
  <img src="https://folderit.net/wp-content/uploads/2014/06/uml-logo.jpg"  />
</div>

El diagrama de casos de uso es uno de los diagramas incluidos en UML 2.5, estando este clasificado dentro del grupo de diagramas de comportamiento. Es, con total seguridad, el diagrama más conocido y es utilizado para representar los actores externos que interactúan con el sistema de información y a través de que funcionalidades (casos de uso o requisitos funcionales) se relacionan. Dicho de otra manera, muestra de manera visual las distintas funciones que puede realizar un usuario (más bien un tipo de usuario) de un Sistema de Información.

En este documento se incluye información sobre como construir este diagrama.

Lo primero es saber cual es su finalidad. El diagrama de casos de uso, dependiendo de la profundidad que le demos, puede ser utilizado para muchos fines, entre ellos podemos encontrar los siguientes:
- Representar los requisitos funcionales.
- Representar los actores que se comunican con el sistema. Normalmente los actores del sistema son los usuarios y otros sistemas externos que se relacionan con el sistema. En el caso de los usuarios hay que entender el actor como un “perfil”, pudiendo existir varios usuarios que actúan como el mismo actor.
- Representar las relaciones entre requisitos funcionales y actores.
- Guiar el desarrollo del sistema. Crear un punto de partida sobre el que empezar a desarrollar el sistema.
- Comunicarse de forma precisa entre cliente y desarrollador. - Simplifica la forma en que todos los participes del desarrollo, incluyendo el cliente, perciben como el sistema funcionará y ofrecerá una visión general común del mismo.

# Elementos de un diagrama de casos de uso
Un diagrama de casos de uso está compuesto, principalmente, de 3 elementos: Actores, Casos de uso y Relaciones.

## Actores
Como ya hemos comentado en la presentación, un actor es algo o alguien externo al sistema que interactúa de forma directa con el sistema. Cuando decimos que interactúa nos referimos a que aporta información, recibe información, inicia una acción…

Se representan con una imagen de un “muñeco de palo” con el nombre del actor debajo.

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_562f5341.gif"  />
</div>


__Existen dos tipos de actores__: _Los usuarios y los sistemas_.

No hay que entender los usuarios como personas singulares, sino como “perfiles o roles” que identifican a un tipo de usuario, pero no al usuario en sí. Por ejemplo, en una aplicación de gestión de nóminas, un actor de este tipo podría ser “gestor de nóminas” que se encarga de emitir y firmar nóminas. Este rol podría ser tomado, por ejemplo, por cualquier individuo del personal de recursos humanos y, además, por el jefe de la empresa. Es un ejemplo muy sencillo, pero como puedes ver, un actor no representa a una única persona o a un único usuario.

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_m3b8a833e-300x113.gif"  />
</div>
Por otro lado, los actores pueden ser otros sistemas que también interactúan con nuestro propio sistema. Un ejemplo podría ser, en nuestra aplicación de nóminas, un sistema que almacene las nóminas firmadas a modo de archivo. En este caso cuando se firma la nómina se recibe la misma por el sistema de archivo, por tanto el caso de uso se relaciona con el actor.


En ocasiones este tipo de actores no se representa con un “hombre de palo” porque puede dar la sensación de que es un usuario y queda poco intuitivo.

## Casos de uso
Un caso de uso se utiliza para representar una de las funcionalidades que realiza el sistema. Es una secuencia de acciones que hace el sistema y que producen un resultado que puede percibir un usuario.

Formalmente hablando, un caso de uso es una clasificación de comportamiento que especifica una unidad de funcionalidad completa y que está realizada por uno o más sujetos que se relacionan con el caso de uso colaborando para ello con uno o más actores y que produce un resultado que tiene alguna utilidad para cualquier de esos actores.

__Se representan con una elipse que incluye en su interior el nombre del caso de uso__.

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_717db682.gif"  />
</div>

__Existen muchos ejemplos de casos de uso__. Algunos podrían ser: _Crear pedido, Listar productos, Enviar correo_. __Cualquier acción que realice la aplicación__.

Las especificaciones anteriores a UML 2.5 requerian que un caso de uso sea invocado por un actor. En UML 2.5 esto se eliminó, lo que significa que podría haber algunas situaciones en las que la funcionalidad del sistema la inicie el propio sistema y, al mismo tiempo, brinde resultados útiles a un actor. Por ejemplo, el sistema podría notificar a un cliente que se envió la orden, programar la limpieza y el archivo de la información del usuario, solicitar información de otro sistema, etc.

## Relaciones

Las relaciones conectan los casos de uso con los actores o los casos de uso entre sí.

Cuando conectan un actor con un caso de uso representa que ese actor interactúa de alguna manera con ese caso de uso y se representa con una linea continua con la identificación __<<communicates>>__.


<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_6cb331c2-300x76.gif"  />
</div>

Cuando conectan casos de uso entre sí se pueden diferenciar dos tipos de relaciones: __<<include>>__ y __<<extends>>__. En español a veces se usa la nomenclatura __<<usa>>__ y __<<extiende>>__:

- __<<include>>__: _Se utiliza para representar que un caso de uso utiliza siempre a otro caso de uso_. Es decir, _un caso de uso se ejecutará obligatoriamente_ (lo incluye, lo usa). Se representa con una flecha discontinua que va desde el caso de uso de origen al caso de uso que se incluye.

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_m63c2a68e-300x60.gif"  />
</div>

_Un uso típico de este tipo de relaciones se produce cuando dos casos de uso comparten una funcionalidad. Esa funcionalidad es extraida de los dos y se crea un caso de uso nuevo que se relaciona con los anteriores con un include_.

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_65fe3e93-300x91.gif"  />
</div>

_En este ejemplo, los casos de uso emitir factura y enviar producto ejecutarán ambos el caso de uso autenticación_.

- __<\<extend\>>__: _Este tipo de relaciones se utilizan cuando un caso de uso tiene un comportamiento opcional, reflejado en otro caso de uso_. Es decir, __un caso de uso puede ejecutar, normalmente dependiendo de alguna condición o flujo del programa__, otro caso de uso. Se representa con una flecha discontinua que va desde el caso de uso opcional al original.

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_80df9c8-300x59.gif"  />
</div>

Un ejemplo de esta relación podría ser la siguiente:

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_m64db9122-300x88.gif"  />
</div>

_En este supuesto el caso de uso Hacer pedido puede dar lugar (o no) a otros dos casos de uso: Enviar notificación SMS y Enviar notificación email. Se supone que, cuando un usuario hace un pedido, el sistema le permite elegir si quiere que se envíe una notificación de ese pedido por SMS o por email_.

Existe,además, otra __relación__ denominada __generalización__ que consiste en hacer que __un elemento herede el comportamiento de otro__. Aunque se puede utilizar entre casos de uso, es más común utilizarlo entre actores, haciendo que uno de los actores tenga acceso a las funcionalidades de otro. Se representa con una flecha con la punta hueca que va desde el elemento que hereda al elemento heredado:

<div align="center">
  <img src="https://diagramasuml.com/wp-content/uploads/2018/08/Diagrama-de-casos-de-uso_html_585ec97c.gif"  />
</div>

Si estás interesado, puedes seguir nuestra guía para identificar actores y casos de uso.

## Descripción de requisitos funcionales y no funcionales

Es común en este tipo de diagramas describir cada caso de uso junto con la secuencia de pasos necesaria para completarlo y las posibles excepciones hasta definir todas las situaciones posibles. Esta descripción servirá de guía para el desarrollo, la profundidad de las situaciones que se traten dependerá de cada fase del proyecto o de cada situación en particular.

Existen dos tipos de requisitos:

- Requisitos funcionales
- Requisitos no funcionales

Los requisitos suelen ser plasmados junto a la [siguiente información](../ESTRUCTURACION-ESPECIFICACION-CASO-USO.md).

## Cómo dibujar un diagrama de casos de uso

A la hora de dibujar un diagrama de casos de uso te recomendamos que compruebes que has realizado previamente todos estas tareas, respondiendo a las preguntas que te escribimos a continuación:

- Recopilar fuentes de información: ¿cómo se supone que debo saber eso?
- Identificar actores potenciales: ¿qué usuarios utilizan los bienes y servicios del sistema empresarial?. Para más información te recomiendo la guía para identificar actores y casos de uso.
- Identificar posibles casos de uso: ¿a qué bienes y servicios pueden recurrir los actores?
- Conectar los casos de uso: ¿quién puede hacer uso de los bienes y servicios del sistema empresarial?
- Describir actores: ¿a quién o qué representan los actores?
- Buscar más casos de uso: ¿Qué más debe hacer el sistema?
- Documentar casos de uso: ¿qué sucede exactamente en cada caso de uso?
- Relacionar modelos entre casos de uso empresarial: ¿qué actividades se realizan repetidamente?
- Verificar la vista, ¿todo es correcto?

Los pasos se han escrito en este orden a propósito, ya que es la forma lógica de seguirlos. Sin embargo, este orden no es obligatorio, ya que en la práctica, los pasos individuales a menudo se superponen unos con otros.

Para poder seguir los pasos de una forma óptima, es importante comprender el negocio/sistema para conseguir seguir cada paso individual. En algunos casos tambien es necesario consultar a los expertos o consultores del negocio. No tiene sentido aferrarse a la visión personal del analista, si este no tiene mucho conocimiento del área de negocio de la aplicación.




</div>