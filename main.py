from flask import Flask, request, jsonify

app = Flask(__name__)

#Crear la ruta del endpoint
@app.route('/validar', methods=['POST'])
def validar():
    data=request.json
    nombre = data.get("nombre", "").strip()
    
    if len(nombre) > 3:
        url_notificacion = "https://servicio-notificacion-u0m2.onrender.com/notificar"
        try:
            requests.post(url_notificacion, json={"nombre": nombre})
        except Exception as e:
            print(f"Error llamando a notificación: {e}")
        
        return jsonify({"estado_validacion": "valido"})
    else:
        return jsonify({"estado_validacion": "No valido"})
