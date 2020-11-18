from abc import abstractmethod
from argparse import ArgumentParser, Namespace


class CliPlugin:
    def __init__(self, parser: ArgumentParser):
        pass

    @abstractmethod
    def execute(self, args: Namespace):
        """
        In a child class, this method is executed by a CLI plugin.
        """
