#!/usr/bin/env python3

import csv
import jinja2
from collections import OrderedDict, defaultdict
from dataclasses import dataclass

@dataclass
class IndexItem:
    book_number: int
    chapter_number: int
    page_number: str
    keyword: str
    description: str

    def __lt__(self, other):
        return self.keyword.upper() < other.keyword.upper()

    def __gt__ (self, other):
        return self.keyword.upper() > other.keyword.upper()

TEMPLATE_FILE = "template.html"

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader, autoescape=True)

template = template_env.get_template(TEMPLATE_FILE)

index_dict = defaultdict(list)
with open('sec542.csv', newline='') as csvfile:
    index_reader = csv.reader(csvfile, delimiter=',', quotechar="\"")
    index_items = [IndexItem(*row) for row in index_reader]
    for item in index_items:
        section_key = item.keyword[0].upper()
        index_dict[section_key].append(item)

sorted_index_dict = {k: sorted(v) for k, v in sorted(index_dict.items(), key=lambda k_v: k_v) }
rendered_template = template.render(index = sorted_index_dict)
print(rendered_template)