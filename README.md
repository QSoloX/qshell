![Upload Python Package](https://github.com/QSoloX/qshell/workflows/Upload%20Python%20Package/badge.svg)

# QShell (Quick Shell)

A simple python command shell, that allows you to wrap your program in a interactive shell environment.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CShell.

```bash
pip install qshell
```

## Docs

The docs will be available soon :)
for now just check out the examples folder to see how its used!

## Example

The barbones example:

```python
from qshell import Shell, register

commands = {}

@register('echo', 'Echo a word back to the console', 'Usage: echo sometext', commands)
def command_echo(shell, user_in):
    return " ".join(user_in[1:])

def main():
    example = Shell(commands)
    example.run()


```

![](https://raw.githubusercontent.com/QSoloX/qshell/main/ext/basic_example.gif)

## ToDo

- Add environment variables
- Create Documentation
- Better error handling

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
