from qshell import Shell, register


# A basic Calculator class
class Calculator:
    '''The Calculator Object'''
    def __init__(self):
        self.memory = []

    def update_memory(self, new_value):
        self.memory.append(new_value)

    def add(self, num_one, num_two):
        return int(num_one) + int(num_two)

    def subtract(self, num_one, num_two):
        return int(num_one) - int(num_two)


# Define the shell commands
commands = {}

# These commands use the calc object


@register('add', "Add two numbers together", "Usage: add num_one num_two",
          commands)
def command_add(shell, user_in):
    output = shell.object.add(user_in[1], user_in[2])
    shell.object.update_memory(output)
    return output


@register('sub', "Subtract two numbers together", "Usage: sub num_one num_two",
          commands)
def command_sub(shell, user_in):
    output = shell.object.subtract(user_in[1], user_in[2])
    shell.object.update_memory(output)
    return output


@register('memory', "Get the output memory", "Usage: memory", commands)
def command_memory(shell, user_in):
    return shell.object.memory


# The main function that runs the shell loop
def main():
    # create our calc object
    calc = Calculator()

    # Create the shell, with the commands dict, a name, the calc object, and clear_on_start
    shell = Shell(commands,
                  name="Calculator",
                  ext_object=calc,
                  clear_on_start=True)

    # Start the shell
    shell.run()


if __name__ == '__main__':
    main()
