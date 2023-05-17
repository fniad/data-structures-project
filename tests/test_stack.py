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

    def test_Stack(self):
        self.assertEqual(self.stack.top.data, 'data3')  # проверяем верхний объект стека
        self.assertEqual(self.stack.top.next_node.data, 'data2')  # объект второй сверху
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')  # проверяем объект ниже, третий сверху
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)  # проверяем объект ещё ниже, но обнаруживаем, что такого нет
        with self.assertRaises(AttributeError):
            self.stack.top.next_node.next_node.next_node.data   # выводим ошибку, если запрашивают объект, которого нет
