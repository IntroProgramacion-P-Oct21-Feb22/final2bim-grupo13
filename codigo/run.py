"""
    Proyecto Bimestral
    Segundo Bimestre

    Problemática:
   """


def obtenerMensaje(cuentas_creadas):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]

    if 1 <= cuentas_creadas <= 5:
        mensaje = (mensajeFinal[0])
    else:
        if 5 < cuentas_creadas <= 16:
            mensaje = (mensajeFinal[1])
        else:
            if cuentas_creadas > 16:
                mensaje = (mensajeFinal[2])
            else:
                mensaje= "No ha registrado cuentas"

    mensaje_retornado = ("Ha ingresado datos para %d cuentas\n%s" % (cuentas_creadas, mensaje))
    return mensaje_retornado


def crearFacebook():

    """
        Explication de método
        En este caso se comienza colocando todos los datos del internauta
        para la creacion de su cuenta, como se aprecia son de tipo String
        pero la Edad no lo es ya que esta es de tipo entero, a fin de cuentas
        se puede observar que el  internauta ingresa todos los datos y hace un
        retorno a la funcion principal para luego imprimirlo, esta pedira nombre del usuario,
        edad, ciudad, pais, correo electrónico.
    """
    print("Ingresar los siguientes datos por favor: ")
    nickname = input("Coloque nombre de Usuario: ")
    edad_usuario_ = input("Edad del Usuario: ")
    ciudad_usuario = input("Ciudad de origen del Usuario: ")
    pais_usuario = input("País de origen del Usuario: ")
    correo_usuario = input("Correo electrónico del Usuario: ")

    cadena_final = ("Creando cuenta de Facebook:\nNombre>> %s\nEdad>> %s\nCiudad>> %s\nPaís>> %s\n"
                    "Correo Electrónico>> %s"
                    % (nickname, edad_usuario_, ciudad_usuario, pais_usuario, correo_usuario))
    return cadena_final


def crearTwitter():
    """
        Explicación de método
        En este caso no va a devolver ningun valor como se ve en su principal característica, esto pedira lo siguiente
        nombre del usuario, nombres, apellidos, edad, ciudad, pais, idioma, correo electrónico.
    """
    print("Ingresar los siguientes datos por favor: ")
    nombre_usuario = input("Nombre de usuario: ")
    nombre = input("Ingresar el nombre personal del Usuario: ")
    apellido = input("Ingresar Apellidos del Usuario: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad de origen del Usuario: ")
    pais = input("Ingresar el País: ")
    idioma = input("Idioma: ")
    correo = input("Correo electrónico del Usuario: ")

    cadena_final = ("Creando cuenta de Twitter:\nUsuario>> %s\nNombre>> %s\nApellido>> "
                    "%s\nEdad>> %s\nCiudad>> %s\nPaís>> %s\nIdioma>> %s\nCorreo Electrónico>> %s"
                    % (nombre_usuario, nombre, apellido, edad, ciudad, pais, idioma, correo))
    print(cadena_final)


def crearWhatsapp():
    """
        Explicación de método
        Esta es una funcion porque va a retornar un valor y a su vez pedira lo siguiente: nombre del usuario,
        número de teléfono, edad, ciudad, pais.
    """
    print("Ingresar los siguientes datos por favor: ")
    nombre = input("Nombre de Usuario: ")
    numero = input("Número de Teléfono: ")
    edad = input("Edad del usuario: ")
    ciudad = input("Ciudad de Origen del Usuario: ")
    pais = input("País de origen del usuario: ")
    cadena_final = ("Creando cuenta de Whatsapp:\nNombre>> %s\nNúmero de teléfono>> %s\n"
                    "Edad del Usuario>> %s\nCiudad>> %s\nPaís>> %s"
                    % (nombre, numero, edad, ciudad, pais))
    return cadena_final


def crearTelegram():
    """
        Explicación de método
        Pues en este caso este proceso va acumular todos los datos en una cadena acumuladora y esta no va a devolver un
        valor, tambien pedira lo siguiente:nombre del usuario, número de teléfono,ciudad, pais, área de interés.
    """
    print("Ingresar los siguientes datos por favor: ")
    nombre_usuario = input("Nombre de usuario: ")
    numero = input("Número de teléfono: ")
    ciudad = input("Ciudad de origen del Usuario: ")
    pais = input("País de origen del usuario: ")
    area = input("Área de interés: ")

    cadena_final = ("Creando cuenta de Telegram:\nUsuario>> %s\nNúmero de teléfono>> %s\nCiudad>> %s\n"
                    "País>> %s\nÁrea de Interés>> %s"
                    % (nombre_usuario, numero, ciudad, pais, area))
    print(cadena_final)


