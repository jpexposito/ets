# Testing en Python

Dentro de la ingeniería software y la programación en general, el testing es una de las partes más importantes que nos encontraremos en casi cualquier proyecto. De hecho es común dedicar más tiempo a probar que el código funciona correctamente que a escribirlo. A continuación veremos las formas más comunes de testear el código en Python, desde lo más básico a conceptos algo más avanzados.

## Tests Manuales y Tests Automatizados

Aunque sea la primera vez que leas acerca de testing en Python, estoy seguro de que ya has ejecutado tests sobre tu código sin darte cuenta. De acuerdo a su forma de ejecución, los podemos clasificar en:

- __Tests manuales__: Son tests ejecutados manualmente por una persona, probando diferentes combinaciones y viendo que el comportamiento del código es el esperado. Sin duda los has realizado alguna vez.
- __Tests automáticos__: Se trata de código que testea que otro código se comporta correctamente. La ejecución es automática, y permite ejecutar gran cantidad de verificaciones en muy poco tiempo. Es la forma más común, pero no siempre es posible automatizar todo.

Imaginemos que hemos escrito una función que calcula la media de los valores que se pasan en una lista como entrada.

```python
def calcula_media(*args):
    return(sum(*args)/len(*args))
```

A nadie se le ocurriría publicar nuestra función calcula_media sin haber hecho alguna verificación anteriormente. Podemos por ejemplo probar con los siguientes datos y ver si la función hace lo que se espera de ella. Al hacer esto ya estaríamos probando manualmente nuestro código.

```python
print(calcula_media([3, 7, 5]))
# 5.0

print(calcula_media([30, 0]))
# 15.0
```

Con bases de código pequeñas y donde sólo trabajemos nosotros, tal vez sea suficiente, pero a medida que el proyecto crece puede no ser suficiente. ¿Qué pasa si alguien modifica nuestra función y se olvida de testear que funciona correctamente? Nuestra función habría dejado de funcionar y nadie se habría enterado.

Es aquí donde los test automáticos nos pueden ayudar. Python nos ofrece herramientas que nos permiten escribir tests que son ejecutados automáticamente, y que si fallan darán un error, alertando al programador de que ha “roto” algo. Podemos hacer esto con assert, donde identificamos dos partes claramente:

Por un lado tenemos la llamada a la función que queremos testear, que devuelve un resultado.
Por otro lado tenemos el resultado esperado, que comparamos con el resultado devuelto por la función. Si no es igual, se lanza un error.

```python
assert(calcula_media([3, 7, 5]) == 5.0)
assert(calcula_media([30, 0]) == 15.0)
```

Nótese que los valores de 5 y 15 los hemos calculado manualmente, y corresponden con la media de 3,7,5 y 30,0 respectivamente. Si por cualquier motivo alguien rompe nuestra función calcula_media(), cuando los tests se ejecuten lanzaran una excepción.

```python
Traceback (most recent call last):
  File "ejemplo.py", line 7, in <module>
    assert((calcula_media([30, 0]) == 15.0))
AssertionError
```

En proyectos grandes, es común que antes de permitirnos hacer merge de nuestro código en master, se nos obligue a ejecutar un conjunto de tests automatizados. Si todos pasan, se asumirá que nuestro código funciona y que no hemos “roto” nada, por lo que tendremos el visto bueno.

Visto esto, tal vez pueda parecer que los test automatizados son lo mejor, sin embargo no siempre se pueden automatizar los tests. Si por ejemplo estamos trabajando con interfaces de usuario, es posible que no podamos automatizarlos, ya que se sigue necesitando a un humano que verifique los cambios visualmente.

## Tests Unitarios en Python con unittest

Aunque el uso de assert() puede ser suficiente para nuestros tests, a veces se nos queda corto y necesitamos librerías como unittest, que ofrecen alguna que otra funcionalidad que nos hará la vida más fácil. Veamos un ejemplo. Recordemos nuestra función calcula_media, que es la que queremos testear.

```python
# funciones.py
def calcula_media(*args):
    return(sum(*args)/len(*args))
```

Podemos usar unittest para crear varios tests que verifiquen que nuestra función funciona correctamente. Aunque la estructura de un conjunto de tests se puede complicar más, la estructura será siempre muy similar a la siguiente:

Creamos una clase __Test<NombreDeLoQueSePrueba>__ que hereda de __unittest.TestCase__.
Definimos varios tests como métodos de la clase, usando __test_<NombreDelTest>__ para nombrarlos.
En cada test ejecutamos las comprobaciones necesarias, usando assertEqual en vez de assert, pero su comportamiento es totalmente análogo.

