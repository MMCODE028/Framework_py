from turtle import st
from unicodedata import category

from sympy import numer


class Documento(object):

    def __init__(self, id : int = 0, titulo : str = "Titulo",numero_pag : int =  0, categoria : str = "categoria", autores: str = "autores"):
        self.id = id 
        self.titulo = titulo
        self.numero_pag = numero_pag
        self.categoria  = categoria
        self.autores = autores


    @property
    def id(self) -> int:
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    
    @property
    def titulo(self) -> str:
        return self.titulo

    
    @titulo.setter
    def titulo(self, titulo: str):
        self.titulo = titulo


    @property
    def numero_pag(self)->int:
        return self.numero_pag

    
    @numero_pag.setter
    def numero_pag(self, numero_pag: int):
        self.numero_pag = numero_pag


    @property
    def categoria(self) -> str:
        return self.categoria


    @categoria.setter
    def categoria(self, categoria:str):
        self.categoria = categoria



    @property
    def autores(self) -> str:
        return self.autores

    @autores.setter
    def autores(self, autores:str):
        self.autores = autores


    def __str__(self):
        return '( {0}, {1}, {2}, {3} , {4} , {5} )'.format(self.id, self.titulo, self.numero_pag, self.categoria, self.autores)
        
if  __name__ == '__main__':

    p = Documento(
        id = 0
        titulo = "Prueba",
        numero_pag=5,
        categoria=accion,
        autores="cc",
        )

    print(p)