def crearSignal():
    """
        Explicación de método
        En este caso  este metodo no  se considera una funcion ya que esta nos va a retornar un valor o un dato que se quiera retornar
        esta pedira lo siguiente nombre del usuario, número de teléfono, ciudad, pais, hobby principal
    """
    print("Ingresar los siguientes datos por favor: ")
    nombre = input("Nombre de Usuario: ")
    numero = input("Número de Teléfono: ")
    ciudad = input("Ciudad de Origen del Usuario: ")
    pais = input("País de origen del usuario: ")
    hobby = input("Hobby del Usuario: ")
    cadena_final = ("Creando cuenta de Signal:\nNombre>> %s\nNúmero de teléfono>> %s\n"
                    "Ciudad>> %s\nPaís>> %s\nHobby del Usuario>> %s"
                    % (nombre, numero, ciudad, pais, hobby))
    return cadena_final


def crearInstagram():
    """
       Explicación de método
       En este caso no va a devolver un valor
        como lo indica su principal característica pues esta lo que hara es pedir que el usuario ingrese  su nombre,
        ciudad, edad, correo electrónico.
    """
    print("Ingresar los siguientes datos por favor: ")
    nombre_user = input("Nombre de usuario: ")
    ciudad_user = input("Ciudad de origen del Usuario: ")
    edad_user = input("Edad Usuario: ")
    correo_user = input("Correo electrónico del Usuario: ")
    cadena_final = ("Creando cuenta de Instagram:\nNombre>> %s\nCiudad>> %s\nEdad>> %s\n"
                    "Correo Electrónico>> %s"
                    % (nombre_user, ciudad_user, edad_user, correo_user))
    print(cadena_final)


def crearFlickr():
    """
        Explicación de método
        En este caso retorna a un valor como lo indica su principal característica y tambien se pide por teclado
        nombre de usuario y correo electrónico.
    """
    print("Ingresar los siguientes datos por favor: ")

    nombre_user = input("Nombre de usuario: ")
    correo_user = input("Correo electrónico del Usuario: ")

    cadena_final = ("Creando cuenta de Flickr:\nUsuario>> %s\n"
                    "Correo Electrónico>> %s"% (nombre_user, correo_user))
    return cadena_final


if __name__ == "__main__":
    print("proceso inicial: ")
    contador = 0
    bandera = True
    while bandera:
        cuenta = int(input("Ingrese 1 para crear una cuenta en Facebook\n"
                           "Ingrese 2 para crear una cuenta en Twitter\n"
                           "Ingrese 3 para crear una cuenta en Whatsappk\n"
                           "Ingrese 4 para crear una cuenta en Telegram\n"
                           "Ingrese 5 para crear una cuenta en Signal\n"
                           "Ingrese 6 para crear una cuenta en Instagram\n"
                           "Ingrese 7 para crear una cuenta en Flickr\n"))
        if cuenta == 1:
            contador = contador + 1
            cuenta_faceboook = crearFacebook()
            print(cuenta_faceboook)
        else:
            if cuenta == 2:
                contador = contador + 1
                crearTwitter()
            else:
                if cuenta == 3:
                    contador = contador + 1
                    cuenta_whatsapp = crearWhatsapp()
                    print(cuenta_whatsapp)
                else:
                    if cuenta == 4:
                        contador = contador + 1
                        crearTelegram()
                    else:
                        if cuenta == 5:
                            contador = contador + 1
                            cuenta_signal = crearSignal()
                            print(cuenta_signal)
                        else:
                            if cuenta == 6:
                                contador = contador + 1
                                crearInstagram()
                            else:
                                if cuenta == 7:
                                    contador = contador + 1
                                    cuenta_flickr = crearFlickr()
                                    print(cuenta_flickr)
                                else:
                                    print("Error. El valor no se encuentra en las opciones a escoger\n")

        salida = input("Ingrese (si) para salir\n")
        if salida == "Si" or salida == "SI" or salida == "si":
            bandera = False

    mensaje_final = obtenerMensaje(contador)
    print(mensaje_final)
