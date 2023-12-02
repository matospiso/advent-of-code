import re

from base_solution import AdventOfCodeSolution
from utils import timer

problem_name = "Cube Conundrum"
input_path = "2023/data/2.txt"


class Solution(AdventOfCodeSolution):
    COLORS = ["red", "green", "blue"]
    LIMITS = {"red": 12, "green": 13, "blue": 14}

    @staticmethod
    def parse_draw(unparsed: str) -> tuple[str, int]:
        parsed = unparsed.strip().split(" ")
        return parsed[1], int(parsed[0])

    @staticmethod
    def draws_from_line(line: str) -> list[tuple[str, int]]:
        line = line.split(":")[1].strip()
        return [Solution.parse_draw(draw) for draw in re.split(r"[,;]", line)]

    @classmethod
    def validate_draw(cls, draw: tuple[str, int]) -> bool:
        return draw[1] <= cls.LIMITS[draw[0]]

    @staticmethod
    def update_required_counts(required_counts: dict[str, int], draw: tuple[str, int]) -> None:
        color, count = draw
        required_counts[color] = max(required_counts[color], count)

    @timer
    def part_one(self) -> str:
        possible = 0
        for game, line in enumerate(self.input_lines, start=1):
            draws = self.draws_from_line(line)
            if all([self.validate_draw(draw) for draw in draws]):
                possible += game
        return str(possible)

    @timer
    def part_two(self) -> str:
        sum_of_powers = 0
        for line in self.input_lines:
            draws = self.draws_from_line(line)
            required_counts = {color: 0 for color in self.COLORS}
            for draw in draws:
                self.update_required_counts(required_counts, draw)
            counts_list = list(required_counts.values())
            sum_of_powers += counts_list[0] * counts_list[1] * counts_list[2]
        return str(sum_of_powers)


if __name__ == "__main__":
    Solution(problem_name, input_path).run()
