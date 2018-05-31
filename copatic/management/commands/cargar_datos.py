import time
import datetime

from openpyxl import load_workbook

from copatic.models.escuela import Escuela
from copatic.models.equipo import Equipo

from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

MODO_VERBOSE = True

def log(*k):
    global MODO_VERBOSE

    if MODO_VERBOSE:
        if isinstance(k, tuple):
            print (" ".join(k))
        else:
            print(k)

def esperar(segundos):
    time.sleep(segundos)

class Command(BaseCommand):
    help = 'Genera todos los datos iniciales.'

    def add_arguments(self, parser):
        parser.add_argument('--filtro', help="Aplica un filtro a los comandos que se ejecutaran")
        parser.add_argument('--depuracion', help="Permite activar todos los detalles (verbose mode)")
        parser.add_argument('--perfil_id', help="Permite aplicar un filtro de perfil al comando ejecutado")

    def handle(self, *args, **options):

        # A continuación están todos los comandos que el importador
        # puede ejecutar. Cada comando es un método, con el mismo nombre
        # que aparece como cadena.
        #
        # por ejemplo 'crear_areas' es la orden para ejecutar el método
        # self.crear_areas().
        comandos = [
            'importar_estado_de_tablero',
        ]

        print("Procesando comandos a ejecutar ...")
        esperar(1)

        print("Se ejecutaran %d comandos" %(len(comandos)))
        self.ejecutar_comandos(comandos)


    def ejecutar_comandos(self, comandos):
        esperar(1)
        self.listar_comandos(comandos)
        esperar(2)

        for i, x in enumerate(comandos):
            print("[01;32m[%d/%d] Ejecutando tarea: %s [0m" %(i+1, len(comandos)-i, x))
            metodo = getattr(self, x)
            metodo()

    def listar_comandos(self, comandos):
        print("Se ejecutaran los comandos en este orden:")
        for i, x in enumerate(comandos):
            print ("  %d %s" %(i+1, x))


    def importar_estado_de_tablero(self):
        ARCHIVO = './/archivos_para_importacion/copa-tic_tablero.xlsx'
        LIMITE_DE_FILAS = 800

        print("Comenzando la importación")
        log("Iniciando la importación del archivo: " + ARCHIVO)
        wb = load_workbook(ARCHIVO)

        columnas_como_string = ", ".join(wb.get_sheet_names())
        log("Las páginas de la planilla son: " + columnas_como_string)

        filas_procesadas = 0
        filas_omitidas_o_con_errores = 0
        filas_omitidas_lista = ""

        listado = ""

        def formatear_fecha(fecha):
            if fecha:
                return fecha.strftime('%Y-%m-%d')
            else:
                return fecha

        def obtener_valores_desde_fila(fila):
            return {
                "cue":                  str(fila[1].value),
                "eid":                  str(fila[2].value),
                "escuela":              str(fila[3].value),
                "localidad":            str(fila[4].value),
                "nombreDelEquipo":      str(fila[5].value),
                "dt":                   str(fila[6].value),
                "puntos":               str(fila[7].value),
                "a1estado":             str(fila[8].value),
                "a1link":               str(fila[9].value),
                "a2estado":             str(fila[10].value),
                "a2link":               str(fila[11].value),
                "a3estado":             str(fila[12].value),
                "a3link":               str(fila[13].value),
                "a4estado":             str(fila[14].value),
                "a4link":               str(fila[15].value),
                "a5estado":             str(fila[16].value),
                "a5link":               str(fila[17].value),
                "a6estado":             str(fila[18].value),
                "a6link":               str(fila[19].value),
                "a7estado":             str(fila[20].value),
                "a7link":               str(fila[21].value),
                "a8estado":             str(fila[22].value),
                "a8link":               str(fila[23].value),
                "a9estado":             str(fila[24].value),
                "a9link":               str(fila[25].value),
                "a10estado":             str(fila[26].value),
                "a10link":               str(fila[27].value),
                "a11estado":             str(fila[28].value),
                "a11link":               str(fila[29].value),
                "a12estado":             str(fila[30].value),
                "a12link":               str(fila[31].value),
                "a13estado":             str(fila[32].value),
                "a13link":               str(fila[33].value),
                "a14estado":             str(fila[34].value),
                "a14link":               str(fila[35].value),
                "a15estado":             str(fila[36].value),
                "a15link":               str(fila[37].value),
                "a16estado":             str(fila[38].value),
                "a16link":               str(fila[39].value),
            }

        cantidad_de_filas_con_datos = 0
        cantidad_de_filas_procesadas_sin_errores = 0

        for indice, fila in enumerate(wb.active.rows):

            if indice is 0:
                continue;             # Ignora la cabecera

            if not fila[0].value:
                log("Terminando en la fila %d porque no parece haber mas registros." %(indice + 1))
                break

            cantidad_de_filas_con_datos += 1
            log("Procesando fila '%d'" %(indice +1))

            try:
                valores = obtener_valores_desde_fila(fila)

                eid = valores['eid']
                escuela = valores['escuela']
                localidad = valores['localidad']
                nombreDelEquipo = valores['nombreDelEquipo']
                dt = valores['dt']
                puntos = valores['puntos']
                a1estado = valores['a1estado']
                a1link = valores['a1link']
                a2estado = valores['a2estado']
                a2link = valores['a2link']
                a3estado = valores['a3estado']
                a3link = valores['a3link']
                a4estado = valores['a4estado']
                a4link = valores['a4link']
                a5estado = valores['a5estado']
                a5link = valores['a5link']
                a6estado = valores['a6estado']
                a6link = valores['a6link']
                a7estado = valores['a7estado']
                a7link = valores['a7link']
                a8estado = valores['a8estado']
                a8link = valores['a8link']
                a9estado = valores['a9estado']
                a9link = valores['a9link']
                a10estado = valores['a10estado']
                a10link = valores['a10link']
                a11estado = valores['a11estado']
                a11link = valores['a11link']
                a12estado = valores['a12estado']
                a12link = valores['a12link']
                a13estado = valores['a13estado']
                a13link = valores['a13link']
                a14estado = valores['a14estado']
                a14link = valores['a14link']
                a15estado = valores['a15estado']
                a15link = valores['a15link']
                a16estado = valores['a16estado']
                a16link = valores['a16link']

                print("-----------------------------------------")
                print("Se va a procesar el equipo:")
                print("-----------------------------------------")
                print("ID: " + eid)
                print("Escuela: " + escuela)
                print("localidad: " + localidad)
                print("Nombre del Equipo: " + nombreDelEquipo)
                print("DT: " + dt)
                print("puntos: " + puntos)
                print("a1estado: " + a1estado)
                print("a1link: " + a1link)

                try:
                    equipo = Equipo.objects.get(eid=eid)
                except Equipo.DoesNotExist:
                    print("-----------------------------------")
                    print("No existe un equipo con ese id")
                    print("-----------------------------------")
                    continue

                equipo.nombre = nombreDelEquipo
                equipo.dt = dt
                if equipo.puntos:
                    equipo.puntos = int(float(puntos))
                else:
                    equipo.puntos = 0
                equipo.a1estado = a1estado
                equipo.a1link = a1link
                equipo.a2estado = a2estado
                equipo.a2link = a2link
                equipo.a3estado = a3estado
                equipo.a3link = a3link
                equipo.a4estado = a4estado
                equipo.a4link = a4link
                equipo.a5estado = a5estado
                equipo.a5link = a5link
                equipo.a6estado = a6estado
                equipo.a6link = a6link
                equipo.a7estado = a7estado
                equipo.a7link = a7link
                equipo.a8estado = a8estado
                equipo.a8link = a8link
                equipo.a9estado = a9estado
                equipo.a9link = a9link
                equipo.a10estado = a10estado
                equipo.a10link = a10link
                equipo.a11estado = a11estado
                equipo.a11link = a11link
                equipo.a12estado = a12estado
                equipo.a12link = a12link
                equipo.a13estado = a13estado
                equipo.a13link = a13link
                equipo.a14estado = a14estado
                equipo.a14link = a14link
                equipo.a15estado = a15estado
                equipo.a15link = a15link
                equipo.a16estado = a16estado
                equipo.a16link = a16link

                equipo.save()

                cantidad_de_filas_procesadas_sin_errores += 1

            except TypeError as e:
                log("-----")
                log("Fila %d - ****** OMITIDA, TypeError. La fila contiene caracteres incorrectos." %(indice + 1))
                filas_omitidas_o_con_errores += 1
                filas_omitidas_lista += ", " + str(indice + 1)
                log(str(e))
                log("-----")
                continue

            filas_procesadas += 1

            if indice > LIMITE_DE_FILAS:
                break


        log("Terminó la ejecución")

        print("")
        print("Resumen:")
        print("")
        print(" - cantidad total de filas:                       " + str(cantidad_de_filas_con_datos))
        print(" - filas procesadas:                              " + str(cantidad_de_filas_procesadas_sin_errores))
        print(" - cantidad de filas que fallaron:                " + str(cantidad_de_filas_con_datos - cantidad_de_filas_procesadas_sin_errores))
