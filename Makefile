FILES_ARGS=*.py


all: check

help:
	@echo "Commands:"
	@echo ""
	@echo "  format    ejecuta prettier y formatea automaticamente"
	@echo "  check     chequea el estilo de los archivos"
	@echo "  create_environment  crea el environment con todos los requerimientos"
	@echo ""

format:
	black $(FILES_ARGS)

check:
	black --check $(FILES_ARGS)
	flake8 $(FILES_ARGS)

server:
	python app.py

create_environment:
	conda env create -f environment.yml

