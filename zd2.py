#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys
from com import add, list, bad, help


if __name__ == '__main__':
    students = []
    while True:
        command = input(">>> ").lower()
        if command == 'end':
            break
        elif command == 'add':
            add.add(students)
        elif command == 'list':
            list.list(students)
        elif command == 'bad':
            bad.bad(students)
        elif command == 'help':
            help.help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)