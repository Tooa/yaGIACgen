# yaGIACgen

A GIAC index generator that just works ...

## Build Index

The index generator expects the following CSV format:

```bash
# Format: book,chapter,page,keyword,description
# Quote character: "
# Example

1,1,1,keyword,"a description"
```

```bash
./generator.py <name>.csv > index.html
```

## Post Processing

## TODOs

* Allow to define book colors
* Toggle for CSV header
* Indent when first word is the same?
