from abc import ABCMeta, abstractmethod
import json
class CComponentConsulta:
    __metaclass__ = ABCMeta
    def __init__(self):
          self.pcParam = str()
          self.pcError = str()

    @abstractmethod
    def mxValParam(self):
        pass

class CConsultaConcreta(CComponentConsulta):
    def mxValParam(self):
       if not self.pcParam.has_key('CNRODNI'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CNRODNI] NO DEFINIDO'
          return False
       elif not self.pcParam.has_key('CTOKEN'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CTOKEN] NO DEFINIDO'
          return False
       return True

class CDecoradorConsulta(CComponentConsulta):

    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons
        
    def mxValParam(self):
        #CComponentConsulta.pcParam   = self.pcParam  
        return self.loComConsulta.mxValParam()



class CDecoradorHorario(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    def __init__(self, p_CompCons):
        super(self.__class__,self).__init__(p_CompCons)

    def mxValParam(self):
        if not self.pcParam.has_key('CCODUSU'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CCODUSU] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CPASSWORD'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CPASSWORD] NO DEFINIDO'
          return False
        return super(CDecoradorHorario,self).mxValParam()


class CDecoradorDeudas(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    
    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons     
    def mxValParam(self):
        if not self.pcParam.has_key('CCODUSU'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CCODUSU] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CPASSWORD'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CPASSWORD] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CPROYEC'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CPROYEC] NO DEFINIDO'
          return False
        return super(CDecoradorDeudas,self).mxValParam()

class CDecoradorNotas(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    
    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons     
    def mxValParam(self):
        if not self.pcParam.has_key('CCODUSU'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CCODUSU] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CPASSWORD'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CPASSWORD] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CPROYEC'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CPROYEC] NO DEFINIDO'
          return False
        return super(CDecoradorNotas,self).mxValParam()

class CDecoradorLogin(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    
    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons     
    def mxValParam(self):
        if not self.pcParam.has_key('CCODUSU'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CCODUSU] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CPASSWORD'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CPASSWORD] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CTOKEN'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CTOKEN] NO DEFINIDO'
          return False
        return True

class CDecoradorEventos(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    
    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons     
    def mxValParam(self):
        if not self.pcParam.has_key('CLIMIT'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CLIMIT] NO DEFINIDO'
          return False
        elif not self.pcParam.has_key('CUNIACA'):
          self.pcError = 'PARAMETRO TOKEN DE APLICACION [CUNIACA] NO DEFINIDO'
          return False
        return True

class CDecoradorMatriculas(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    
    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons     
    def mxValParam(self):
        if not self.pcParam.has_key('CCODUSU'):
          self.pcError = 'PARAMETRO DE CLAVE DE USUARIO [CLIMIT] NO DEFINIDO'
          return False
        return True
    
class CDecoradorConcreto(CDecoradorConsulta):
    anadido = None
    loComConsulta = None
    def __init__(self, p_CompCons):
        self.loComConsulta = p_CompCons     
    def mxValParam(self):
        CComponentConsulta.pcParam =self.pcParam
        print "aaaaaa", self.pcParam
        self.anadido = "PASSWORD Y TOKEN"
        return super(CDecoradorConcreto,self).mxValParam()
        print self.anadido
'''
c = CConsultaConcreta()
p = CDecoradorConcreto(c)
p.mxValParam("TUGFAAAAA")
'''
        
    
