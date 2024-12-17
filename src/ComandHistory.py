class Node:
    def __init__(self, command):
        self.command = command
        self.prev = None
        self.next = None


class CommandHistory:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.size = 0
        self.head = None  
        self.tail = None 

    def remove_oldest(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail 
            self.tail.next = self.head 
        self.size -= 1

    def add_command(self, command):
        new_node = Node(command)
        if not self.head:
            self.head = self.tail = new_node
            self.size = 1
            self.head.next = self.head
            self.head.prev = self.head
            return
        
        new_node.prev = self.tail
        new_node.next = self.head  
        self.tail.next = new_node  
        self.head.prev = new_node  
        self.tail = new_node       
        self.size += 1

        if self.size > self.max_size:
            self.remove_oldest()

    def set_size(self, new_size):
        self.max_size = new_size
        while self.size > new_size:
            self.remove_oldest()
    
    def get_commands(self):
        if not self.head:
            return []
        commands = []
        current = self.head
        for i in range(self.size):
            commands.append(current.command)
            current = current.next
        return commands
    
    def next_command(self, command):
        current = self.head
        if command == '':
            return current.command
        
        while current.command != command:
            current = current.next
            
        current = current.next
        return current.command
    
    def prev_command(self, command):
        current = self.tail
        if command == '':
            return current.command
        
        while current.command != command:
            current = current.prev
            
        current = current.prev
        return current.command