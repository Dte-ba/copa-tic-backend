VERSION=$(shell git describe --tags)
NOMBRE=copatic-backend

N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

DB_NOMBRE_DEL_DUMP= ~/Dropbox/4cores/Backups/copatic/copatic_`date +'%Y%m%d_%Hhs%Mmin'`.dump

comandos:
	@echo ""
	@echo "${B}Comandos disponibles para ${G}${NOMBRE}${N} (versión: ${VERSION})"
	@echo ""
	@echo "  ${Y}Para desarrolladores${N}"
	@echo ""
	@echo "    ${G}iniciar${N}                            Instala todas las dependencias."
	@echo "    ${G}crear_migraciones${N}                  Genera las migraciones."
	@echo "    ${G}migrar${N}                             Ejecuta las migraciones."
	@echo "    ${G}test${N}                               Ejecuta los tests."
	@echo "    ${G}test_live${N}                          Ejecuta los tests de forma continua."
	@echo "    ${G}ejecutar${N}                           Ejecuta el servidor en modo desarrollo."
	@echo "    ${G}test_server${N}                        Ejecuta el servidor en modo test."
	@echo "    ${G}shell${N}                              Ejecuta un intérprete de python."
	@echo "    ${G}version${N}                            Incrementa la versión."
	@echo "    ${G}realizar_backup_desde_produccion${N}   Incrementa la versión."
	@echo ""
	@echo ""


iniciar:
	@pipenv install

crear_migraciones:
	@pipenv run "python manage.py makemigrations"

migrar:
	@pipenv run "python manage.py migrate --noinput"

clear:
	@clear;

test: clear migrar
	@echo "${G}Ejecutando tests ...${N}"
	dropdb --if-exists copatic-test -e; createdb copatic-test
	pipenv run flake8;pipenv run "python manage.py test" # -v 2

test_live:
	@make test; watchmedo shell-command --patterns="*.py" --recursive --command='make test' .

ejecutar:
	@pipenv run "python manage.py runserver"


testserver:
	@pipenv run "python manage.py testserver fixture.json"

shell:
	@pipenv run "python manage.py shell -i ipython"

version:
	@pipenv run bumpversion patch --verbose
	@git push
	@git push --tags


realizar_backup_desde_produccion:
	@echo "${G}Creando el archivo ${DB_NOMBRE_DEL_DUMP}${N}"
	@ssh dokku@enjambrelab.com.ar postgres:export copatic > ${DB_NOMBRE_DEL_DUMP}
