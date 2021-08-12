from TestingWorker01.worker import Worker

from unittest import TestCase, main


class WorkerTest(TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_init_worker_properly(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_incremented_after_rest(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_worker_try_to_work_with_negative_energy_raises(self):
        worker = Worker("Test", 100, -1)
        self.assertEqual(-1, worker.energy)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_increase_after_work_method(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_energy_decrease_after_work_method(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_get_info_method_returns_what_we_need(self):
        worker_name = self.worker.name
        worker_money = self.worker.money

        self.assertEqual(f'{worker_name} has saved {worker_money} money.', self.worker.get_info())


if __name__ == '__main__':
    main()
