# QShell (Quick Shell)

A simple python command shell, that allows you to wrap your program in a interactive shell environment.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CShell.

```bash
pip install qshell
```

## Docs

The docs will be available soon :)

## Example

The barbones example:

```python
from qshell import Shell, register

commands = {}

@register('echo', 'Echo a word back to the console', 'Usage: echo sometext', commands)
def command_echo(shell, user_in):
    print(" ".join(user_in[1:]))

def main():
    example = Shell(commands)
    example.run()


```

![](https://raw.githubusercontent.com/QSoloX/qshell/main/ext/basic_example.gif)

## ToDo

- Add Customizable Colors
- Create Documentation
- Better error handling

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
