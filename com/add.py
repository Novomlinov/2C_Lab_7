#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add(students):
    name = input("Фамилия и инициалы ")
    post = input("Номер группы ")
    a = int(input("Русский язык "))
    b = int(input("Математика "))
    c = int(input("Информатика "))
    d = int(input("История "))
    e = int(input("Физика "))
    student = {
        'name': name,
        'post': post,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
    }
    students.append(student)
    if len(students) > 1:
        students.sort(key=lambda item: item.get('name', ''))