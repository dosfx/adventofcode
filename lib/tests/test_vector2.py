from unittest import TestCase

from aoc_lib import DOWN, LEFT, RIGHT, UP, directions, Vector2


class TestDirection(TestCase):
    def test_direction_loop(self) -> None:
        self.assertEqual([d for d in directions], [
            UP,
            RIGHT,
            DOWN,
            LEFT,
        ])


class TestVector2(TestCase):
    def test_vector2(self) -> None:
        v = Vector2(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

    def test_vector2_eq(self) -> None:
        self.assertEqual(Vector2(3, 4), Vector2(3, 4))

    def test_vector2_set(self) -> None:
        s = set([Vector2(4, 6), Vector2(4, 6)])
        self.assertEqual(len(s), 1)

    def test_vector2_add(self) -> None:
        self.assertEqual(Vector2(1, 2) + Vector2(3, 4), Vector2(4, 6))

    def test_vector2_neg(self) -> None:
        self.assertEqual(-Vector2(3, 4), Vector2(-3, -4))

    def test_vector2_sub(self) -> None:
        v1 = Vector2(1, 2)
        v2 = Vector2(3, 4)
        with self.subTest("first"):
            self.assertEqual(v1 - v2, Vector2(-2, -2))
        with self.subTest("flipped"):
            self.assertEqual(v2 - v1, Vector2(2, 2))

    def test_vector2_mul(self) -> None:
        self.assertEqual(Vector2(1, 2) * 3, Vector2(3, 6))

    def test_vector2_vertical(self) -> None:
        with self.subTest("True"):
            for v in (UP, DOWN, Vector2(0, 3)):
                self.assertTrue(v.vertical)
        with self.subTest("False"):
            for v in (LEFT, RIGHT, Vector2(3, 0), Vector2(1, 2)):
                self.assertFalse(v.vertical)

    def test_vector2_horizontal(self) -> None:
        with self.subTest("True"):
            for v in (LEFT, RIGHT, Vector2(3, 0)):
                self.assertTrue(v.horizonal)
        with self.subTest("False"):
            for v in (UP, DOWN, Vector2(0, 3), Vector2(1, 2)):
                self.assertFalse(v.horizonal)

    def test_vector2_clock(self) -> None:
        self.assertEqual(UP.clock, RIGHT)
        self.assertEqual(RIGHT.clock, DOWN)
        self.assertEqual(DOWN.clock, LEFT)
        self.assertEqual(LEFT.clock, UP)
        self.assertEqual(Vector2(1, 2).clock, Vector2(-2, 1))

    def test_vector2_counter(self) -> None:
        self.assertEqual(UP.counter, LEFT)
        self.assertEqual(LEFT.counter, DOWN)
        self.assertEqual(DOWN.counter, RIGHT)
        self.assertEqual(RIGHT.counter, UP)
        self.assertEqual(Vector2(1, 2).counter, Vector2(2, -1))
