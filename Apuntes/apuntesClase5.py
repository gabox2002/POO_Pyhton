

"""
    Clase 5 - POO python
    Libreria
    Producto -PADRE
    HIJOS 3 CLASS (Libro, disco, peliculas)  
"""


class Producto: 
    def __init__(self, id, titulo, autor, precio, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock

def mostrarProducto(self):
    pass #delegar el cuerpo del metodo a la clase hijo

class Libro(Producto): #la clase libro extiende a producto
    def __init__(
            self, 
            id, 
            titulo, 
            autor, 
            precio, 
            stock,
            formato,
            cantHojas
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.formato = formato
        self.cantHojas = cantHojas

    def mostrarProducto(self):
        print(f'id: {self.id}')
        print(f'titulo: {self.titulo}')
        print(f'autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'formato: {self.formato}')
        print(f'cantHojas: {self.cantHojas}')


