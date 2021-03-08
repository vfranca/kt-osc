from kt_var import var
import click


@click.command()
@click.argument("preco-final")
@click.argument("preco-inicial")
def cli(preco_final, preco_inicial):
    """Calcula variacao percentual de b em a."""
    click.echo(var.var(float(preco_final), float(preco_inicial)))


if __name__ == "__main__":
    cli()
