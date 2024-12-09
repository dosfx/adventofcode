from operator import concat
import os
from unittest import TestCase

from aoc_lib._grid import Grid


class TestGrid(TestCase):
    def setUp(self) -> None:
        self.grid = Grid(["1234", "2345", "3456"])

    def test_grid(self) -> None:
        self.assertEqual(self.grid.width, 4)
        self.assertEqual(self.grid.height, 3)

    def test_eq(self) -> None:
        self.assertEqual(self.grid, Grid(["1234", "2345", "3456"]))

    def test_str(self) -> None:
        self.assertEqual(str(self.grid), "1234\n2345\n3456")

    def test_at(self) -> None:
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                with self.subTest(f"{x},{y}"):
                    self.assertEqual(self.grid.at(x, y), str(x + y + 1))

    def test_contains(self) -> None:
        with self.subTest("inside"):
            self.assertTrue(self.grid.contains(0, 0))
            self.assertTrue(self.grid.contains(2, 2))
            self.assertTrue(self.grid.contains(3, 2))
        with self.subTest("outside"):
            self.assertFalse(self.grid.contains(-1, -1))
            self.assertFalse(self.grid.contains(0, -1))
            self.assertFalse(self.grid.contains(-1, 0))
            self.assertFalse(self.grid.contains(-1, -1))
            self.assertFalse(self.grid.contains(5, 5))
            self.assertFalse(self.grid.contains(4, 2))
            self.assertFalse(self.grid.contains(3, 3))

    def test_find(self) -> None:
        self.assertEqual(list(self.grid.find("3")),[
            (2, 0, "3"),
            (1, 1, "3"),
            (0, 2, "3"),
        ])

    def test_rows(self) -> None:
        self.assertEqual(list(self.grid.rows()), [
            (y, tuple([str(y + i) for i in range(1, 5)]))
            for y in range(3)
        ])

    def test_cells(self) -> None:
        self.assertEqual(list(self.grid.cells()), [
            (x, y, str(x + y + 1))
            for y in range(3)
            for x in range(4)
        ])

    def test_from_lines(self) -> None:
        grid = Grid.from_lines([
            "1234",
            "2345",
            "3456",
        ])
        self.assertEqual(grid, self.grid)

    def test_from_lines_sep(self) -> None:
        grid = Grid.from_lines([
            "1,2,3,4",
            "2,3,4,5",
            "3,4,5,6",
        ], ",")
        self.assertEqual(grid, self.grid)

    def test_from_file(self) -> None:
        grid = Grid.from_file(os.path.join(
            os.path.dirname(__file__), "grid.txt"))
        self.assertEqual(grid, self.grid)
