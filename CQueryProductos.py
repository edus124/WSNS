#import psycopg2
import datetime
import xml.etree.ElementTree as ET
from CBase import *
from CSql import *
from decorador import *
from Command import *
import json
import collections
from collections import namedtuple
from pymongo import *
import pprint
from bson.json_util import dumps
import re

class CQueryProductos(CBase,Command):
   pcParam = None
   lcIdCate = None
  
   def mxValParam(self):
       if not self.pcParam.has_key('CIDCATE'):
          self.pcError = 'PARAMETRO DE CATEGORIA DE PRODUCTO [CIDCATE]'
          return False
       return True  
      
   def mxEjecutarConsulta(self):
       self.lcIdCate = self.pcParam['CIDCATE']
       client = MongoClient()
       db = client.GAMESTORE
       if self.lcIdCate != '00':
          RS = db.productos.find({"CDESCAT.CIDCATE":self.lcIdCate}).sort("CITNAME", 1)
       else:
          RS = db.productos.find().limit(20).sort([("CDESCAT.CIDCATE", 1), ("CITNAME", 1)])
          #lcSql = "SELECT  nombreprod,precio,marca,stock,imagen,cdescri,cdescor FROM g01prod ORDER BY TMODIFI DESC LIMIT 20"
       if not RS:
          self.pcError = 'no hay productos' 
          return False
       i = 1;
       llist = []
       for R in RS:
         lcDicc = {"CITNAME":str(R.get("CITNAME")) ,"CITPRIC":str(R.get("NPRECIO")),"CMARCA":str(R.get("CMARCA")),"CSTOCK":str(R.get("NSTOCK")),"CIMGURL":str(R.get("CIMGURL")),"CDESCRI":R.get("CDESCOR").encode('ascii','ignore'),"CITDESC":R.get("CDESCOR").encode('ascii','ignore')}
         lcDicc = {"prod"+str(i):lcDicc }
         llist.append(lcDicc)
         i +=1
       self.pcData = json.dumps(llist)
       print ("Productos retornados")
       return True
 

 
