from ComandHistory import *

def test_add_command():
    """Тест на добавление команд в историю."""
    history = CommandHistory(3)
    history.add_command("ls")
    history.add_command("cd /")
    history.add_command("mkdir test")
    assert history.get_commands() == ['ls', 'cd /', 'mkdir test'], "test_add_command failed"

def test_exceeding_limit():
    """Тест на удаление старых команд при превышении лимита."""
    history = CommandHistory(2)
    history.add_command("ls")
    history.add_command("cd /")
    history.add_command("mkdir test")
    assert history.get_commands() == ["cd /", "mkdir test"], "test_exceeding_limit failed"

def test_reduce_size():
    """Тест на уменьшение размера истории."""
    history = CommandHistory(3)
    history.add_command("ls")
    history.add_command("cd /")
    history.add_command("mkdir test")
    history.set_size(2)  # Изменение максимального размера истории
    assert history.get_commands() == ["cd /", "mkdir test"], "test_reduce_size failed"

def test_increase_size():
    """Тест на увеличение размера истории."""
    history = CommandHistory(2)
    history.add_command("ls")
    history.add_command("cd /")
    history.set_size(4)  # Увеличение максимального размера
    history.add_command("mkdir test")
    history.add_command("touch file.txt")
    assert history.get_commands() == ["ls", "cd /", "mkdir test", "touch file.txt"], "test_increase_size failed"

def test_empty_history():
    """Тест на пустую историю команд."""
    history = CommandHistory(3)
    assert history.get_commands() == [], "test_empty_history failed"
# Запуск тестов
test_add_command()
test_exceeding_limit()
test_reduce_size()
test_increase_size()
test_empty_history()
print("Все тесты пройдены успешно!")