import unittest
from src.stack import Node, Stack

"""Здесь надо написать тесты с использованием unittest для модуля stack."""


class TestNode(unittest.TestCase):
    """ Тестирование функции Node """

    def setUp(self):
        """ Тестовые данные для теста: заданные два объекта класса Node """
        self.node_first = Node(5, None)
        self.node_second = Node('a', 5)

    def tearDown(self):
        pass

    def test_Node(self):
        """ Тест атрибутов класса Node """
        self.assertEqual(self.node_first.data, 5)  # проверяем как считывается атрибут data
        self.assertEqual(self.node_second.data, 'a')
        self.assertEqual(self.node_second.next_node, 5)  # проверяем как считывается атрибут next_node
        self.assertEqual(self.node_first.next_node, None)


class TestStack(unittest.TestCase):
    """ Тестирование функции Node """

    def setUp(self):
        """
        Тестовые данные для теста: заданный объект класса Stack
        Вызванный метод push трижды, для занесения добавления элементов в стек
        """
        self.stack = Stack()
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')

    def tearDown(self):
        pass

    def test_str(self):
        self.assertEqual(self.stack.__str__(), "data3\ndata2\ndata1")  # проверяем порядок добавления в стек

    def test_stack_push(self):
        self.assertEqual(self.stack.top.data, 'data3')  # проверяем верхний объект стека
        self.assertEqual(self.stack.top.next_node.data, 'data2')  # объект второй сверху
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')  # проверяем объект ниже, третий сверху
        # проверяем объект ещё ниже, но обнаруживаем, что такого нет
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            self.stack.top.next_node.next_node.next_node.data  # выводим ошибку, если запрашивают объект, которого нет

    def test_stack_pop(self):
        self.assertEqual(self.stack.top.data, 'data3')  # проверяем верхний объект стека
        self.assertEqual(self.stack.pop(), 'data3')  # удаляем верхний объект, получаем его значение
        self.assertEqual(self.stack.top.data, 'data2')  # проверяем какой объект теперь вверху стека
        self.assertEqual(self.stack.pop(), 'data2')
        self.assertEqual(self.stack.pop(), 'data1')
        # проверяем, что при удалении из пустого стека будет ошибка IndexError
        self.assertRaises(IndexError, self.stack.pop)
