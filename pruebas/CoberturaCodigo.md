<div align="justify">

# ¿Qué es la cobertura de Código?

<div align="center">
  <img src="https://3.bp.blogspot.com/-RWJRuo_s4A4/W94W9MmFDmI/AAAAAAAABF8/JrNzkVSbARsbVXJ6GyX4V_MJXu91_7VngCLcBGAs/s1600/fowler.png" with="400px">
</div>

La cobertura de código es un parámetro con el que podrás saber qué parte de tu fuente se ha sometido a pruebas. Es muy útil para evaluar la calidad del conjunto de pruebas. Ahora, vamos a ver cómo dar los primeros pasos con tus proyectos.

## ¿Cómo se calcula la cobertura de código?

_Las herramientas de cobertura de código utilizarán uno o varios criterios para determinar cómo se ejecutó o no tu código durante la ejecución del conjunto de pruebas_. Estos son algunos de los parámetros que es habitual encontrar en los informes de cobertura:

- __Cobertura de funciones__: la cantidad de funciones definidas que se abarcan.
- __Cobertura de instrucciones__: cuántas instrucciones del programa se han ejecutado.
- __Cobertura de ramas__: cuántas ramas de las estructuras de control (instrucciones IF, por ejemplo) se han ejecutado.
- __Cobertura de condiciones__: en cuántas subexpresiones booleanas se ha comprobado el valor verdadero o falso.
- __Cobertura de líneas__: cuántas líneas de código fuente se han probado.

___Estas métricas suelen estar representadas por el número de elementos sometidos a prueba, los elementos que se encuentran en tu código y un porcentaje de cobertura (elementos probados/elementos encontrados)____.

_La métrica de la cantidad de líneas de código validadas exitosamente en el desarrollo de pruebas se convierte en un aspecto esencial para las empresas, debido a la necesidad de verificar que los productos que lanzan al mercado cumplan con cada uno de los estándares para una calidad significativa_.
___La efectividad, la seguridad y la confiabilidad son elementos que requieren revisión permanente__. Para ello existen las __pruebas automatizadas__. No obstante, se necesita a la vez controlar el desempeño de este elemento. Para esto se establece _la cobertura de código como elemento que asegura que todas las bases de código funcionan bajo tests automatizados_.

___La cobertura de código representa una garantía de que existe un nivel suficiente de pruebas automatizadas__. _La disminución de la tasa de cobertura de código supone la existencia de códigos añadidos al software sin revisión. Ello implica una ausencia de monitoreo total y, en consecuencia, incertidumbre sobre la calidad de la escritura general del programa. Cabe resaltar que en este escenario la probabilidad de fallos y errores crece_.

## Beneficios de la cobertura de código

___La cobertura de código representa una garantía del mantenimiento de la base de código___. Ello quiere decir que existe un seguro sobre la aplicación de pruebas automatizadas a las nuevas funciones. ___De esta manera, la calidad del programa base se mantiene___.
___Por otro lado, la cobertura de código ofrece la posibilidad de detectar algún código defectuoso, inactivo y/o no utilizado__. _Como consecuencia, puede darse un mejoramiento en la escritura general del software_. ___Paralelamente, la calidad del producto se asegura___.
_Teniendo en cuenta esto, un informe de cobertura puede considerarse un criterio para permitir o no desplegar un producto, estableciendo un nivel mínimo de desempeño de prueba para el lanzamiento del programa. Por último, como resultado del control de errores y de la calidad del producto, las empresas pueden conseguir mayor satisfacción de sus clientes. Del mismo modo, pueden aumentar la productividad y el lanzamiento de sus aplicaciones_.

__La cobertura de código ofrece la posibilidad de determinar qué partes del código fuente funcionan bajo pruebas automatizadas__. _Sin embargo, esta herramienta no asegura la eficacia de la revisión automatizada_. Por ello, es recomendable acompañar la cobertura de código con otros mecanismos de comprobación de eficiencia de pruebas.
<div align="center">
  <img src="https://www.parasoft.com/wp-content/uploads/2020/12/Fig-1-Code-Coverage-Metrics-and-Trends-1024x608.png.webp" with="400px">
</div>

## Consejos para tus primeros pasos

### Elige la herramienta adecuada para tu proyecto

Puede que encuentres varias opciones para crear informes de cobertura en función de los lenguajes que utilices. Estas son algunas herramientas populares:

- __Java__: Atlassian Clover, Cobertura, JaCoCo.
- __JavaScript__: istanbul
- __PHP__: PHPUnit
- __Python__: Coverage.py
- __Ruby__: SimpleCov

### ¿Qué porcentaje de cobertura es el que debes buscar?

