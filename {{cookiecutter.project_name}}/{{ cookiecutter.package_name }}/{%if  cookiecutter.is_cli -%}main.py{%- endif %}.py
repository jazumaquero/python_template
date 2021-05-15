import click


@click.command()
@click.version_option()
def main():
    click.echo("{{cookiecutter.description}}.")


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")
