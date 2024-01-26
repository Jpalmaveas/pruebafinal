from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios registrados con sus contraseñas
usuarios_registrados = {
    'juan': 'admin',
    'pepe': 'user'
}

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
    resultado = None

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        # Calcular el total sin descuento
        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        # Aplicar descuento basado en la edad
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        # Calcular el total con descuento
        total_con_descuento = total_sin_descuento * (1 - descuento)

        # Crear el resultado a mostrar en la plantilla
        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'total_con_descuento': total_con_descuento,
        }

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None

    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # Verificar la autenticación del usuario
        if nombre in usuarios_registrados and usuarios_registrados[nombre] == contrasena:
            mensaje = f"Bienvenido {'administrador' if nombre == 'juan' else 'usuario'} {nombre}"
            resultado = {'mensaje': mensaje}
        else:
            resultado = {'mensaje': 'Nombre de usuario o contraseña incorrectos'}

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
