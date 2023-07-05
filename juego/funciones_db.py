import sqlite3


def extraer_datos_db(datos_jugador):
    condicion = "Id"
    with sqlite3.connect("juego_pygame.db") as conexion:
        try: 
            sentencia = f'''
                        SELECT Nombre,Puntaje_actual FROM Jugadores WHERE {condicion} = 1
                        '''
            coleccion = conexion.execute(sentencia)
            for fila in coleccion:
                datos_jugador["Nombre"] = fila[0]
                datos_jugador["Puntos"] = fila[1]
            print("Datos extraidos con exito")
        except Exception as e:
            print(f"Error. No se pudo extraer los datos.\nRazon: {e}")

def extraer_datos_jugadores(lista_jugadores):
    with sqlite3.connect("juego_pygame.db") as conexion:
        try: 
            sentencia = '''
                        SELECT Nombre,Puntaje_actual FROM Jugadores ORDER BY Puntaje_actual DESC limit 3
                        '''
            coleccion = conexion.execute(sentencia)
            lista_jugadores.append(coleccion)
            print("Datos extraidos con exito") 
        except Exception as e:
            print(f"Error. No se pudo extraer los datos.\nRazon: {e}")

def extraer_permiso(datos_jugador: dict):
    with sqlite3.connect("juego_pygame.db") as conexion:
        try: 
            sentencia = '''
                        SELECT Nombre,Permiso FROM Jugadores WHERE Id = 1
                        '''
            coleccion = conexion.execute(sentencia)
            for fila in coleccion:
                datos_jugador["Nombre"] = fila[0]
                datos_jugador["Permiso"] = fila[1]
            print("Permisos extraidos con exito")
        except Exception as e:
            print(f"Error. No se pudo extraer los datos.\nRazon: {e}")

def actualizar_game_over_db(nivel,puntaje_actual):
    with sqlite3.connect("juego_pygame.db") as conexion:
        try: 
            sentencia = f'''
                        UPDATE Jugadores SET Puntaje_actual = ?, {nivel} = ? WHERE Id = 1
                        '''
            conexion.execute(sentencia,(puntaje_actual,puntaje_actual))
            print("Datos GAME OVER actualizados con exito")
        except Exception as e:
            print(f"Error. No se pudo actualizar los datos.\nRazon: {e}")

def actualizar_permiso(nivel,puntaje_actual,permiso):
    with sqlite3.connect("juego_pygame.db") as conexion:
        try: 
            sentencia = f'''
                        UPDATE Jugadores SET Puntaje_actual = ?, {nivel} = ?, Permiso = ? WHERE Id = 1
                        '''
            conexion.execute(sentencia,(puntaje_actual,puntaje_actual,permiso))
            print("Permisos actualizados con exito")
        except Exception as e:
            print(f"Error. No se pudo actualizar los datos.\nRazon: {e}")

