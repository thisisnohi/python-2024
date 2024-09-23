import typer
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

def main(name: str, lastname: str = "", formal: bool = False) -> None:
    """
        Say hi to NAME, optionally with a --lastname.

        If --formal is used, say hi very formally.
    """
    print(data)

    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")

    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)

    if formal:
        print(f"Good Day Mr. {name} {lastname}")
    else:
        print(f"Hello {name} {lastname}")

    message_start = "everything is "
    if formal:
        ending = typer.style("good", fg=typer.colors.GREEN, bold=True)
    else:
        ending = typer.style("bad", fg=typer.colors.WHITE, bg=typer.colors.RED)
    message = message_start + ending
    typer.echo(message)


if __name__ == "__main__":
    typer.run(main)