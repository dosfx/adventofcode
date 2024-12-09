from unittest import TestCase

from aoc_lib._point2 import Point2



class TestPoint2(TestCase):
    def test_point2(self) -> None:
        p = Point2(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_point2_eq(self) -> None:
        self.assertEqual(Point2(3, 4), Point2(3, 4))

    def test_point2_set(self) -> None:
        s = set([Point2(4, 6), Point2(4, 6)])
        self.assertEqual(len(s), 1)

    def test_point2_add(self) -> None:
        self.assertEqual(Point2(1, 2) + Point2(3, 4), Point2(4, 6))

    def test_point2_neg(self) -> None:
        self.assertEqual(-Point2(3, 4), Point2(-3, -4))

    def test_point2_sub(self) -> None:
        p1 = Point2(1, 2)
        p2 = Point2(3, 4)
        with self.subTest("first"):
            self.assertEqual(p1 - p2, Point2(-2, -2))
        with self.subTest("flipped"):
            self.assertEqual(p2 - p1, Point2(2, 2))

    def test_point2_mul(self) -> None:
        self.assertEqual(Point2(1, 2) * 3, Point2(3, 6))