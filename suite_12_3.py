from unittest import TestCase
import unittest
from Ex import Runner
import Ex
from pprint import pprint


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Serega')
        for i in range(10):
            runner.walk()
        self.assertEquals(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Stepan')
        for i in range(10):
            runner.run()
        self.assertEquals(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('Ivan')
        runner2 = Runner('Paul')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEquals(runner2.distance, runner1.distance)


class TestTournament(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    is_frozen = True

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner = Ex.Runner('Усэйн', 10)
        self.runner1 = Ex.Runner('Андрей', 9)
        self.runner2 = Ex.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def tearDown(self):
        pprint(self.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_run(self):
        tour = Ex.Tournament(90, self.runner, self.runner2)
        t_s = tour.start()
        self.all_results.update(t_s)
        self.assertTrue(self.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_run1(self):
        tour = Ex.Tournament(90, self.runner1, self.runner2)
        t_s = (tour.start())
        self.all_results.update(t_s)
        self.assertTrue(self.all_results[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_speed_run2(self):
        tour = Ex.Tournament(90, self.runner, self.runner1, self.runner2)
        t_s = tour.start()
        self.all_results.update(t_s)
        self.assertTrue(self.all_results[3] == 'Ник')

run = RunnerTest()
test = TestTournament()
