# Bibliotecas estándar de Python
La biblioteca estándar de Python ofrece una amplia gama de módulos útiles que cubren diversas áreas. Aquí tienes algunos ejemplos de módulos comúnmente utilizados:

1. **os**: Proporciona funciones para interactuar con el sistema operativo, como manipulación de archivos y directorios, obtener información del entorno y ejecutar comandos en la línea de comandos.
1. **datetime**: Permite trabajar con fechas, horas y operaciones relacionadas, como formateo, cálculos y comparaciones.
1. **random**: Proporciona funciones para generar números aleatorios y realizar operaciones relacionadas con la aleatoriedad, como selección aleatoria de elementos de una lista.
1. **math**: Contiene una variedad de funciones matemáticas, como trigonometría, logaritmos, exponenciales y más.
1. **json**: Permite trabajar con el formato de datos JSON, incluyendo la conversión de objetos Python a JSON y viceversa.
1. **re**: Proporciona funcionalidades para trabajar con expresiones regulares, permitiendo la búsqueda, extracción y manipulación de patrones de texto.
1. **csv**: Permite leer y escribir archivos CSV (valores separados por comas), un formato comúnmente utilizado para datos tabulares.
1. **urllib**: Proporciona herramientas para trabajar con URL, realizar solicitudes HTTP y manipular datos web.
1. **sqlite3**: Permite interactuar con bases de datos SQLite, incluyendo la creación, consulta y modificación de tablas y registros.
1. **argparse**: Facilita la creación de interfaces de línea de comandos, permitiendo definir argumentos y opciones con sus respectivas acciones y validaciones.

Estos son solo algunos ejemplos, pero la biblioteca estándar de Python contiene muchos más módulos útiles para diferentes propósitos. Puedes explorar la documentación oficial de Python para obtener más información sobre cada uno de ellos y descubrir nuevas funcionalidades según tus necesidades específicas.

Documentación:  <https://docs.python.org/3/library/index.html>

PIP (Instalador de Paquetes de Python) 

Es una herramienta que facilita la instalación, actualización y desinstalación de paquetes de Python de PyPI (Python Package Index), que es el repositorio público de paquetes de Python.

Aquí tienes cómo utilizar PIP para instalar y desinstalar paquetes listos para usar desde PyPI:

1. Instalación de paquetes con PIP:
   1. Abre una terminal o línea de comandos en tu sistema operativo.
   1. Para instalar un paquete, usa el siguiente comando: **pip install nombre\_paquete**. Por ejemplo, si deseas instalar el paquete "requests", ejecuta **pip install requests**.
   1. PIP buscará el paquete en PyPI y descargará e instalará automáticamente la última versión disponible del paquete junto con sus dependencias.
1. Actualización de paquetes con PIP:
   1. Para actualizar un paquete a la última versión disponible, usa el siguiente comando: **pip install --upgrade nombre\_paquete**. Por ejemplo, si deseas actualizar el paquete "requests", ejecuta **pip install --upgrade requests**.
   1. PIP verificará si hay una versión más reciente del paquete en PyPI y actualizará tu instalación existente.
1. Desinstalación de paquetes con PIP:
   1. Si deseas desinstalar un paquete, usa el siguiente comando: **pip uninstall nombre\_paquete**. Por ejemplo, si deseas desinstalar el paquete "requests", ejecuta **pip uninstall requests**.
   1. PIP eliminará el paquete y todos sus archivos relacionados de tu entorno de Python.

En el ámbito de la ciencia de datos, hay varias bibliotecas y paquetes de Python que son ampliamente utilizados debido a su potencia y versatilidad para el análisis de datos, la visualización y el aprendizaje automático. Aquí te presento algunas de las bibliotecas más comunes:

1. **NumPy**: Esencial para computación numérica en Python. Proporciona matrices multidimensionales y funciones para realizar operaciones matemáticas de manera eficiente.
1. **Pandas**: Ofrece estructuras de datos de alto nivel y herramientas de análisis de datos. Es especialmente útil para manipular y analizar datos tabulares.
1. **Matplotlib**: Una biblioteca de trazado 2D que produce figuras de calidad de publicación en una variedad de formatos y entornos.
1. **Seaborn**: Basado en Matplotlib, Seaborn proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos y informativos.
1. **Scikit-learn**: Es una biblioteca de aprendizaje automático simple y eficiente para Python. Contiene implementaciones de una amplia gama de algoritmos de aprendizaje supervisado y no supervisado.
1. **TensorFlow** y **PyTorch**: Son bibliotecas de aprendizaje profundo que permiten construir y entrenar modelos de redes neuronales para tareas de aprendizaje automático.
1. **SciPy**: Proporciona rutinas eficientes para la integración numérica, la interpolación, la optimización, el álgebra lineal y muchas otras tareas comunes en ciencia e ingeniería.
1. **Statsmodels**: Ofrece clases y funciones para la estimación de modelos estadísticos, realización de pruebas estadísticas y exploración de datos estadísticos.
1. **XGBoost** y **LightGBM**: Son bibliotecas de gradiente potenciado que son muy populares en competiciones de ciencia de datos y se utilizan para problemas de clasificación y regresión.
1. **Keras**: Proporciona una API de alto nivel para construir y entrenar modelos de redes neuronales. Es más fácil de usar y más flexible que TensorFlow y PyTorch para muchas aplicaciones.



Es importante tener en cuenta que PIP instala paquetes de Python a nivel de sistema o en entornos virtuales específicos. Si estás utilizando un entorno virtual, asegúrate de activarlo antes de ejecutar los comandos de PIP.

PIP también proporciona otras funcionalidades, como la instalación de paquetes desde archivos de distribución local, la instalación de versiones específicas de paquetes y la gestión de requisitos de paquetes en un archivo **requirements.txt**.
