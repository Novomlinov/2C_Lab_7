#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list(students):
    for idx, student in enumerate(students, 1):
        print(
            '{:>7}: ФИО: {}, Номер группы: {}, Русский язык: {}, Математика: {}, Информатика: {}, История: {}, Физика: {};'.format(
                idx,
                student.get('name', ''), student.get('post', ''), student.get('a', 0),
                student.get('b', 0), student.get('c', 0),
                student.get('d', 0), student.get('e', 0)))