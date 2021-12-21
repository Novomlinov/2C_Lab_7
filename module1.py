#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def first(tag):
    def second(s):
        group = tag, s
        return group

    return second