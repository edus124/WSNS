#! /usr/bin/env python
from flask import Flask, jsonify, request,render_template
from CQueryProductos import *
from CBusqueda import *
#from CDeudas import *
import json
import sys
from datetime import datetime
app = Flask(__name__)


@app.route('/cqueryOfertas1', methods=['GET'])
#Devuelve las Notas
def f_cqueryNotas():
    #st = '[{"prod1": {"CIMGURL":"http://media.ldlc.com/ld/products/00/01/69/25/LD0001692516_1.jpg","CITNAME":"Tarjeta de Video gtx 980 ti","CITDESC":"Tarjeta de video poderosa, para correr los ultimos juegos en 4K","CITPRIC":"1000.00$"}, {"prod2": "CIMGURL":"http://media.ldlc.com/ld/products/00/01/69/25/LD0001692516_1.jpg","CITNAME":"Tarjeta de Video gtx 980 ti","CITDESC":"Tarjeta de video poderosa, para correr los ultimos juegos en 4K","CITPRIC":"1000.00$"}]'
    item1 = '{"prod1":{"CIMGURL":"http://media.ldlc.com/ld/products/00/01/69/25/LD0001692516_1.jpg","CITNAME":"Tarjeta de Video GTX 980ti","CITDESC":"Tarjeta de video poderosa, para correr los ultimos juegos en 4K","CITPRIC":"1000.00$"}}'
    item2 = '{"prod2":{"CIMGURL":"https://ic.tweakimg.net/ext/i/2001106897.png","CITNAME":"Tarjeta de Video GTX 1070","CITDESC":"Tarjeta de video poderosa, para correr los ultimos juegos en 4K","CITPRIC":"900.00$"}}'
    print "-------"
    return "[" + item1 + "," + item2 + "]"


@app.route('/cqueryOfertas', methods=['POST'])
#Devuelve las Notas
def f_cqueryProductos():
    data = request.get_json(force=True)  
    lo = CQueryProductos()
    loInvoker =  Invoker(lo)
    lo.pcParam = data
    return loInvoker.omInicializar()
    
@app.route('/ccompra', methods=['POST'])
#Devuelve las Notas
def f_compra():
    data = request.get_json(force=True)
    print data
    return '{"OK":"OK"}'

@app.route('/cbusqueda', methods=['POST'])
#Devuelve las Notas
def f_BusquedaProductos():
    data = request.get_json(force=True)  
    lo = CBusqueda()
    loInvoker =  Invoker(lo)
    lo.pcParam = data
    return loInvoker.omInicializar()

if __name__ == '__main__':

  #app.run(host='localhost', debug=True, port=8080)
  app.run(host='0.0.0.0', debug=True, port=8081)
   #app.run(host='192.168.0.3', debug=True, port=8080)
   


   

