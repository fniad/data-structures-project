class Node:
    """Класс для узла стека"""

    def __init__(self, data: object, next_node: object) -> None:
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def __str__(self):
        """Возвращает пользователю строку со всеми добавленными элементами в стек"""
        result = ""
        node = self.top
        while node:
            result += str(node.data) + "\n"
            node = node.next_node
        new_result = result[:-1]
        return new_result

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        new_node = Node(data, self.top)
        self.top = new_node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            raise IndexError('Попытка удаления элемента из пустого стека')
        top = self.top
        self.top = self.top.next_node
        return top.data

