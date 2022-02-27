# yaGIACgen

A GIAC index generator that just works ...

## Build Index

### 1. Learn and accumulate your Knowledge Base 

* While studying create your index with MS Excel or LibreOffice Calc
* The columns in your worksheet should be book number, chapter number, page(-range), keyword, description/notes
  * The index generator expects the book and chapter number be representable as number whereas the rest can be string like objects
* You don't need to sort your worksheet beforehand
  
### 2. Export your Index as CSV

* Export your index as CSV file
  * Make sure you have 5 columns: book number, chapter number, page(-range), keyword, description/notes
  * Make sure you choose comma-separated entries
  * Use the `"` character as quote character


Example `myindex.csv`
```
1,4,7-15,keyword a,"a description"
2,5,3,keyword b,"a description"
``` 

### 3. Generate HTML

The generator will collect your entries group them alphabetically and sort them:


```bash
./generator.py <name>.csv > index.html
./generator.py <name>.csv --skip-header > index.html
```

### 4. Print

* Open the document in Google-Chrome and select the action `print` in the settings menu
* Choose `Save as PDF` as destination
* Then under the `more settings` deselect the option `Header and footers`
* Finally, click `save`

## TODOs

* Allow to define book colors
* Toggle for CSV header
* Indent when first word is the same?
