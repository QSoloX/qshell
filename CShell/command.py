#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Command:
    '''The command object'''

    def __init__(self, name, help_message, usage, func):
        self.name = name
        self.help_message = help_message
        self.usage = usage
        self.func = func


def register(name, help_message, usage, commands):
    '''Used to register different commands'''
    def inner(func):
        command = Command(name, help_message, usage, func)
        commands[name] = command

    return inner
