import typer


def main():
    user_name_input = typer.prompt("What's your name?")
    print(f'Hello {user_name_input}')
    user_pin_input = typer.prompt('Enter PIN')
    typer.echo(user_pin_input)



if __name__ == "__main__":
    typer.run(main)