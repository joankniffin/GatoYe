from flask import Flask, render_template, request, session
from gato import asignar_simbolo, checar_disponible,checar_si_gano,limpia_tablero
#tablero_str = "123456789"
#tablero = { pos:pos for pos in tablero_str } # compresión | comprehension llave:valor
tablero = limpia_tablero()
tablero_limpio = limpia_tablero()

print(f"tablero:{id}")
app = Flask(__name__)
app.secret_key = "245635756735sdfhgsfgasrfhrtw45462"
movimientos = 0
gano=""
@app.route("/", methods=['GET','POST'])
def index():
    if request.method=='GET':
        session['tablero'] = tablero_limpio
        session['gano'] = ""
        session['movimientos']=0
        print(f"tablero:{id}")
        return render_template("index.html",celda=tablero_limpio,ganador="")
    else:
        if request.method == 'POST':
            if "repetir" not in request.form:
                celda = request.form['pos']
                tablero = session['tablero']
                gano = session['gano']
                movimientos = session['movimientos']            
                movimientos += 1
                print(celda)
                asignar_simbolo(tablero,celda,"X")
                print(tablero)         
                if checar_si_gano(tablero,"X") == True:
                    gano = "X"
                else:
                    if movimientos < 5:
                        celda = checar_disponible(tablero)
                        asignar_simbolo(tablero,celda,"O")
                        
                        if checar_si_gano(tablero,"O") == True:
                            gano = "O"
                    else:
                        if gano == "":
                            gano = "Empate"
                session['tablero'] = tablero
                session['gano']    = gano
                session['movimientos'] = movimientos
                return render_template("index.html",celda=tablero,ganador=gano)
            else:
                #limpiamos el tablero
                #tablero = { pos:pos for pos in tablero_str } # compresión | comprehension llave:valor
                session['tablero'] = tablero_limpio
                movimientos = 0
                session['movimientos'] = movimientos
                session['gano'] = ""
                print(f"tablero:{id}")
                return render_template("index.html",celda=tablero_limpio,ganador="")


if __name__ == "__main__":
    app.run(debug=True)
    