import re
from dataclasses import dataclass

from base_solution import AdventOfCodeSolution
from utils import timer

problem_name = "Gear Ratios"
input_path = "2023/data/3.txt"


@dataclass
class Neighborhood:
    top: int
    right: int
    bottom: int
    left: int

    def __contains__(self, item: tuple[int, int]) -> bool:
        return self.top <= item[0] < self.bottom and self.left <= item[1] < self.right

    def __iter__(self):
        for row in range(self.top, self.bottom):
            for col in range(self.left, self.right):
                yield row, col


@dataclass
class Symbol:
    def __init__(self, symbol: str, row: int, left: int, length: int, plan_shape: tuple[int, int]):
        self.symbol = symbol
        self.neighborhood = Neighborhood(max(0, row - 1), min(plan_shape[1], left + length + 1), min(plan_shape[0], row + 2), max(0, left - 1))


@dataclass
class Part(Symbol):
    def __init__(self, number_str: str, row: int, left: int, length: int, plan_shape: tuple[int, int]):
        super().__init__(number_str, row, left, length, plan_shape)
        self.number = int(number_str)

    def __mul__(self, other: "Part") -> int:
        return self.number * other.number


@dataclass
class Star(Symbol):
    def __init__(self, row: int, col: int, plan_shape: tuple[int, int]):
        super().__init__("*", row, col, 1, plan_shape)
        self.position = (row, col)


class Solution(AdventOfCodeSolution):
    def __init__(self, problem_name: str, input_path: str):
        super().__init__(problem_name, input_path)
        self.plan_shape = (len(self.input_lines), len(self.input_lines[0]))
        self.__read_parts()
        self.__read_stars()

    def __read_parts(self) -> None:
        self.parts = []
        for row, line in enumerate(self.input_lines):
            for match in re.finditer(r"\d+", line):
                number_str = match.group()
                self.parts.append(Part(number_str, row, match.start(), len(number_str), self.plan_shape))

    def __read_stars(self) -> None:
        self.stars = []
        for row, line in enumerate(self.input_lines):
            for match in re.finditer(r"\*", line):
                self.stars.append(Star(row, match.start(), self.plan_shape))

    def _check_coordinate_for_symbol(self, row: int, col: int) -> bool:
        return not (self.input_lines[row][col].isdigit() or self.input_lines[row][col] == ".")

    @timer
    def part_one(self) -> str:
        found_parts = []
        for part in self.parts:
            for row, col in part.neighborhood:
                if self._check_coordinate_for_symbol(row, col):
                    found_parts.append(part.number)
                    break
        return str(sum(found_parts))

    def _get_neighboring_parts(self, star: Star) -> list[Part]:
        return [part for part in self.parts if star.position in part.neighborhood]

    @timer
    def part_two(self) -> str:
        gear_ratios = []
        for star in self.stars:
            neighboring_parts = self._get_neighboring_parts(star)
            if len(neighboring_parts) == 2:
                gear_ratios.append(neighboring_parts[0] * neighboring_parts[1])
        return str(sum(gear_ratios))


if __name__ == "__main__":
    Solution(problem_name, input_path).run()
