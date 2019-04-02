import click
import csv
from script.helpers import create_pdf


@click.group()
def main():
    """CSV script."""
    pass


@main.command()
@click.option('--file', '-f', help="CSV file name", required=True)
@click.option('--pdf', '-p', help="Pdf file", required=True)
@click.option('--delimiter', '-d', help="CSV delimiter", default=";")
def read(file, delimiter, pdf):

    with open(file, newline='') as csvfile:

        reader = csv.reader(csvfile, delimiter=delimiter)

        reader = list(reader)
        create_pdf(table=reader, out=pdf)


if __name__ == "__main__":
    main()