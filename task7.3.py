import unittest
import os
import shutil

def Path(path):
    os.makedirs(path, exist_ok=True)
    file_name = path + "\\1D.txt"
    with open(file_name, "w") as d:
        d.write("I won't let these little things slip out of my mouth\nBut if I do, it's you\nOh, it's you, they add up to\nI'm in love with you\nAnd all these little things")

class ThirdTask(unittest.TestCase):
    def setUp(self) -> None:
        Path("Macintosh HD\\Пользователи\\aleksandraholland\\PycharmProjects\\task7.3")

    def test_equality(self):
        with open('Macintosh HD\\Пользователи\\aleksandraholland\\PycharmProjects\\task7.3\\1D.txt', 'r') as to_check:
            text = to_check.read()
            self.assertEqual(text, "I won't let these little things slip out of my mouth\nBut if I do, it's you\nOh, it's you, they add up to\nI'm in love with you\nAnd all these little things")

    def tearDown(self) -> None:
        shutil.rmtree('Macintosh HD\\Пользователи\\aleksandraholland\\PycharmProjects\\task7.3')


if __name__ == '__main__':
    unittest.main()