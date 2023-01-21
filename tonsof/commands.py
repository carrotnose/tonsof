import json
import os
import subprocess


class CommandHandler:
    def __init__(self, proton_path: str, compat_path: str, alias_path: str):
        self.proton_path = proton_path
        self.compat_path = compat_path
        self.alias_path = alias_path
        self.aliases = None

    def load_aliases(self):
        try:
            with open(self.alias_path) as f:
                self.aliases = json.load(f)
        except:
            self.aliases = {}

    def save_aliases(self):
        with open(self.alias_path) as f:
            json.dump(self.aliases)

    def make_alias(self, name: str, content: str):
        self.aliases[name] = content
        self.save_aliases()

    def run_program(self, program_path: str):
        if program_path in self.aliases:
            program_path = self.aliases[program_path]
        p = subprocess.Popen(
            [
                self.proton_path,
                program_path
            ],
            env = dict(os.environ, **{
                "STEAM_COMPAT_DATA_PATH": self.compat_path
            })
        )
