#!/usr/bin/env python3

import csv
import jinja2
import argparse
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class IndexItem:
    book_number: int
    chapter_number: int
    page_number: str
    keyword: str
    description: str

    colors = [
        'DarkOrange',
        'HotPink',
        'MediumSeaGreen',
        'Gold',
        'SteelBlue',
        'MediumPurple'
    ]

    @property
    def color(self):
        return self.colors[int(self.book_number)-1]

    def __lt__(self, other):
        return self.keyword.upper() < other.keyword.upper()

    def __gt__ (self, other):
        return self.keyword.upper() > other.keyword.upper()

TEMPLATE_FILE = "template.html"
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader, autoescape=True)
template = template_env.get_template(TEMPLATE_FILE)


parser = argparse.ArgumentParser(description='Creates your GIAC Index')
parser.add_argument('file', metavar='file', help='a CSV file')
parser.add_argument('--skip-header', default=False, action=argparse.BooleanOptionalAction, help='ignore CSV header column')
args = parser.parse_args()

index_dict = defaultdict(list)
with open(args.file, newline='') as csvfile:
    index_reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
    if(args.skip_header):
        next(index_reader)

    index_items = [IndexItem(*row) for row in index_reader]
    for item in index_items:
        section_key = item.keyword[0].upper()
        index_dict[section_key].append(item)

sorted_index_dict = {k: sorted(v) for k, v in sorted(index_dict.items(), key=lambda k_v: k_v) }
rendered_template = template.render(index = sorted_index_dict)
print(rendered_template)