#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
from typing import Dict
from colorama import init, Fore


class Shell:
    """A basic command line shell implemented in python"""

    def __init__(
        self, command_dict, name="Shell", ext_object=None, clear_on_start=False, banner=None
    ):
        self.history = []
        self.command_dict = command_dict
        self.object = ext_object
        self.name = name
        self.running = True
        self.user_os = platform.system().lower()
        self.clear_on_start = clear_on_start

        # Shell Variables
        self.shell_variable = ""

        # Banner
        self.shell_banner = banner

        # Shell Colors
        self.colors = {
            "red": Fore.RED,
            "blue": Fore.BLUE,
            "cyan": Fore.CYAN,
            "black": Fore.BLACK,
            "green": Fore.GREEN,
        }

        # This init is for colorama
        init()
        self.set_colors()

    def set_colors(
        self, shell="blue", shell_var="red", output="red", input_color="green"
    ):
        """Allows to set all the colors, if not specified will use default"""
        self.shell_color = self.colors[shell]
        self.shell_var_color = self.colors[shell_var]
        self.output_color = self.colors[output]
        self.shell_input_color = self.colors[input_color]

    def update_var(self, new_var):
        """Updates the shell variable"""
        self.shell_variable = new_var

    def update_history(self, new_item):
        """Used to update the command history"""
        self.history.append(new_item)

    def clear(self):
        """Used to clear the console screen"""
        if self.user_os == "linux":
            os.system("clear")
        elif self.user_os == "windows":
            os.system("cls")

    def run(self):
        """The main shell loop"""

        if self.clear_on_start:
            self.clear()
        if self.shell_banner:
            print(f"{self.shell_banner}")
        while self.running:
            try:
                if self.shell_variable != "":
                    print(
                        f"{self.shell_color}{self.name} {self.shell_var_color}{self.shell_variable} {self.shell_color}>{self.shell_input_color}",
                        end=" ",
                    )
                else:
                    print(
                        f"{self.shell_color}{self.name} >{self.shell_input_color}",
                        end=" ",
                    )

                user_input = input().split(" ")

                if user_input[0] in self.command_dict:
                    self.update_history(user_input)
                    output = self.command_dict[user_input[0]].func(
                        self, user_input)
                    if type(output) == list:
                        for i in output:
                            print(
                                f"{self.output_color}{' '.join(i) if type(i) == list else ''.join(i)}")
                    elif type(output) == dict:
                        for key, value in output:
                            print(f"{self.output_color}{key}:{value}")
                    elif output == None:
                        continue
                    else:
                        print(f"{self.output_color}{output}")

            except KeyboardInterrupt:
                self.running = False
