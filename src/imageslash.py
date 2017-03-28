# coding: UTF-8

import click
from PIL import Image


@click.command()
@click.option('--target', '-t', type=click.Path(exists=True))
@click.option('--left', '-l', type=int)
@click.option('--top', '-t', type=int)
@click.option('--right', '-r', type=int)
@click.option('--bottom', '-b', type=int)
@click.option('--output', '-o')
def cmd(target, left, top, right, bottom, output):
    img = Image.open(target)
    cropped = img.crop((left, top, right, bottom))
    cropped.save(output, 'PNG')
