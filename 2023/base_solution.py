from abc import ABC, abstractmethod
from utils import timer


class AdventOfCodeSolution(ABC):
    """
    Abstract class for Advent of Code solutions

    Attributes:
        problem_name (str): Name of the problem used for logging
        input_path (str): Path to the input file
        input_lines (list[str]): Lines of the input file (stripped)
    """

    def __init__(self, problem_name: str, input_path: str):
        self.problem_name = problem_name
        self.input_path = input_path
        self.input_lines = self.__read_input()

    def __read_input(self) -> list[str]:
        """
        Reads the input file
        :return: lines of the input file
        """
        with open(self.input_path) as f:
            return [line.strip() for line in f.readlines()]

    @timer
    @abstractmethod
    def part_one(self) -> str:
        """
        Solves part one of the problem
        :return: Part one solution
        """
        pass

    @timer
    @abstractmethod
    def part_two(self) -> str:
        """
        Solves part two of the problem
        :return: Part two solution
        """
        pass

    def run(self) -> None:
        """
        Runs the solution
        :return: None
        """
        print(f"Solving {self.problem_name} ...")

        print(f"Solving part one ...")
        print(f"Solution: {self.part_one()}")

        print(f"Solving part two ...")
        print(f"Solution: {self.part_two()}")
