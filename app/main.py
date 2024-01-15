from flask import Flask, render_template, request # pylint: disable=import-error
 # Importa las clases y funciones necesarias de Flask

app = Flask(__name__)  # Crea una instancia de la aplicación Flask

@app.route('/')
def index():
    """
    Ruta para la página principal.

    Returns:
        str: Renderiza la plantilla 'index.html'.
    """
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    """
    Ruta para el ejercicio 1.

    Returns:
        str: Renderiza la plantilla 'ejercicio1.html'.
    """
    resultado = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = 'Aprobado' if promedio >= 40 and asistencia >= 75 else 'Reprobado'

        resultado = {'promedio': promedio, 'estado': estado}

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    """
    Ruta para el ejercicio 2.

    Returns:
        str: Renderiza la plantilla 'ejercicio2.html'.
    """
    resultado = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        resultado = {
    'nombre_mas_largo': nombre_mas_largo,
    'cantidad_caracteres': cantidad_caracteres
}

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(
    debug=True
)  # Ejecuta la aplicación en modo de depuración si se ejecuta directamente el script
