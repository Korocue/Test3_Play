import random
from dataclasses import dataclass


@dataclass
class GuessResult:
    status: str
    message: str


class NumberGuessGame:
    def __init__(self, lower: int = 1, upper: int = 100, max_attempts: int = 8) -> None:
        if lower > upper:
            raise ValueError("Lower bound must be less than or equal to upper bound")
        self.lower = lower
        self.upper = upper
        self.max_attempts = max_attempts
        self.target = random.randint(self.lower, self.upper)
        self.attempts = 0
        self.finished = False

    def guess(self, number: int) -> GuessResult:
        if self.finished:
            return GuessResult("finished", "ゲームはすでに終わっています。新しく始めてください。")

        self.attempts += 1

        if number == self.target:
            self.finished = True
            return GuessResult("correct", f"正解！ {self.attempts} 回目で当たりました。")

        if self.attempts >= self.max_attempts:
            self.finished = True
            return GuessResult(
                "finished",
                f"残念！ 正解は {self.target} でした。もう一度遊んでみてね。",
            )

        if number < self.lower or number > self.upper:
            remaining = self.max_attempts - self.attempts
            return GuessResult(
                "out_of_range",
                f"{self.lower}〜{self.upper} の範囲で入力してください。残り {remaining} 回。",
            )

        hint = "大きい" if number < self.target else "小さい"
        remaining = self.max_attempts - self.attempts
        return GuessResult("continue", f"もっと{hint}数字だよ。残り {remaining} 回。")


def play() -> None:
    print("\n==== 数当てゲーム ====")
    print("1〜100 の数字を当ててください。最大 8 回挑戦できます！\n")

    game = NumberGuessGame()

    while not game.finished:
        raw = input(f"{game.attempts + 1} 回目の予想: ")
        try:
            guess_value = int(raw)
        except ValueError:
            print("数字で入力してください。")
            continue

        result = game.guess(guess_value)
        print(result.message)

    print("また遊んでね！\n")


if __name__ == "__main__":
    play()
