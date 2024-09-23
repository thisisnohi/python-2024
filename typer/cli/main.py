from typing import Annotated, Optional

import typer
from rich import print
from rich.console import Console

console = Console()

def main(name : Annotated[Optional[str], typer.Argument(help="The name of the user to greet")] = None):
    if name is None:
        print("Hello [bold red]World![/bold red] ")
    else:
        print(f"Hello [bold red] {name}![/bold red] ")


if __name__ == '__main__':
    typer.run(main)