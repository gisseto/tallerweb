from flask import Flask, escape,request, render_template   # importar la libreria
app=Flask(__name__) # inicializamos la app con el nombre
@app.route('/') # definimos que en la ruta de inicio sera aplicada la funcion hola
def hola():
    return 'hi penguins!' #retorno hi penguis!

@app.route('/coach')  #creamos la ruta coach
def hola_coahes(): #definimos la funcion que sera devuelta
    nombre='Gisselle'  #iniciamos un dato
    devolver=request.args.get('nombre',nombre) #definimos que sera devuelto y renderizado
    return f'Hola,{escape(devolver)}'  #retornamos al html

@app.route('/inicio') #creamos la ruta inicio
def inicio():
    return render_template('inicio.html')

@app.route('/contacto') #creamos la ruta inicio
def contacto():
    return render_template('contacto.html')

app.run(debug=True) # para ejecutar
