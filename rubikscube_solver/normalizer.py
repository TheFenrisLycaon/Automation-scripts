"""Normalizer module."""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import exit as Die

try:
    import json
except ImportError as err:
    Die(err)


class Normalizer:
    """Normalizer class."""

    def algorithm(self, alg, language):
        """Normalize an algorithm from the json-written manual.

        :param alg: The algorithm itself
        :returns: list
        """
        with open("solve-manual.json") as f:
            manual = json.load(f)

        solution = []
        for notation in alg.split(" "):
            solution.append(manual[language][notation])
        return solution


normalize = Normalizer()
