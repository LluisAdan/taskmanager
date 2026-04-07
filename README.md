# TaskManager

**TaskManager** es una aplicación de línea de comandos para la gestión de tareas, con integración opcional de IA para desglosar tareas complejas en subtareas simples utilizando OpenAI.

## Características

- Añadir, listar, completar y eliminar tareas.
- Persistencia automática de tareas en archivo `tasks.json`.
- Generación automática de subtareas a partir de descripciones complejas usando IA (OpenAI).
- Test unitarios con `pytest`.

## Instalación

1. Clona el repositorio y accede a la carpeta del proyecto:
	```bash
	git clone <url-del-repo>
	cd taskmanager
	```

2. Crea y activa un entorno virtual:
	```bash
	python3 -m venv .venv
	source .venv/bin/activate
	```

3. Instala las dependencias:
	```bash
	pip install -r requirements.txt
	```

4. (Opcional, para IA) Crea un archivo `.env` con tu clave de OpenAI:
	```
	OPENAI_API_KEY=tu_clave_aqui
	```

## Uso

Ejecuta la aplicación principal:
```bash
python main.py
```

### Opciones del menú

1. Añadir tarea manualmente.
2. Añadir tarea compleja (la IA la desglosa en subtareas simples).
3. Listar tareas.
4. Completar tarea.
5. Eliminar tarea.
6. Salir.

## Tests

Para ejecutar los tests:
```bash
pytest test_task_manager.py
```

## Dependencias principales

- Python 3.11+
- openai
- python-dotenv
- pytest

Consulta `requirements.txt` para la lista completa.

## Estructura del proyecto

- `main.py`: Interfaz principal de usuario.
- `task_manager.py`: Lógica de gestión de tareas.
- `ai_service.py`: Integración con OpenAI para desglosar tareas complejas.
- `test_task_manager.py`: Tests unitarios.
- `tasks.json`: Archivo de persistencia de tareas.
- `requirements.txt`: Dependencias.