En la cobertura de código no hay soluciones milagrosas. Además, incluso con un alto porcentaje de cobertura, podrías seguir teniendo problemas si no se prueban partes críticas de la aplicación o si las pruebas existentes no son lo suficientemente robustas como para detectar correctamente los fallos de antemano. Dicho esto, generalmente se acepta que la cobertura del 80 % es el objetivo que se debe perseguir. Tratar de alcanzar una cobertura mayor puede resultar costoso y no siempre genera unas ventajas que justifiquen el esfuerzo.

Cuando ejecutes por primera vez la herramienta de cobertura, puedes observar un porcentaje bastante bajo de cobertura. Si acabas de empezar con las pruebas, es algo normal y no deberías sentirte presionado por conseguir una cobertura del 80 % enseguida. Si te precipitas, podrías empujar al equipo a crear pruebas centradas en las líneas del código, en lugar de atender a los requisitos empresariales de la aplicación.

_Por ejemplo, en el caso anterior alcanzamos una cobertura del 100 % probando si 100 y 34 eran múltiplos de 10. Pero ¿y si la función se llamase con una letra en lugar de con un número? ¿Obtendríamos un resultado verdadero/falso? ¿O sería una excepción? Es importante que des tiempo al equipo para pensar en pruebas desde la perspectiva del usuario y no solo fijándose en las líneas de código. La cobertura de código no te dirá si te faltan cosas en la fuente_.

### Comienza centrándote en las pruebas unitarias
Las pruebas unitarias comprueban que los métodos individuales de las clases y los componentes utilizados por la aplicación funcionan. Por lo general, son baratas de implementar y rápidas de ejecutar, y dan una garantía general de que la base de la plataforma es sólida. Una forma sencilla de aumentar rápidamente la cobertura de código es añadir pruebas unitarias que, por definición, deberían ayudarte a garantizar que el conjunto de pruebas llega a todas las líneas de código.

### Utiliza informes de cobertura para detectar fallos críticos en las pruebas
Enseguida tendrás tantas pruebas en el código que será imposible saber qué parte de la aplicación se comprueba durante la ejecución del conjunto de pruebas. Cuando haya compilaciones defectuosas sabrás que se ha roto algo, pero te será difícil saber qué componentes han superado las pruebas.

Precisamente en este punto es donde los informes de cobertura pueden proporcionar orientación práctica para el equipo. La mayoría de las herramientas permiten examinar los informes de cobertura para ver los elementos que no cubren las pruebas y luego utilizarlos para identificar partes críticas de la aplicación que todavía estén por probar.

SimpleCov para Ruby puede mostrar qué métodos no han sido probados
### Cuando lo tengas todo listo, integra la cobertura de código en tu flujo de integración continua
Cuando establezcas un flujo de trabajo de integración continua (CI), puede que empieces a recibir fallos de las pruebas si no alcanzas un porcentaje suficientemente alto de cobertura. Por supuesto, como se ha dicho ya, no sería razonable establecer un umbral demasiado alto y es probable que una cobertura del __90 %__ ocasione muchos fallos en la compilación. __Si tu objetivo es una cobertura del 80 %, podrías establecer un umbral de fallo del 70 % como red de seguridad para tu cultura de CI__.

Como tantas veces, procura no enviar el mensaje equivocado, ya que presionar al equipo para que alcance una buena cobertura podría llevar a malas prácticas de pruebas.

### Una buena cobertura no equivale a buenas pruebas

Para conformar una buena cultura de pruebas, tu equipo debe saber cómo debería comportarse la aplicación cuando se usa correctamente, pero también cuando alguien intenta forzarla. Las herramientas de cobertura de código ayudan a saber dónde mirar, pero no indican si tus pruebas son lo suficientemente robustas ante comportamientos inesperados.

```python
python3 -m pip install coverage
```

__Salida de la ejecución__:

```code
Installing collected packages: coverage
Successfully installed coverage-7.2.7
WARNING: You are using pip version 20.3.3; however, version 23.1.2 is available.
You should consider upgrading via the '/usr/local/opt/python@3.9/bin/python3.9 -m pip install --upgrade pip' command.
````

__Verificamos la versión__

```python
coverage --version
Coverage.py, version 7.2.7 with C extension
Full documentation is at https://coverage.readthedocs.io/en/7.2.7
```

```python
python3 -m coverage --version
Coverage.py, version 7.2.7 with C extension
Full documentation is at https://coverage.readthedocs.io/en/7.2.7
```

# Referencias
- [Atlassian](https://www.atlassian.com/es/continuous-delivery/software-testing/code-coverage).

- [Coverage](https://coverage.readthedocs.io/en/7.2.7/install.html).


</div>