```python
# tests.py
from funciones import calcula_media
import unittest

class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        resultado = calcula_media([10, 10, 10])
        self.assertEqual(resultado, 10)

    def test_2(self):
        resultado = calcula_media([5, 3, 4])
        self.assertEqual(resultado, 4)

if __name__ == '__main__':
    unittest.main()
```

Si ejecutamos el código anterior, obtendremos el siguiente resultado. Esta es una de las ventajas de unittest, ya que nos muestra información sobre los tests ejecutados, el tiempo que ha tardado y los resultados.

```python
Ran 2 tests in 0.006s

OK
```

Por otro lado, usando -v podemos obtener más información sobre cada test ejecutado con su resultado individualmente. Si tenemos gran cantidad de tests suele ser recomendable usarla, ya que será más fácil localizar los tests que han fallado.

```python
$ python -m unittest -v tests

test_1 (tests.TestCalculaMedia) ... ok
test_2 (tests.TestCalculaMedia) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```python

Por último, si tenemos varios ficheros de test, podemos usar discover, para decirle a Python que busque en la carpeta todos los tests y los ejecute.

```python
$ python -m unittest discover -v
```python

Otras comprobaciones en unittest
Anteriormente hemos visto el uso de __.assertEqual(a, b)__ _que simplemente verifica que dos valores a y b son iguales_, y de lo contrario da error. Sin embargo unittest nos ofrece un amplio abanico de opciones. Nótese que existen algunas variaciones usando “not”, como assertNotIn():
- __.assertEqual(a, b)__: Verifica la igualdad de ambos valores.
- __.assertTrue(x): Verifica que el valor es True.
- __.assertFalse(x): Verifica que el valor es False.
- __.assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
- __.assertIsNone(x): Verifica que el valor es None.
- __.assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
- __.assertIsInstance(a, b): Verifica que a es una instancia de b
- __.assertRaises(x): Verifica que se lanza una excepción.

```python
import unittest
class TestEjemplos(unittest.TestCase):
    def test_in(self):
        # Ok ya que 1 esta contenido en [1, 2, 3]
        self.assertIn(1, [1, 2, 3])

    def test_is(self):
        a = [1, 2, 3]
        b = a
        # Ok ya que son el mismo objeto
        self.assertIs(a, b)

    def test_excepcion(self):
        # Dividir 0/0 da error, pero es lo esperado por el test
        with self.assertRaises(ZeroDivisionError):
            x = 0/0
```

```python
$ python -m unittest -v tests

test_excepcion (tests.TestEjemplos) ... ok
test_in (tests.TestEjemplos) ... ok
test_is (tests.TestEjemplos) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

### Usando setUp y tearDown

Otra de las ventajas de usar unittest, es que nos ofrece la posibilidad de definir funciones comunes que son ejecutadas antes y después de cada test. Estos métodos son setUp() y tearDown().

```python
import unittest
class TestEjemplos(unittest.TestCase):
    def setUp(self):
        print("Entra setUp")
    def tearDown(self):
        print("Entra tearDown")

    def test_1(self):
        print("Test: test_1")
    def test_2(self):
        print("Test: test_2")
```

Siendo el resultado el siguiente. Podemos ver que hace una especie de sandwich con cada test, metiéndolo entre setUp y tearDown. Nótese que si ambas funciones realizan siempre lo mismo, tal vez se pueda usar un TestSuite con una función común para todos los tests, pero se trata de un concepto algo más avanzado que dejaremos para otro artículo.

```python
$ python -m unittest -v tests

test_1 (tests.TestEjemplos) ... Entra setUp
Test: test_1
Entra tearDown
ok
test_2 (tests.TestEjemplos) ... Entra setUp
Test: test_2
Entra tearDown
ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### Evitando Side Effects

_Hasta ahora hemos visto las herramientas que necesitamos para escribir nuestros tests, pero es también muy importante seguir una serie de buenas practicas a la hora de escribir nuestro código. Uno de los principios más importantes a seguir es el Principio de Responsabilidad Única o SRP, que nos dice que el código (bien sea una clase o una función) debe tener una única responsabilidad. Si hace demasiadas cosas, será más complicado de modificar y mantener, y además será más complicado de testear._

__Por lo tanto es tan importante escribir buenos tests que sean completos y tengan en cuenta todas las posibles casuísticas como escribir código que pueda ser testeado de manera fácil.__

# Referencias
- [Documentación Oficial Test Python](https://docs.python.org/es/3.9/library/test.html).