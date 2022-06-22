import Datos

class Perro():

    def __init__(self, nombre = 0, dueno = 0, direccion= 0, telefono= 0):
        self.conexionDB = Datos.DBConexion()
        self.nombre = nombre
        self.dueno = dueno
        self.direccion = direccion
        self.telefono = telefono

    def traerPerros(self):
        cursor = self.conexionDB.obtener_muchos("select * from perro")
        return cursor

    def guardar(self, value1, value2, comportamiento):
        query = f'INSERT INTO perro VALUES(NULL,"{self.nombre}","{self.dueno}", "{self.direccion}", "{self.telefono}", "{value1}", "{value2}", "{comportamiento}")'
        self.conexionDB.ejecutar_query(query)

    def __str__(self):
        return ('{} {} {} {}'.format(self.nombre, self.dueno, self.direccion, self.telefono))
    
    def modificarPerro(self,banio, corte, comportamiento, id):
        query = f'UPDATE perro SET nombre="{self.nombre}", dueno="{self.dueno}", direccion="{self.direccion}", telefono="{self.telefono}", banio= banio, corte=corte, comportamiento="{comportamiento}" WHERE id={id}'
        if banio :
            query = f'UPDATE perro SET nombre="{self.nombre}", dueno="{self.dueno}", direccion="{self.direccion}", telefono="{self.telefono}", banio= banio+1, corte=corte, comportamiento="{comportamiento}" WHERE id={id}'
        elif corte:
            query = f'UPDATE perro SET nombre="{self.nombre}", dueno="{self.dueno}", direccion="{self.direccion}", telefono="{self.telefono}", banio= banio, corte=corte+1, comportamiento="{comportamiento}" WHERE id={id}'
        if corte and banio: 
           query = f'UPDATE perro SET nombre="{self.nombre}", dueno="{self.dueno}", direccion="{self.direccion}", telefono="{self.telefono}", banio= banio+1, corte=corte+1, comportamiento="{comportamiento}" WHERE id={id}'
        self.conexionDB.ejecutar_query(query)

    def borrarPerro(self, id):
        query3 =f'DELETE FROM perro WHERE id="{id}"'
        self.conexionDB.ejecutar_query(query3)