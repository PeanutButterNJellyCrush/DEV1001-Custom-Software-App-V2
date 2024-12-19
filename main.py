import typer


def main():
    user_name_input = typer.prompt("What's your name?")
    print(f"Hello {user_name_input}")
    


if __name__ == "__main__":
    typer.run(main)