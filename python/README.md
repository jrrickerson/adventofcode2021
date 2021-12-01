# Advent of Code 2021 - Python solutions

Python puzzle solutions are separated per day in `day-NN/` directories.  Shared code libraries used by multiple puzzle solutions will appear under the `lib/` directory.

## Python Solution Dependencies
A virtual environment is highly recommended to isolate depenencies.

Pipfile and Pipfile.lock are provided for use with [pipenv](https://pipenv.pypa.io/en/latest/)  
`requirements.txt` is provided for use with `pip`


## Makefile Usage
The Python solution directory makes use of `make` to automate setup, testing, and solution execution.  While not required to run the solutions, it makes my workflow more convenient.

### Environment variables / make parameters
**DAY**: Specify which day you want to work on, used by most targets   
Examples:
`$ make setup DAY=1`  
```
$ export DAY=1
$ make setup
$ make test
$ make solve
```
**URL**: Optional URL to display with the puzzle solution, used by the `setup` target

### Targets
- `setup`: Create a new directory and insert a boilerplate solution script for day `$DAY`
- `edit`: Edit the `$DAY` solution file using the tool specified by `$EDITOR`
- `solve`: Run the Python solution script for day `$DAY`
- `timer`: Run the Python solution script for day `$DAY` using `time`
- `test`: Run Python unit tests for day `$DAY` via `$TEST_RUNTIME`

### Example Workflow
```
$ export DAY=1
$ make setup
$ make edit
<...edit solution code...>
$ make test
$ make solve
```
