import click
import constants


@click.group()
def cli():
    pass


@click.command()
def menu():
    """
    Prints menu to the command line
    """
    print("Menu:")
    for index, (name, pizza) in enumerate(constants.PIZZAS.items()):
        print(f"{index + 1} {name}: {pizza().dict()}")


@click.command()
@click.argument("pizza")
@click.option("-s", "--size", prompt="Enter a size of the pizza[L/XL]")
def cook(pizza, size):
    """
    Cooks pizza
    """
    if pizza not in constants.PIZZAS.keys():
        print("We don't have these pizza yet")
        return
    constants.PIZZAS[pizza](size).cook()


cli.add_command(menu)
cli.add_command(cook)


if __name__ == "__main__":
    cli()
