# Split iterm panes by user defined structure

> TODO - publish to pypi, until published, use `python3 main.py` instead of `iterm-pane-spliter`

Split iterm panes by user defined structure from the command line.

## Usage
```bash
pip3 install -r requirements.txt
python3 main.py <json-structure>
```

the structure is a json Matrix, where each value is a different pane, the number of panes is the number of different values in the matrix.

the more values of the same number in the matrix, the bigger the pane will be.

## Examples

### 2 panes vertically split
For this:
```
-------------------
|        |        |
|        |        |
|   1    |    2   |
|        |        |
|        |        |
-------------------
```

the json structure you should provide is:
> Tip: just add more numbers to add more vertical panes
```json
[
  [1, 2]
]
```

so you will need to run:
```bash
iterm-pane-spliter "[[1, 2]]"
```

### 2 panes horizontally split
For this:
```
-------------------
|                 |
|       1         |
|                 |
-------------------
|                 |
|       2         |
|                 |
-------------------
```

the json structure you should provide is:
> Tip: just add more single value arrays to add more horizontal panes
```json
[
  [1],
  [2]
]
```

so you will need to run:
```bash
iterm-pane-spliter "[[1], [2]]"
```

### 2 panes vertically split 1 is bigger than 2
For this:
```
-------------------
|           |     |
|           |     |
|     1     |  2  |
|           |     |
|           |     |
-------------------
```

the json structure you should provide is:
```json
[
  [1, 1, 1, 2]
]
```

so you will need to run:
```bash
iterm-pane-spliter "[[1, 1, 1, 2]]"
```




### split to 4 equal panes
For this:
```
-------------------
|        |        |
|    1   |   2    |
|        |        |
-------------------
|        |        |
|    3   |   4    |
|        |        |
-------------------
```

the json structure you should provide is:
```json
[
  [1, 2],
  [3, 4]
]
```

so you will need to run:
```bash
iterm-pane-spliter "[[1, 2], [3, 4]]"
```


### Some crazy structure
```
-------------------
|     1     |     |
| --------- |  5  |
|     |     |     |
|     |  7  | --- |
|  2  |     |  3   |
|     | --- | --- |
|     |  8  |  6  |
| --- | --- | --- |
|        4        |
-------------------
```

the json structure you should provide is:
```json
[
    [1, 1, 5],
    [2, 7, 5],
    [2, 7, 3],
    [2, 8, 6],
    [4, 4, 4]
]
```

so you will need to run:
```bash
iterm-pane-spliter "[[1, 1, 5], [2, 7, 5], [2, 7, 3], [2, 8, 6], [4, 4, 4]]"
```



