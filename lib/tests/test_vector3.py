from math import sqrt
from unittest import TestCase

from aoc_lib import Vector3


class TestVector3(TestCase):
    def test_vector3(self) -> None:
        v = Vector3(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)

    def test_vector3_eq(self) -> None:
        self.assertEqual(Vector3(3, 4, 5), Vector3(3, 4, 5))

    def test_vector3_set(self) -> None:
        s = set([Vector3(4, 6, 8), Vector3(4, 6, 8)])
        self.assertEqual(len(s), 1)

    def test_vector3_add(self) -> None:
        self.assertEqual(Vector3(1, 2, 3) + Vector3(3, 4, 3), Vector3(4, 6, 6))

    def test_vector3_neg(self) -> None:
        self.assertEqual(-Vector3(3, 4, 5), Vector3(-3, -4, -5))

    def test_vector3_sub(self) -> None:
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(3, 4, 5)
        with self.subTest("first"):
            self.assertEqual(v1 - v2, Vector3(-2, -2, -2))
        with self.subTest("flipped"):
            self.assertEqual(v2 - v1, Vector3(2, 2, 2))

    def test_vector3_mul(self) -> None:
        self.assertEqual(Vector3(1, 2, 3) * 3, Vector3(3, 6, 9))

    def test_vector3_dist(self) -> None:
        self.assertEqual(Vector3(1, 2, 3).dist(Vector3(2, 4, 6)), sqrt(14))

    def test_vector3_dist2(self) -> None:
        self.assertEqual(Vector3(1, 2, 3).dist2(Vector3(2, 4, 6)), 14)

    def test_vector3_len(self) -> None:
        self.assertEqual(Vector3(3, 4, 5).len(), sqrt(50))

    def test_vector3_len2(self) -> None:
        self.assertEqual(Vector3(3, 4, 5).len2(), 50)

    def test_vector3_mod(self) -> None:
        self.assertEqual(Vector3(1, 2, 3).mod(3), Vector3(1, 2, 0))
        self.assertEqual(Vector3(7, 8, 9).mod(4), Vector3(3, 0, 1))
        self.assertEqual(Vector3(-1, -2, -3).mod(3), Vector3(2, 1, 0))
        self.assertEqual(Vector3(-7, -8, -9).mod(4), Vector3(1, 0, 3))

    def test_vector3_mod2(self) -> None:
        self.assertEqual(Vector3(1, 2, 3).mod2(3, 4, 5), Vector3(1, 2, 3))
        self.assertEqual(Vector3(7, 8, 9).mod2(4, 5, 6), Vector3(3, 3, 3))
        self.assertEqual(Vector3(-1, -2, -3).mod2(3, 4, 5), Vector3(2, 2, 2))
        self.assertEqual(Vector3(-7, -8, -9).mod2(4, 5, 6), Vector3(1, 2, 3))
