from typing import Annotated

import typer

# no_args_is_help 如果没有给定命令，则显示帮助消息
app = typer.Typer(no_args_is_help=True, help="Awesome CLI user manager.")

@app.command()
def create(name : Annotated[str, typer.Argument(help="请输入创建用户名称")]):
    """
        Create a new user with USERNAME.
    """
    print(f"Creating user: {name}")

@app.command()
def delete(name : Annotated[str, typer.Argument( help="请输入要删除的用户名称")],
           force : Annotated[bool, typer.Option(prompt="是否强制删除",help="强制删除 without confirmation.")],
           ):
    """
       Delete a user with USERNAME.

       If --force is not used, will ask for confirmation.
   """
    if force:
        print(f"Deleting user: {name}")
    else:
        print("Operation cancelled")

@app.command(deprecated=True)
def delete2(username: str):
    """
    Delete a user.

    This is deprecated and will stop being supported soon.
    """
    print(f"Deleting user: {username}")

@app.command()
def delete_all(
    force: Annotated[
        bool, typer.Option(prompt="Are you sure you want to delete ALL users?")
    ],
):
    """
        Delete ALL users in the database.

        If --force is not used, will ask for confirmation.
    """
    if force:
        print("Deleting all users")
    else:
        print("Operation cancelled")


if __name__ == "__main__":
    app()