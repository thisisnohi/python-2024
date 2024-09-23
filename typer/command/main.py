import typer


app = typer.Typer()

# app 指 app = typer.Typer() 定义的app变量
@app.command()
def main(name: str):
    print(f"Hello {name}")

if __name__ == '__main__':
    # 指向 app = typer.Typer() 定义的app变量
    app()