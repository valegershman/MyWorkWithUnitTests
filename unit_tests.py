from src.index import findMin, findMax, sumOfElements, multOfElements

import os
import unittest
import time
import psutil

class TestTZ1(unittest.TestCase):
    def setUp(self):
        self.lst = [1, 4, 2, 3]

    def test_findMin(self):
        self.assertEqual(findMin(self.lst), 1)

    def test_findMax(self):
        self.assertEqual(findMax(self.lst), 4)

    def test_sum(self):
        self.assertEqual(sumOfElements(self.lst), 10)

    def test_multiply(self):
        self.assertEqual(multOfElements(self.lst), 24)

    def testOnSpeed(self):
        content = os.listdir('temp')    # ['numbers.txt', 'numbers5000.txt', ...]
        for file in content:
            path = os.path.join('temp', file)     # temp/numbers.txt
            with open(path, 'r') as f:
                data = f.read()
                list_of_numbers = data.split()
                list_of_numbers = list(map(int, list_of_numbers))
                start = time.time()   # начало отсчета

                findMin(list_of_numbers)
                findMax(list_of_numbers)
                sumOfElements(list_of_numbers)
                multOfElements(list_of_numbers)

                end = time.time()    # конец отсчета
                print("Time elapsed during the calculation " + file + ":", end - start)    # время вычисления 4 наших функций

                self.assertLessEqual(end - start, 1)

    # Using memory in MB
    def testOnMemory(self):
        for i in range(0, 100000, 5000):
            temp = [x for x in range(0,i)]
            multOfElements(temp)
            used_memory = psutil.Process().memory_info().rss / (1024 * 1024)      # количество затраченной памяти (оперативной) в МБ
            print('Memory used on list with len ' + str(len(temp)) + ':'+ str(used_memory))

            self.assertLessEqual(used_memory, 100)


if __name__ == '__main__':
    unittest.main()