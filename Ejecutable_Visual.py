from Personal import Peluquero, Personal, Recepcionista
import Peluqueria

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import BOLD


root = Tk()
root.title("Peluquería Pelusa")
root.geometry("500x340")
root.resizable(width=None, height=None)
azulFondo = "#1b284c"
root.config(bg=azulFondo)
root.iconbitmap("paw.ico")

cabecera = Label(root, text="Peluquería Pelusa")
cabecera.place(x=120, y=30)
cabecera.config(font=("Verdana", 20, BOLD), bg=azulFondo, fg="#fff")
tituloOpciones = Label(root, text="Seleccione una de las siguientes opciones:")
tituloOpciones.place(x=115, y=75)
tituloOpciones.config(font=("Verdana", 10), bg=azulFondo, fg="#fff")

"""          Inicio de la ventana Perros          """
def ventanaPerros():
    # --- Interface ---
    vP = Toplevel()
    vP.title("Peluquería Pelusa")
    vP.geometry("800x600")
    vP.resizable(width=None, height=None)
    vP.config(bg=azulFondo)
    vP.iconbitmap("paw.ico")

    # --- Variables ---
    miID=IntVar()
    miNombre=StringVar()
    miDuenio=StringVar()
    miDireccion=StringVar()
    miTelefono=StringVar()
    Comportamiento=StringVar()
    miBanio=BooleanVar()
    miCorte=BooleanVar()

    # --- Funciones menú ---
    def cargarLista():
        try:
            mostrarPerros()
            messagebox.showinfo(title="Conexión exitosa", message="Se ha conectado correctamente a la base de datos")
        except:
            messagebox.showerror(title="Error", message="No fue posible conectar con la base de datos")

    def salirAplicacion():
        valor = messagebox.askquestion("Salir", "¿Está seguro que desea salir de la aplicación?")
        if valor == "yes":
            vP.destroy()
        else:
            pass

    def acercaDe():
        acerca = """
        UTN | TUP | Comisión 5

        Programación 2 
        TRABAJO PRÁCTICO INTEGRADOR
        Alumnos: Ruiz - Saraceni - Corvalan - Romano - Luraschi

        Versión 13.0

        Python ~ Tkinter ~ Sqlite3
        """
        messagebox.showinfo(title="Información del programa", message=acerca)

    # --- Funciones pantalla ---
    def mostrarPerros():
        registros = treePerros.get_children()
        for elemento in registros:
            treePerros.delete(elemento)
        try:
            
            miCursor = Peluqueria.Perro().traerPerros()
            for row in miCursor:
                treePerros.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        except:
            messagebox.showerror("Error", "No se pudo acceder a la BBDD")

    def limpiarCampos():
        miID.set("")
        miNombre.set("")
        miDuenio.set("")
        miDireccion.set("")
        miTelefono.set("")
        miBanio.set(False)
        miCorte.set(False)
        Comportamiento.set("(vacio)")

    def agregarPerro():
        try:
            nuevoPerro = Peluqueria.Perro(miNombre.get(), miDuenio.get(), miDireccion.get(), miTelefono.get())
            if miCorte.get() and miBanio.get():
                nuevoPerro.guardar(1,1,Comportamiento.get())
            elif miBanio.get() and miCorte.get() == False:
                nuevoPerro.guardar(1,0,Comportamiento.get())
            elif miCorte.get() and miBanio.get() == False:
                nuevoPerro.guardar(0,1,Comportamiento.get())
            else:
                nuevoPerro.guardar(0,0,Comportamiento.get())
            mostrarPerros()
            limpiarCampos()
        except:
            messagebox.showerror("Error", "No se pudo agregar el nuevo registro a la base de datos")

    def modificarPerro():
        try:
            if messagebox.askyesno(message="¿Realmente desea modificar el perro: {}?".format(miNombre.get()),
                                   title="ADVERTENCIA"):
                nuevoPerro = Peluqueria.Perro(miNombre.get(), miDuenio.get(), miDireccion.get(), miTelefono.get())
                if miBanio.get():
                    nuevoPerro.modificarPerro(1, 0, Comportamiento.get(),miID.get())
                elif miCorte.get():
                    nuevoPerro.modificarPerro(0, 1, Comportamiento.get(),miID.get())
                if miCorte.get() and miBanio.get():
                    nuevoPerro.modificarPerro(1, 1, Comportamiento.get(),miID.get())
                else:
                    nuevoPerro.modificarPerro(0,0, Comportamiento.get(),miID.get())
                mostrarPerros()
                limpiarCampos()
        except:
            messagebox.showerror("Error", "No se pudo modificar el registro")

    def borrarPerro():
        try:
           if messagebox.askyesno(message="¿Realmente desea eliminar el perro: {}?".format(miNombre.get()),
                                   title="ADVERTENCIA"):
                nuevoPerro = Peluqueria.Perro(miNombre.get(), miDuenio.get(), miDireccion.get(), miTelefono.get())
                nuevoPerro.borrarPerro(miID.get())
                mostrarPerros()
                limpiarCampos()
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro")

    # --- Widget ---

    # Menú
    menubar = Menu(vP)
    menuPrincipal = Menu(menubar, tearoff=0)
    menuPrincipal.add_command(label="Conectar Base de Datos", command=cargarLista)
    menuPrincipal.add_command(label="Salir", command=salirAplicacion)
    menubar.add_cascade(label="Inicio", menu=menuPrincipal)

    menuAyuda = Menu(menubar, tearoff=0)
    menuAyuda.add_command(label="Acerca de...", command=acercaDe)
    menubar.add_cascade(label="Ayuda", menu=menuAyuda)
    
    # Titulos
    cabecera = Label(vP, text="Peluquería Pelusa")
    cabecera.place(x=265, y=15)
    cabecera.config(font=("Verdana", 20, BOLD), bg=azulFondo, fg="#fff")

    tituloOpciones = Label(vP, text="- Gestor Sección Perros -")
    tituloOpciones.place(x=320, y=55)
    tituloOpciones.config(font=("Verdana", 10), bg=azulFondo, fg="#fff")

    # Botones

    botonPeluqueria = Button(vP, text="Cargar Perros")
    botonPeluqueria.place(x=350, y=85)
    botonPeluqueria.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2, command=mostrarPerros)

    # Tabla
    tituloPerros = Label(vP, text="Lista de perros:")
    tituloPerros.place(x=10, y=130)
    tituloPerros.config(width=110, height=20)

    treePerros=ttk.Treeview(tituloPerros, height=13, columns=('#0','#1','#2','#3','#4','#5','#6','#7',))
    treePerros.place(x=0, y=0)
    treePerros.column('#0', width=50)
    treePerros.heading('#0', text="ID", anchor=CENTER)
    treePerros.column('#1', width=120)
    treePerros.heading('#1', text="Nombre", anchor=CENTER)
    treePerros.column('#2', width=120)
    treePerros.heading('#2', text="Dueño", anchor=CENTER)
    treePerros.column('#3', width=120)
    treePerros.heading('#3', text="Dirección", anchor=CENTER)
    treePerros.column('#4', width=120)
    treePerros.heading('#4', text="Telefono", anchor=CENTER)
    treePerros.column('#5', width=60)
    treePerros.heading('#5', text="Baño", anchor=CENTER)
    treePerros.column('#6', width=60)
    treePerros.heading('#6', text="Corte", anchor=CENTER)
    treePerros.column('#7', width=110)
    treePerros.heading('#7', text="Comportamiento", anchor=CENTER)

    # --- Función tabla --- #
    def seleccionarUsandoClick(event):
        item=treePerros.identify('item', event.x, event.y)
        miID.set(treePerros.item(item, "text"))
        miNombre.set(treePerros.item(item, "values")[0])
        miDuenio.set(treePerros.item(item, "values")[1])
        miDireccion.set(treePerros.item(item, "values")[2])
        miTelefono.set(treePerros.item(item, "values")[3])
        Comportamiento.set(treePerros.item(item, "values")[6])

    treePerros.bind("<Double-1>", seleccionarUsandoClick)

    # Widget parte inferior
    labelNombre = Label(vP, text="Nombre:")
    labelNombre.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelNombre.place(x=38, y=465)
    entryNombre = Entry(vP, width=35, textvariable=miNombre)
    entryNombre.place(x=105, y=465)

    labelNombre = Label(vP, text="Nombre:")
    labelNombre.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelNombre.place(x=38, y=465)
    entryNombre = Entry(vP, width=35, textvariable=miNombre)
    entryNombre.place(x=105, y=465)

    labelDuenio = Label(vP, text="Dueño:")
    labelDuenio.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelDuenio.place(x=365, y=465)
    entryDuenio = Entry(vP, width=35, textvariable=miDuenio)
    entryDuenio.place(x=425, y=465)

    labelDireccion = Label(vP, text="Dirección:")
    labelDireccion.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelDireccion.place(x=30, y=500)
    entryDireccion = Entry(vP, width=35, textvariable=miDireccion)
    entryDireccion.place(x=105, y=500)

    labelTelefono = Label(vP, text="Telefono:")
    labelTelefono.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelTelefono.place(x=352, y=500)
    entryTelefono = Entry(vP, width=35, textvariable=miTelefono)
    entryTelefono.place(x=425, y=500)

    botonBuscar = Button(vP, text="Agregar", command=agregarPerro)
    botonBuscar.place(x=50, y=535, width=80)
    botonBuscar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonLimpiar = Button(vP, text="Limpiar", command=limpiarCampos)
    botonLimpiar.place(x=145, y=535, width=80)
    botonLimpiar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonModificar = Button(vP, text="Modificar", command=modificarPerro)
    botonModificar.place(x=240, y=535, width=80)
    botonModificar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonBorrar = Button(vP, text="Borrar", command=borrarPerro)
    botonBorrar.place(x=335, y=535, width=80)
    botonBorrar.config(font=("Verdana", 10), bg="#DF2935", fg="#fff", padx=10, pady=2)

    #Checkbox
    checkboxBanio=Checkbutton(vP, variable=miBanio)
    checkboxBanio.place(x=650, y=465)
    checkboxBanio.config(background=azulFondo)

    labelBanio=Label(vP, text="Baño")
    labelBanio.place(x=670, y=465)
    labelBanio.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")

    checkboxCorte=Checkbutton(vP, variable=miCorte)
    checkboxCorte.place(x=650, y=500)
    checkboxCorte.config(background=azulFondo)

    labelCorte=Label(vP, text="Corte")
    labelCorte.place(x=670, y=500)
    labelCorte.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")

    #ComboBox
    Comportamiento=ttk.Combobox(vP, values=["(vacio)","Muy mal", "Mal", "Bien", "Muy bien"], state="readonly")
    Comportamiento.place(x=570, y=540)
    Comportamiento.config(background=azulFondo)
    Comportamiento.current(0)

    labelmiComportamiento=Label(vP, text="Comportamiento:")
    labelmiComportamiento.place(x=445, y=540)
    labelmiComportamiento.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")

    # --- Finalización ventana Perro ---
    vP.config(menu=menubar)
    vP.mainloop()

