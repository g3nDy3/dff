
# Защита курсовой работы по АиСД

### Студент: Миллер Сергей Евгеньевич, группа 3382

## Задание на защиту
Реализовать функциb, которая будет выполнять следующие операции:
- выводить следующую команду
- выводить предыдущую команду

### Функция `next_command`
```
def next_command(self, command):
    current = self.head
    if command == '':
        return current.command
    
    while current.command != command:
        current = current.next
        
    current = current.next
    return current.command
```
### Функция `prev_command`
```
def prev_command(self, command):
    current = self.tail
    if command == '':
        return current.command
    
    while current.command != command:
        current = current.prev
        
    current = current.prev
    return current.command
```

### Реализация в main
```
elif choice == "4":
    command = history.next_command(now_command)
    now_command = command
    print(now_command)
    
    
elif choice == "5":
    command = history.prev_command(now_command)
    now_command = command
    print(now_command)
```
