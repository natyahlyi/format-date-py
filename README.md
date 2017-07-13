# format-date-py
Converts "A/B/C" format date into the earliest possible legal date between Jan 1, 2000 and Dec 31, 2999

## Requirements
Python 3.*

Python packages:
* `Click` 

```
$ pip install -r requirements.txt
```

## Usage

```
$ python format.py --file <input_file> --output <output_file>
```
Input file example:

* ``` 
    3/02/01
    20/1/3
    3000/2/1
    1999/1/2
  ```
Will output file containing:
* ``` 
    3/02/01 >> 2001-02-03
    20/1/3 >> 2001-03-20
    3000/2/1 >> Invalid input
    1999/1/2 >> Invalid input
  ```
If you haven't specified output, it'll printed in terminal:
```
$ python format.py --file <input_file> 
```
Interactive mode:
```
$ python format.py --interactive
```