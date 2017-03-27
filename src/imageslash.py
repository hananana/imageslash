# coding: UTF-8

import click
from PIL import Image


@click.command()
@click.option('--target', '-t', type=click.Path(exists=True))
@click.option('--x', '-x', type=int)
@click.option('--y', '-y', type=int)
@click.option('--width', '-w', type=int)
@click.option('--height', '-h', type=int)
@click.option('--output', '-o')
def cmd(target, x, y, width, height, output):
    img = Image.open(target)
    cropped = img.crop((x, y, width, height))
    cropped.save(output, 'PNG')
