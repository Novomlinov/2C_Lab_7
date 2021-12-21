#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import module1


if __name__ == "__main__":
    module1.A = input("Введите тег ")
    module1.B = input("Введите содержимое строки ")
    print(module1.first(module1.A)(module1.B))