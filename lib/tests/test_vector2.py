from unittest import TestCase

from aoc_lib._vector2 import Direction, Vector2


class TestDirection(TestCase):
    def test_direction_loop(self) -> None:
        self.assertEqual([d for d in Direction], [
            Direction.Up,
            Direction.Right,
            Direction.Down,
            Direction.Left,
        ])

    def test_direction_horizontal(self) -> None:
        self.assertFalse(Direction.Up.horizonal)
        self.assertTrue(Direction.Right.horizonal)
        self.assertFalse(Direction.Down.horizonal)
        self.assertTrue(Direction.Left.horizonal)

    def test_direction_vertical(self) -> None:
        self.assertTrue(Direction.Up.vertical)
        self.assertFalse(Direction.Right.vertical)
        self.assertTrue(Direction.Down.vertical)
        self.assertFalse(Direction.Left.vertical)

    def test_direction_clock(self) -> None:
        self.assertEqual(Direction.Up.clock(), Direction.Right)
        self.assertEqual(Direction.Right.clock(), Direction.Down)
        self.assertEqual(Direction.Down.clock(), Direction.Left)
        self.assertEqual(Direction.Left.clock(), Direction.Up)

    def test_direction_counter(self) -> None:
        self.assertEqual(Direction.Up.counter(), Direction.Left)
        self.assertEqual(Direction.Right.counter(), Direction.Up)
        self.assertEqual(Direction.Down.counter(), Direction.Right)
        self.assertEqual(Direction.Left.counter(), Direction.Down)


class TestVector2(TestCase):
    def test_point2(self) -> None:
        p = Vector2(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

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
        p1 = Vector2(1, 2)
        p2 = Vector2(3, 4)
        with self.subTest("first"):
            self.assertEqual(p1 - p2, Vector2(-2, -2))
        with self.subTest("flipped"):
            self.assertEqual(p2 - p1, Vector2(2, 2))

    def test_vector2_mul(self) -> None:
        self.assertEqual(Vector2(1, 2) * 3, Vector2(3, 6))

    def test_vector2_shift(self) -> None:
        point = Vector2(1, 2)
        self.assertEqual(point.shift(Direction.Up), Vector2(1, 1))
        self.assertEqual(point.shift(Direction.Right), Vector2(2, 2))
        self.assertEqual(point.shift(Direction.Down), Vector2(1, 3))
        self.assertEqual(point.shift(Direction.Left), Vector2(0, 2))

    def test_vector2_up(self) -> None:
        self.assertEqual(Vector2(1, 2).up(), Vector2(1, 1))

    def test_vector2_right(self) -> None:
        self.assertEqual(Vector2(1, 2).right(), Vector2(2, 2))

    def test_vector2_down(self) -> None:
        self.assertEqual(Vector2(1, 2).down(), Vector2(1, 3))

    def test_vector2_left(self) -> None:
        self.assertEqual(Vector2(1, 2).left(), Vector2(0, 2))
