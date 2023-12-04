from base_solution import AdventOfCodeSolution
from utils import timer

problem_name = "Scratchcards"
input_path = "2023/data/4.txt"


class Solution(AdventOfCodeSolution):
    def __init__(self, problem_name: str, input_path: str):
        super().__init__(problem_name, input_path)
        self.winning, self.yours = self.__read_scratchcards()

    def __read_scratchcards(self) -> tuple[list[dict[int, int]], list[list[int]]]:
        winning = []
        yours = []
        for line in self.input_lines:
            winning_part, your_part = tuple(line.split(":")[1].strip().split("|"))
            winning.append({int(number): 1 for number in winning_part.strip().split()})
            yours.append([int(number) for number in your_part.strip().split()])
        return winning, yours

    @timer
    def part_one(self) -> str:
        total = 0
        for winning_card, your_card in zip(self.winning, self.yours):
            matched = sum([winning_card.get(number, 0) for number in your_card])
            total += 2**(matched-1) if matched >= 1 else 0
        return str(total)

    @timer
    def part_two(self) -> str:
        card_counts = [1] * len(self.yours)
        for i, (winning_card, your_card) in enumerate(zip(self.winning, self.yours)):
            matched = sum([winning_card.get(number, 0) for number in your_card])
            for j in range(i+1, i+matched+1):
                card_counts[j] += card_counts[i]
        return str(sum(card_counts))


if __name__ == "__main__":
    Solution(problem_name, input_path).run()
