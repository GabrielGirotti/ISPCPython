class Libro:
    all = []

    def __init__(self, titulo: str, categoria: str, autor: str, paginas=0, edicion=0, codigo=str):
        assert paginas >= 0, f'La cantidad de paginas no puede ser menor a cero'
        assert edicion >= 0, f'El anio de edicion no puede ser menor a cero'

        self.titulo = titulo
        self.categoria = categoria
        self.autor = autor
        self.paginas = paginas
        self.edicion = edicion
        self.codigo = codigo

        Libro.all.append(self)

    def __repr__(self):
        return f'Libro {self.codigo}: Titulo: {self.titulo} / Categoria: "{self.categoria}" / Autor: {self.autor} / Cantidad de paginas: {self.paginas} / Anio de edicion {self.edicion}\n'

    catDrama = []
    catAccion = []
    catInfantil = []
    catDramaC = 0
    catAccionC = 0
    catInfantilC = 0

    def busqueda(lista):
        for instance in lista:
            if instance.categoria == "Infantil" or instance.categoria == "infantil":
                Libro.catInfantil.append(instance)
                Libro.catInfantilC += 1
            elif instance.categoria == "Drama" or instance.categoria == "drama":
                Libro.catDrama.append(instance)
                Libro.catDramaC += 1
            elif instance.categoria == "Accion" or instance.categoria == "accion":
                Libro.catAccion.append(instance)
                Libro.catAccionC += 1

    contTotal = 0

    def elimando(lista):
        libroABorrar = input('Ingrese el titulo que quiere borrar: ')
        for instancia in lista:
            if instancia.titulo == libroABorrar and instancia.categoria == "Infantil":
                print(f'Hemos eliminado el libro {libroABorrar}')
                Libro.contTotal -= 1
                Libro.catInfantil.remove(instancia)
                Libro.catInfantilC -= 1
                return Libro.all.remove(instancia)
            if instancia.titulo == libroABorrar and instancia.categoria == "Drama":
                print(f'Hemos eliminado el libro {libroABorrar}')
                Libro.contTotal -= 1
                Libro.catDrama.remove(instancia)
                Libro.catDramaC -= 1
                return Libro.all.remove(instancia)
            if instancia.titulo == libroABorrar and instancia.categoria == "Accion":
                print(f'Hemos eliminado el libro {libroABorrar}')
                Libro.contTotal -= 1
                Libro.catAccion.remove(instancia)
                Libro.catAccionC -= 1
                return Libro.all.remove(instancia)
        else:
            print(
                f'El libro {libroABorrar} no se encuentra en nuestros registros')
            Libro.elimando(lista)

    def longitud(mi_lista):
        for _ in range(len(mi_lista)):
            Libro.contTotal += 1


class pedidos(Libro):
    carrito = []

    def __init__(self, titulo: str, categoria: str, autor: str, paginas=0, edicion=0, codigo=str):
        super().__init__(
            titulo, categoria, autor, paginas, edicion, codigo
        )

    def agregandoACarrito(lista):
        libroXraAgregar = input(
            'Ingrese el titulo que quiere agregar a su carrito: ')
        for instancia in lista:
            if instancia.titulo == libroXraAgregar:
                print(f'Hemos agregado el libro {libroXraAgregar}')
                pedidos.carrito.append(instancia)
                return print(f'Estos son los libros en su carrito: {pedidos.carrito}')
        else:
            print(
                f'El titulo {libroXraAgregar} no se encuentra en nuestros registros')
            pedidos.agregandoACarrito(lista)

    def eliminandoDeCarrito():
        libroXraEliminar = input(
            'Ingrese el titulo que quiere eliminar de su carrito: ')
        for instancia in pedidos.carrito:
            if instancia.titulo == libroXraEliminar:
                print(f'Hemos eliminado el libro {libroXraEliminar}')
                pedidos.carrito.remove(instancia)
                return print(f'Estos son los libros en su carrito: {pedidos.carrito}')
        else:
            print(
                f'El titulo {libroXraEliminar} no se encuentra en nuestros registros')
            pedidos.eliminandoDeCarrito()

    def verTitulo(lista):
        titulos = []
        for instance in lista:
            titulos.append(instance.titulo)
        print(f'Los titulos de los libros en el carrito son: {titulos}')

    def nuevoCarrito(nuevoCarrito):
        nuevoCarrito = list()
        print(f'Se creo un nuevo carrito')


libro1 = pedidos("Cenicienta", "Infantil", "Disney", 800, 1697, "i-001")
libro2 = Libro("Programando en Python", "Drama", "Gabba", 1800, 2022, "d-001")
libro3 = Libro("Vistiendo a mi hijo de 2", "Drama",
               "Gabba", 51800, 2022, "d-002")
libro4 = Libro("Rambo", "Accion", "SS", 5100, 1986, "a-001")
libro5 = Libro("Pinocho", "Infantil", "Disney", 5100, 1883, "i-002")


'''------------------- PUNTO UNO ----------------------------
Libro.busqueda(Libro.all)
Libro.longitud(Libro.all)
print(
    f'Los libros en la categoria Infantil son {Libro.catInfantilC}: {Libro.catInfantil}')
print('---------------------------------------------------------------------------------------')
print(
    f'Los libros en la categoria Drama son {Libro.catDramaC}: {Libro.catDrama}')
print('---------------------------------------------------------------------------------------')
print(
    f'Los libros en la categoria Accion son {Libro.catAccionC}: {Libro.catAccion}')


print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
print(f'En total hay {Libro.contTotal} libros. Estos son: {Libro.all}')

print('---------------------------------------------------------------------------------------')
print('---------------------------------------------------------------------------------------')
Libro.elimando(Libro.all)

print(f'En total hay {Libro.contTotal} libros. Estos son: {Libro.all}')

print(
    f'Los libros en la categoria Infantil son {Libro.catInfantilC}: {Libro.catInfantil}')
print('---------------------------------------------------------------------------------------')
print(
    f'Los libros en la categoria Drama son {Libro.catDramaC}: {Libro.catDrama}')
print('---------------------------------------------------------------------------------------')
print(
    f'Los libros en la categoria Accion son {Libro.catAccionC}: {Libro.catAccion}')
    '''


pedidos.agregandoACarrito(Libro.all)
pedidos.agregandoACarrito(Libro.all)
pedidos.agregandoACarrito(Libro.all)
pedidos.eliminandoDeCarrito()
pedidos.verTitulo(pedidos.carrito)
pedidos.nuevoCarrito(nuevoCarrito='Uno')
pedidos.nuevoCarrito(nuevoCarrito='Dos')
