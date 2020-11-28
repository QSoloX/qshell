#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform


class Shell():
    '''A basic command line shell implemented in python'''

    def __init__(self, command_dict, name="Shell", ext_object=None):
        self.history = []
        self.command_dict = command_dict
        self.object = ext_object
        self.name = name
        self.running = True
        self.user_os = platform.system().lower()

    def update_history(self, new_item):
        '''Used to update the command history'''
        self.history.append(new_item)

    def clear(self):
        '''Used to clear the console screen'''
        if self.user_os == 'linux':
            os.system('clear')
        elif self.user_os == 'windows':
            os.system('cls')

    def run(self):
        '''The main shell loop'''
        while self.running:
            try:
                print(f"{self.name} > ", end=" ")

                user_input = input().split(" ")

                if user_input[0] in self.command_dict:
                    self.command_dict[user_input[0]].func(self, user_input)
                    self.update_history(user_input)

            except KeyboardInterrupt:
                self.running = False
