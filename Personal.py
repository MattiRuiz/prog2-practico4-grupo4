import Datos

class Personal():

    def __init__(self, nombre= 0, apellido=0, dni=0, direccion=0, telefono=0, email=0, sueldo=0):
        self.conexionDB = Datos.DBConexion()
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.sueldo = sueldo
        self.direccion = direccion

    def traerPersonal(self):
        cursor = self.conexionDB.obtener_muchos("select * from personal")
        return cursor

    def traerTodosLosPeluqueros(self):
        cursor = self.conexionDB.obtener_muchos("select * from personal where anios_experiencia != '' ")
        return cursor

    def traerTodosLosRecepcionistas(self):
        cursor = self.conexionDB.obtener_muchos("select * from personal where anios_experiencia == '' ")
        return cursor
    
    def traerPorMonto(self,monto):
        cursor = self.conexionDB.obtener_muchos("select * from personal where sueldo >= {}".format(monto))
        return cursor

    
    
class Peluquero(Personal):
    _monto = 0
    _codigo = 0
    def __init__(self, nombre, apellido, dni, direccion, telefono, email, sueldo, aniosExp):
        self.conexionDB = Datos.DBConexion()
        super().__init__(nombre, apellido, dni, direccion, telefono, email, sueldo)
        self.aniosExp=aniosExp

    def crearCodigo(self):
        doc = str(self.dni)
        _codigo= "PQ_" + doc[-3:]
        return _codigo

    def guardarPeluquero(self):
        codigo = self.crearCodigo()
        query2= 'INSERT INTO personal (id, nombre, apellido, dni, direccion, telefono, email, sueldo, anios_experiencia) VALUES (\"{}\", \"{}\", \"{}\",\"{}\",\"{}\", \"{}\", \"{}\",\"{}\",\"{}\")'.format(codigo, self.nombre, self.apellido, self.dni,self.direccion, self.telefono, self.email, self.sueldo,self.aniosExp)
        self.conexionDB.ejecutar_query(query2)

    def eliminarPeluquero (self, codigo):
        query3 =f'DELETE FROM personal WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)

    def consularPorMonto(self,_monto):
        cursor = self.conexionDB.obtener_muchos("select * from personal where sueldo > {}".format(_monto))
        return cursor

    def modificarPeluquero(self, codigo):
        query3 =f'UPDATE personal SET nombre="{self.nombre}", apellido="{self.apellido}", dni="{self.dni}", telefono="{self.telefono}", anios_experiencia="{self.aniosExp}", email="{self.email}" , direccion="{self.direccion}", sueldo="{self.sueldo}" WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)

        
class Recepcionista(Personal):
     
    def __init__(self, nombre, apellido, dni, direccion, telefono, email, sueldo, aniosExpr=""):
        self.conexionDB = Datos.DBConexion()
        super().__init__(nombre, apellido, dni, direccion, telefono, email, sueldo)
        self.aniosExp=aniosExpr

    
    def crearCodigo(self):
        doc = str(self.dni)
        return "RC_" + doc[-3:]

    def modificarRecepcionista(self, codigo):
        query3 =f'UPDATE personal SET nombre="{self.nombre}", apellido="{self.apellido}", dni="{self.dni}", telefono="{self.telefono}", anios_experiencia="{""}", email="{self.email}" , direccion="{self.direccion}", sueldo="{self.sueldo}" WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)
    
    def guardarRecepcionista(self):
        codigo = self.crearCodigo()
        query2= 'INSERT INTO personal (id, nombre, apellido, dni, direccion, telefono, email, sueldo, anios_experiencia) VALUES (\"{}\", \"{}\", \"{}\",\"{}\",\"{}\", \"{}\", \"{}\",\"{}\",\"{}\")'.format(codigo, self.nombre, self.apellido, self.dni,self.direccion, self.telefono,self.email,self.sueldo, self.aniosExp)
        self.conexionDB.ejecutar_query(query2)

    def eliminarRecepcionista (self, codigo):
        query3 =f'DELETE FROM personal WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)
