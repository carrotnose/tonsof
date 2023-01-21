from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter


command_completes = WordCompleter(["run", "alias"])


class Repl:
    def __init__(self):
        self.prompt_session = PromptSession(completer=command_completes)

    def run(self):
        while True:
            entry = self.prompt_session.prompt("ton> ")
            print(f"{entry=}")


if __name__ == "__main__":
    Repl().run()
