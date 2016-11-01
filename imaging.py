__author__ = 'ericsage'

import sys
import logging
import argparse

from imagingd.src.imager import render_from_json

def create_parser():
    logging.info("Creating parser")
    parser = argparse.ArgumentParser(description='Convert CX into an image format.')
    p.add_argument('-f', '--font-size', type=int, default=18, help= "the desired font size for text in the image")
    p.add_argument('-d', '--image-dimensions', type=tuple, default=(200, 200), help="a tuple representing the desired dimensions of the image"
    p.add_argument('-t', '--image-format', default="png", choices=['png'], help="the output image format")
    p.add_argument('cx_json', type=open, help="the cx documented to be converted to an image")

def main():
    """Accepts a single input, CX as a string, and outputs CX as a string"""
    logging.basicConfig(level=logging.INFO)
    parser = create_parser()
    args = parser.parse_args()
    logging.info('Starting image generator')
    render_from_json(args.cx_json)
