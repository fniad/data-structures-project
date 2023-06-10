"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import Node, LinkedList


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


class TestLinkedList(unittest.TestCase):
    """
    Тестирование класса LinkedList
    """
    def setUp(self):
        """ Тестовые данные для теста: заданные два объекта класса LinkedList """
        self.ll = LinkedList()
        # Добавляем данные
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})

    def tearDown(self):
        pass

    def test_str(self):
        """Проверяем вывод строки пользователю об элементах односвязного списка"""
        self.assertEqual(str(LinkedList()), 'None')  # если список пуст
        # если в список добавлено 4 объекта
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_repr(self):
        """Представление списка в виде строки для разработки"""
        self.assertEqual(LinkedList().__repr__(), '')
        self.assertEqual(self.ll.__repr__(), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3}")

    def test_len(self):
        """Возвращает длину списка"""
        self.assertEqual(self.ll.__len__(), 4)  # в списке 4 словаря

    def test_insert_beginning(self):
        """Добавление элемента вперёд списка"""
        self.ll.insert_beginning({'id': -1})
        self.assertEqual(self.ll.__repr__(), "{'id': -1} -> {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3}")

        # проверка на пустом списке
        ll2 = LinkedList()
        ll2.insert_beginning({'id': 0})
        self.assertEqual(ll2.head.data, {'id': 0})
        self.assertEqual(ll2.tail.data, {'id': 0})
        self.assertEqual(ll2.__repr__(), "{'id': 0}")

    def test_insert_at_end(self):
        """Добавление элемента в конец списка"""
        self.ll.insert_at_end({'id': 4})
        self.assertEqual(self.ll.__repr__(), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> {'id': 4}")

        # Проверка при добавлении в пустой список
        ll3 = LinkedList()
        ll3.insert_at_end({'id': 5})
        self.assertEqual(ll3.head.data, {'id': 5})
        self.assertEqual(ll3.tail.data, {'id': 5})


class Test_LinkedList_to_list_data_by_id(unittest.TestCase):
    """
        Тестирование класса LinkedList:
        функции test_to_list and get_data_by_id
    """

    def setUp(self):
        """ Тестовые данные для теста: заданные два объекта класса LinkedList """
        self.ll = LinkedList()
        # Добавляем данные
        self.ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        self.ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        self.ll.insert_beginning({'id': 0, 'username': 'serebro'})

    def tearDown(self):
        pass

    def test_to_list(self):
        """Возвращение списка с данными в списке"""
        self.assertEqual(self.ll.to_list(), [{'id': 0, 'username': 'serebro'},
                                             {'id': 1, 'username': 'lazzy508509'},
                                             {'id': 2, 'username': 'mik.roz'},
                                             {'id': 3, 'username': 'mosh_s'},
                                             ])

    def test_get_data_by_id(self):
        """
        Возврат первого найденного словаря с ключом id,
        значение которого передано по методу"""
        user_data = self.ll.get_data_by_id(3)
        self.assertEqual(user_data, {'id': 3, 'username': 'mosh_s'})

        # Проверка обработки ошибок
        ll4 = LinkedList()
        ll4.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll4.insert_at_end('idusername')
        ll4.insert_at_end([1, 2, 3])
        ll4.insert_at_end({'id': 2, 'username': 'mosh_s'})

        # Корректный поиск по ID
        self.assertEqual(ll4.get_data_by_id(2), {'id': 2, 'username': 'mosh_s'})

        # Проверка обработки ошибки некорректного типа ID
        with self.assertRaises(TypeError):
            ll4.get_data_by_id('2')

        # Проверка обработки ошибки отсутствия элемента с заданным ID
        with self.assertRaises(ValueError):
            ll4.get_data_by_id(4)

        # Проверка обработки ошибки при отсутствии элемента в списке
        with self.assertRaises(ValueError):
            ll4.get_data_by_id(3)
