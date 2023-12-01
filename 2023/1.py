import re

from base_solution import AdventOfCodeSolution
from utils import timer

problem_name = "Trebuchet?!"
input_path = "2023/data/1.txt"


class Solution(AdventOfCodeSolution):
    @timer
    def part_one(self) -> str:
        digits = [str(i) for i in range(10)]
        total = 0
        for line in self.input_lines:
            first = last = ""
            for c in line:
                if c not in digits:
                    continue
                if first == "":
                    first = c
                last = c
            if first == "":
                continue
            total += int(first + last)
        return str(total)

    @timer
    def part_two(self) -> str:
        written = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        digits = [str(i) for i in range(10)]
        written2digit = {w: d for w, d in zip(written+digits, digits+digits)}
        pattern = re.compile("|".join([f"(?=({string}))" for string in written] + ["([0-9])"]))
        total = 0
        for line in self.input_lines:
            matches = re.findall(pattern, line)
            first = written2digit["".join(matches[0])]
            last = written2digit["".join(matches[-1])]
            total += int(first + last)
        return str(total)


if __name__ == "__main__":
    solution = Solution(problem_name, input_path)
    solution.run()
