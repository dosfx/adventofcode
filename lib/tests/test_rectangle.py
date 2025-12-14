from unittest import TestCase

from aoc_lib import Rectangle, Vector2


class TestRectangle(TestCase):
    def test_area(self) -> None:
        self.assertEqual(Rectangle(1, 2, 3, 4).area, 12)

    def test_top(self) -> None:
        self.assertEqual(Rectangle(1, 2, 3, 4).top, 2)
        self.assertEqual(Rectangle.from_ints(1, 2, 3, 4).top, 2)

    def test_bot(self) -> None:
        self.assertEqual(Rectangle(1, 2, 3, 4).bot, 5)
        self.assertEqual(Rectangle.from_ints(1, 2, 3, 4).bot, 4)

    def test_left(self) -> None:
        self.assertEqual(Rectangle(1, 2, 3, 4).left, 1)
        self.assertEqual(Rectangle.from_ints(1, 2, 3, 4).left, 1)

    def test_right(self) -> None:
        self.assertEqual(Rectangle(1, 2, 3, 4).right, 3)
        self.assertEqual(Rectangle.from_ints(1, 2, 3, 4).right, 3)

    def test_contains(self) -> None:
        rect = Rectangle(1, 2, 3, 4)
        self.assertTrue(rect.contains(1, 2))
        self.assertTrue(rect.contains(3, 5))
        self.assertTrue(rect.contains(1, 5))
        self.assertTrue(rect.contains(3, 2))

        self.assertFalse(rect.contains(1, 1))

    def test_containsp(self) -> None:
        rect = Rectangle(1, 2, 3, 4)
        self.assertTrue(rect.containsp(Vector2(1, 2)))
        self.assertTrue(rect.containsp(Vector2(3, 5)))
        self.assertTrue(rect.containsp(Vector2(1, 5)))
        self.assertTrue(rect.containsp(Vector2(3, 2)))

        self.assertFalse(rect.containsp(Vector2(1, 1)))

    def test_from_ints(self) -> None:
        self.assertEqual(Rectangle(1, 1, 2, 2), Rectangle.from_ints(
            1, 1, 2, 2))
        self.assertEqual(Rectangle.from_ints(
            1, 1, 2, 2).area, 4)
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_ints(
            1, 2, 3, 5))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_ints(
            3, 5, 1, 2))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_ints(
            1, 5, 3, 2))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_ints(
            3, 2, 1, 5))

    def test_from_points(self) -> None:
        self.assertEqual(Rectangle(1, 1, 2, 2), Rectangle.from_points(
            Vector2(1, 1), Vector2(2, 2)))
        self.assertEqual(Rectangle.from_points(
            Vector2(1, 1), Vector2(2, 2)).area, 4)
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_points(
            Vector2(1, 2), Vector2(3, 5)))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_points(
            Vector2(3, 5), Vector2(1, 2)))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_points(
            Vector2(1, 5), Vector2(3, 2)))
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle.from_points(
            Vector2(3, 2), Vector2(1, 5)))