"""          Inicio de la ventana Personal          """
def ventanaPersonal():

    # --- Interface ---
    v2 = Toplevel()
    v2.title("Peluquería Pelusa")
    v2.geometry("800x600")
    v2.resizable(width=None, height=None)
    v2.config(bg=azulFondo)
    v2.iconbitmap("paw.ico")

    # --- Variables ---
    persID = StringVar()
    persNombre = StringVar()
    persApellido = StringVar()
    persDni = StringVar()
    persTelefono = StringVar()
    persExperiencia = StringVar()
    persEmail = StringVar()
    persDireccion = StringVar()
    persSueldo = StringVar()
    filtroSueldo = StringVar()

    # --- Widget ---
    cabecera = Label(v2, text="Peluquería Pelusa")
    cabecera.place(x=265, y=15)
    cabecera.config(font=("Verdana", 20, BOLD), bg=azulFondo, fg="#fff")

    tituloOpciones = Label(v2, text="- Gestor Sección Personal -")
    tituloOpciones.place(x=315, y=55)
    tituloOpciones.config(font=("Verdana", 10), bg=azulFondo, fg="#fff")

    tituloPersonal = Label(v2, text="Lista de personal:")
    tituloPersonal.place(x=10, y=130)
    tituloPersonal.config(width=110, height=20)

    # Tabla
    treePersonal = ttk.Treeview(tituloPersonal, height=13,
                                columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8',))
    treePersonal.place(x=0, y=0)
    treePersonal.column('#0', width=70)
    treePersonal.heading('#0', text="ID", anchor=CENTER)
    treePersonal.column('#1', width=95)
    treePersonal.heading('#1', text="Nombre", anchor=CENTER)
    treePersonal.column('#2', width=95)
    treePersonal.heading('#2', text="Apellido", anchor=CENTER)
    treePersonal.column('#3', width=90)
    treePersonal.heading('#3', text="Dni", anchor=CENTER)
    treePersonal.column('#4', width=90)
    treePersonal.heading('#4', text="Telefono", anchor=CENTER)
    treePersonal.column('#5', width=40)
    treePersonal.heading('#5', text="Exp", anchor=CENTER)
    treePersonal.column('#6', width=118)
    treePersonal.heading('#6', text="Email", anchor=CENTER)
    treePersonal.column('#7', width=95)
    treePersonal.heading('#7', text="Dirección", anchor=CENTER)
    treePersonal.column('#8', width=80)
    treePersonal.heading('#8', text="Sueldo", anchor=CENTER)

    # --- Funciones ---
    def mostrarPersonal():
        registrosPers = treePersonal.get_children()
        for elemento in registrosPers:
            treePersonal.delete(elemento)
        try:
            miCursor = Personal().traerPersonal()
            for row in miCursor:
                treePersonal.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
            messagebox.showerror("Error", "No se pudo acceder a la BBDD.")
    
    def agregarPersonal():
        try:
            if puesto.get() == "Peluquero":
                personalPeluquero = Peluquero(nombre=persNombre.get(), apellido=persApellido.get(),dni=persDni.get(),direccion=persDireccion.get(),telefono=persTelefono.get(), email=persEmail.get(),sueldo=persSueldo.get(),aniosExp=persExperiencia.get())
                personalPeluquero.guardarPeluquero()
                messagebox.showinfo(message="Se agrego correctamente el personal con ID: " + personalPeluquero.crearCodigo(), title="Título")
          
            elif puesto.get()== "Recepcionista":
                personalRecepcionista = Recepcionista(nombre=persNombre.get(), apellido=persApellido.get(),dni=persDni.get(),direccion=persDireccion.get(),telefono=persTelefono.get(), email=persEmail.get(),sueldo=persSueldo.get())
                personalRecepcionista.guardarRecepcionista()
                messagebox.showinfo(message="Se agrego correctamente el personal con ID: " + personalRecepcionista.crearCodigo(), title="Título")
                entryExperiencia.config(state="normal")
            mostrarPersonal()
            limpiarCampos()
        except:
            messagebox.showerror("Error", "No se pudo agregar el nuevo registro a la base de datos")

    def modificarPersonal():
        try:
            if messagebox.askyesno(message="¿Realmente desea modificar el personal: {}?".format(persNombre.get()),
                                   title="ADVERTENCIA"):
                if persID.get()[:2] == "PQ":
                    personalPeluquero = Peluquero(nombre=persNombre.get(), apellido=persApellido.get(),dni=persDni.get(),direccion=persDireccion.get(),telefono=persTelefono.get(), email=persEmail.get(),sueldo=persSueldo.get(),aniosExp=persExperiencia.get())
                    personalPeluquero.modificarPeluquero(persID.get())
                elif persID.get()[:2]== "RC": 
                    entryExperiencia.config(state="disabled")
                    personalRecepcionista = Recepcionista(nombre=persNombre.get(), apellido=persApellido.get(),dni=persDni.get(),direccion=persDireccion.get(),telefono=persTelefono.get(), email=persEmail.get(),sueldo=persSueldo.get())
                    personalRecepcionista.modificarRecepcionista(persID.get())
                mostrarPersonal()
                limpiarCampos()
        except:
            messagebox.showerror("Error", "No se pudo modificar el registro.")
    
    def callback(*args):
        if puesto.get() == "Peluquero":
            entryExperiencia.config(state="normal")
        if puesto.get()== "Recepcionista" :
            entryExperiencia.config(state="disabled")

    def borrarPersonal():
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el personal: {}?".format(persNombre.get()),
                                   title="ADVERTENCIA"):
                
                if persID.get()[:2] == "PQ":
                    personalPeluquero = Peluquero(nombre=persNombre.get(), apellido=persApellido.get(),dni=persDni.get(),direccion=persDireccion.get(),telefono=persTelefono.get(), email=persEmail.get(),sueldo=persSueldo.get(),aniosExp=persExperiencia.get())
                    personalPeluquero.eliminarPeluquero(persID.get())
                elif persID.get()[:2]== "RC":
                    personalRecepcionista = Recepcionista(nombre=persNombre.get(), apellido=persApellido.get(),dni=persDni.get(),direccion=persDireccion.get(),telefono=persTelefono.get(), email=persEmail.get(),sueldo=persSueldo.get())
                    personalRecepcionista.eliminarRecepcionista(persID.get())
                mostrarPersonal()
                limpiarCampos()
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro.")

    def limpiarCampos():
        persID.set("")
        persNombre.set("")
        persApellido.set("")
        persDni.set("")
        persTelefono.set("")
        persExperiencia.set("")
        persEmail.set("")
        persDireccion.set("")
        persSueldo.set("")
    
    def mostrarPorSueldo():
        registrosPers = treePersonal.get_children()
        filtro = entryFiltro.get()
        
        for elemento in registrosPers:
            treePersonal.delete(elemento)
        try:
            miCursor = Personal().traerPorMonto(filtro)
            for row in miCursor:
                    treePersonal.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
                messagebox.showerror("Error", "No se pudo acceder a la BBDD.")

    # --- Función tabla ---
    def seleccionarPersUsandoClick(event):
        item = treePersonal.identify('item', event.x, event.y)

        persID.set(treePersonal.item(item, "text"))
        persNombre.set(treePersonal.item(item, "values")[0])
        persApellido.set(treePersonal.item(item, "values")[1])
        persDni.set(treePersonal.item(item, "values")[2])
        persTelefono.set(treePersonal.item(item, "values")[3])
        persExperiencia.set(treePersonal.item(item, "values")[4])
        persEmail.set(treePersonal.item(item, "values")[5])
        persDireccion.set(treePersonal.item(item, "values")[6])
        persSueldo.set(treePersonal.item(item, "values")[7])

    treePersonal.bind("<Double-1>", seleccionarPersUsandoClick)

    # --- Widgets ---
    botonCargar = Button(v2, text="Cargar Personal", command=mostrarPersonal)
    botonCargar.place(x=220, y=85)
    botonCargar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonMostrarPorSueldo = Button(v2, text="Filtrar por sueldo", command=mostrarPorSueldo)
    botonMostrarPorSueldo.place(x=420, y=85)
    botonMostrarPorSueldo.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    entryFiltro = Entry(v2, width=15, textvariable=filtroSueldo)
    entryFiltro.place(x=570, y=85, height=28)

    botonBuscar = Button(v2, text="Agregar", command=agregarPersonal)
    botonBuscar.place(x=220, y=550)
    botonBuscar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonLimpiar = Button(v2, text="Limpiar", command=limpiarCampos)
    botonLimpiar.place(x=313, y=550)
    botonLimpiar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonModificar = Button(v2, text="Modificar", command=modificarPersonal)
    botonModificar.place(x=400, y=550)
    botonModificar.config(font=("Verdana", 10), bg="#fff", fg="#000", padx=10, pady=2)

    botonBorrar = Button(v2, text="Borrar", command=borrarPersonal)
    botonBorrar.place(x=500, y=550)
    botonBorrar.config(font=("Verdana", 10), bg="#DF2935", fg="#fff", padx=10, pady=2)

    # Inputs
    labelNombre = Label(v2, text="Nombre:")
    labelNombre.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelNombre.place(x=20, y=455)
    entryNombre = Entry(v2, width=25, textvariable=persNombre)
    entryNombre.place(x=90, y=455)

    labelApellido = Label(v2, text="Apellido:")
    labelApellido.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelApellido.place(x=20, y=485)
    entryApellido = Entry(v2, width=25, textvariable=persApellido)
    entryApellido.place(x=90, y=485)

    labelDNI = Label(v2, text="DNI:")
    labelDNI.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelDNI.place(x=20, y=515)
    entryDNI = Entry(v2, width=25, textvariable=persDni)
    entryDNI.place(x=90, y=515)

    labelTelPers = Label(v2, text="Telefono:")
    labelTelPers.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelTelPers.place(x=260, y=455)
    entryTelPers = Entry(v2, width=25, textvariable=persTelefono)
    entryTelPers.place(x=350, y=455)

    labelEmail = Label(v2, text="Email:")
    labelEmail.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelEmail.place(x=260, y=485)
    entryEmail = Entry(v2, width=25, textvariable=persEmail)
    entryEmail.place(x=350, y=485)

    labelExperiencia = Label(v2, text="Experiencia:")
    labelExperiencia.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelExperiencia.place(x=260, y=515)
    entryExperiencia = Entry(v2, width=25, textvariable=persExperiencia)
    entryExperiencia.place(x=350, y=515)

    labelSueldo = Label(v2, text="Sueldo:")
    labelSueldo.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelSueldo.place(x=520, y=485)
    entrySueldo = Entry(v2, width=25, textvariable=persSueldo)
    entrySueldo.place(x=595, y=485)

    labelDireccion = Label(v2, text="Dirección:")
    labelDireccion.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")
    labelDireccion.place(x=520, y=455)
    entryDireccion = Entry(v2, width=25, textvariable=persDireccion)
    entryDireccion.place(x=595, y=455)

    #ComboBox
    puesto=ttk.Combobox(v2, values=["Peluquero", "Recepcionista"], state="readonly")
    puesto.place(x=595, y=515)
    puesto.config(background=azulFondo, width=22)
    puesto.current(0)
    puesto.bind("<<ComboboxSelected>>", callback)

    labelPuesto=Label(v2, text="Puesto:")
    labelPuesto.place(x=520, y=515)
    labelPuesto.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")

    # --- Finalización ventana Personal ---
    v2.mainloop()

# --- Widget del root ---
botonPeluqueria = Button(root, text="PERROS")
botonPeluqueria.place(x=90, y=115)
botonPeluqueria.config(font=("Verdana", 11, BOLD), bg="#fff", fg=azulFondo, command=ventanaPerros, height=8, width=15)

botonPersonal = Button(root, text="PERSONAL")
botonPersonal.place(x=270, y=115)
botonPersonal.config(font=("Verdana", 11, BOLD), bg="#fff", fg=azulFondo, command=ventanaPersonal, height=8, width=15)

nosotros = Label(root, text="Programación 2 | Trabajo práctico 4 | Grupo 4")
nosotros.place(x=110, y=290)
nosotros.config(font=("Verdana", 9), bg=azulFondo, fg="#fff")

# --- Finalización del código ---
root.mainloop()

