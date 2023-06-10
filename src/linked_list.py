class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.tail = None
        self.head = None
        self.length = 0
        self.values = []

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string[1:]

    def __repr__(self):
        """Представление списка в виде строки для разработки"""
        node = self.head
        values = []
        while node:
            values.append(str(node.data))
            node = node.next_node
        return " -> ".join(values)

    def __len__(self):
        """Возвращает длину списка"""
        return self.length

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.length += 1

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке LinkedList"""
        node = self.head
        while node:
            self.values.append(node.data)
            node = node.next_node
        return self.values

    def get_data_by_id(self, id_dict: int):
        """
        Возвращает первый найденный в LinkedList словарь с ключом 'id',
        значение которого равно переданному в метод значению.
        """
        if not isinstance(id_dict, int):
            raise TypeError('ID должно быть целочисленным числом.')  # ID должен быть целым числом

        node = self.head
        while node:
            try:
                if isinstance(node.data, dict) and 'id' in node.data:
                    if node.data['id'] == id_dict:
                        return node.data
                else:
                    raise ValueError('Данные не являются словарём или в словаре нет ID.')
            except ValueError as ex:
                print(ex)
            node = node.next_node
        raise ValueError(f'Элемента с номером {id_dict} нет.')  # Элемент с ID <номер> не найден.


