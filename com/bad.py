#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bad(students):
    count = 0
    for student in students:
        if (student.get('a') == 2) or (student.get('b') == 2) or (student.get('c') == 2) \
                or (student.get('d') == 2) or (student.get('e') == 2):
            count += 1
            print('{:>4}: {}'.format(count, student.get('name', '')))
    if count == 0:
        print("Таких студентов не выявлено.")