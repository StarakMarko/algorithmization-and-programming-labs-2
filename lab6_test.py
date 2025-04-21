import unittest
from lab_6 import gas_supply


class TestFnc(unittest.TestCase):
    def test_empty_result(self):
        cities = ["Львів", "Стрий"]
        gas_storages = ["Сховище_1", "Сховище_2"]
        lst = [["Львів", "Стрий"], ["Сховище_2", "Львів"], ["Сховище_1", "Сховище_2"]]
        self.assertEqual(gas_supply(cities, gas_storages, lst), [])

    def test_example(self):
        cities = ["Львів", "Стрий", "Долина", "Жовква"]
        gas_storages = ["Сховище_1", "Сховище_2", "Сховище_3"]
        lst = [
            ["Львів", "Стрий"],
            ["Долина", "Львів"],
            ["Сховище_1", "Сховище_2"],
            ["Сховище_2", "Долина"],
            ["Сховище_3", "Жовква"],
        ]
        self.assertEqual(
            gas_supply(cities, gas_storages, lst),
            [
                ["Сховище_1", ["Жовква"]],
                ["Сховище_2", ["Жовква"]],
                ["Сховище_3", ["Стрий", "Львів", "Долина"]],
            ],
        )


unittest.main()
