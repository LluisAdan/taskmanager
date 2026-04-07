import os
import json
import pytest
from task_manager import TaskManager

def setup_function(function):
    # Elimina el archivo de tareas antes de cada test
    if os.path.exists(TaskManager.FILENAME):
        os.remove(TaskManager.FILENAME)

def teardown_function(function):
    # Limpia el archivo de tareas después de cada test
    if os.path.exists(TaskManager.FILENAME):
        os.remove(TaskManager.FILENAME)

def test_add_task():
    tm = TaskManager()
    tm.add_task("Tarea de prueba")
    assert len(tm._tasks) == 1
    assert tm._tasks[0].description == "Tarea de prueba"
    assert not tm._tasks[0].completed

def test_list_task(capsys):
    tm = TaskManager()
    tm.add_task("Tarea 1")
    tm.list_task()
    captured = capsys.readouterr()
    assert "Tarea 1" in captured.out

def test_complete_task(capsys):
    tm = TaskManager()
    tm.add_task("Tarea a completar")
    tm.complete_task(1)
    assert tm._tasks[0].completed
    captured = capsys.readouterr()
    assert "Tarea completada" in captured.out

def test_delete_task(capsys):
    tm = TaskManager()
    tm.add_task("Tarea a eliminar")
    tm.delete_task(1)
    assert len(tm._tasks) == 0
    captured = capsys.readouterr()
    assert "Tarea eliminada" in captured.out

def test_complete_task_not_found(capsys):
    tm = TaskManager()
    tm.complete_task(99)
    captured = capsys.readouterr()
    assert "Tarea no encontrada" in captured.out

def test_delete_task_not_found(capsys):
    tm = TaskManager()
    tm.delete_task(99)
    captured = capsys.readouterr()
    assert "Tarea no encontrada" in captured.out

def test_persistence():
    tm = TaskManager()
    tm.add_task("Persistencia 1")
    tm.add_task("Persistencia 2")
    # Crea una nueva instancia para verificar la carga
    tm2 = TaskManager()
    assert len(tm2._tasks) == 2
    assert tm2._tasks[0].description == "Persistencia 1"
    assert tm2._tasks[1].description == "Persistencia 2"
