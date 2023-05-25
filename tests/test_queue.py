"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Node, Queue


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


class TextQueue(unittest.TestCase):
    """Queue"""
    def setUp(self):
        """
        Тестовые данные для теста: заданный объект класса Queue
        Вызванный метод queue трижды, для занесения добавления элементов в очередь
        """
        self.queue = Queue()
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')

    def tearDown(self):
        pass

    def test_str(self):
        """Проверяем вывод строки пользователю об элементах в очереди"""
        self.assertEqual(str(Queue()), "")  # если очередь пуста
        self.assertEqual(str(self.queue), "data1\ndata2\ndata3")  # если в очереди добавлено 3 объекта
        self.queue.dequeue()
        self.assertEqual(str(self.queue), "data2\ndata3")  # проверяем очередь после удаления объекта

    def test_queue_enqueue(self):
        """Проверяем добавление элемента в очередь"""
        self.assertEqual(self.queue.head.data, "data1")  # смотрим первый объект очереди
        self.assertEqual(self.queue.tail.data, "data3")  # смотрим последний объект очереди
        self.queue.enqueue("data4")
        self.assertEqual(self.queue.tail.data, "data4")  # смотрим последний объект после добавления

    def test_queue_dequeue(self):
        """Проверяем удаление элемента из очереди"""
        self.assertEqual(self.queue.head.data, "data1")  # смотрим первый объект очереди
        self.queue.dequeue()
        self.assertEqual(self.queue.head.data, "data2")  # смотрим первый объект очереди после удаления
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(self.queue.head, None)  # Удаляем все объекты и доходим до пустой очереди
        # Проверяем вывод ошибки при попутке удаления из пустой очереди
        self.assertRaises(IndexError, self.queue.dequeue)
