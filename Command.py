from abc import ABCMeta, abstractmethod
import inspect
import os


class Invoker(object):

    def __init__(self, command):
        self.command = command

    def omInicializar(self):    
        if self.command.omInitConsulta():
          self.command.omLog(str(self.command.pcParam), str(self.command.pcData))
          return self.command.pcData 
        else:
          self.command.omLog(str(self.command.pcParam), str(self.command.pcError))
          return self.command.pcError
          
          
class Command(object):
    """
    Clase Base Abstracta que es la base para todos los
    concreteCommand
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def omInitConsulta(self):
        pass




'''

class CreateCommand(Command):
    """
    Create command implementation.
    """
    def __init__(self, name):
        self.file_name = name

    def omEjecutarConsulta(self, name):
        open(self.file_name, 'w')
        print str(self) + ':::Method:::' + inspect.stack()[0][3]


class MoveCommand(Command):
    """
    Move command implementation.
    """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def omEjecutarConsulta(self, src, dest):
        os.rename(self.src, self.dest)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]


# Client for the command pattern
if __name__ == '__main__':
    create_cmd = CreateCommand('/tmp/foo.txt')
    move_cmd = MoveCommand('/tmp/foo.txt', '/tmp/bar.txt')
    create_invoker = Invoker(create_cmd)
    move_invoker = Invoker(move_cmd)
    create_invoker.do()
    move_invoker.do()
    move_invoker.undo()
    create_invoker.undo()
'''
