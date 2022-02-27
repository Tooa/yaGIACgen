# yaGIACgen

A GIAC index generator that just works ...

## Build Index

### 1. Learn and accumulate your Knowledge Base 

* While studying create your index with MS Excel or LibreOffice Calc
* The columns in your worksheet should be book number, chapter number, page(-range), keyword, description/notes
  * The index generator expects the book and chapter number be representable as number, whereas the rest should be string like data types
* You don't need to sort your worksheet beforehand
  
### 2. Export your Index as CSV

* Export your index as CSV file
  * Make sure you have 5 columns: book number, chapter number, page(-range), keyword, description/notes
  * Make sure you choose comma-separated entries
  * Use the `"` character as quote character


Example `index.csv`
```
1,4,7-15,keyword a,"a description"
2,5,3,keyword b,"a description"
``` 

### 3. Generate HTML

The generator groups the rows by the first letter of the keyword and sorts each group alphabetically by its keyword as well.

The usage of the generator is as follows:
```bash
./generator.py -h
./generator.py <name>.csv > index.html
./generator.py <name>.csv --skip-header > index.html
```

You can further preserve the order of certain rows using a magic block (`[1-9]`) in your keyword column. The following input data
```
1,4,7-15,keyword [1] a,"a description"
2,5,3,keyword [2] c,"a description"
2,5,3,keyword [3] b,"a description"
```
will stay in order and the HTML result does **not** display the magic block.

### 4. Print

* Open the document in Google-Chrome and select the action `print` in the settings menu
* Choose `Save as PDF` as destination
* Then under the `more settings` deselect the option `Header and footers`
* Finally, click `save`

## Limitations

* The tool does not group together entries with the exact same keyword, but different pages,book/chapter numbers. Such occurrences will end-up as separate entries in the HTML file next to each other.

## TODOs

* Make book colors configurable
* Add toggle `--book-colors` to disable feature
* Indent when first word is the same?
