class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.tail is not None:
            self.tail.next_node = new_node
        self.tail = new_node

        if self.is_empty():
            self.head = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.is_empty():
            raise IndexError('Попытка удаления элемента из пустого стека')
        head = self.head
        self.head = head.next_node
        if self.is_empty():
            self.tail = None
        return head.data

    def is_empty(self):
        """Метод для проверки, пуста ли очередь"""
        return self.head is None

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = ""
        node = self.head
        while node:
            result += str(node.data) + "\n"
            node = node.next_node
        new_result = result[:-1]
        return new_result
