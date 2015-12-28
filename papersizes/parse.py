# -*- coding: utf-8 -*-
"""Parsing for dimensions and paper sizes."""

from . import units
from . import papersizes
from . import papersize

def dimension(size_string):
    """Parses a numeric dimension, returning a size in points."""
    size_string, unit = __extract_unit(size_string)
    return __parse_number(size_string) * unit

def paper_size(size_string):
    """Parses a paper size string, either a name or a pair of dimensions."""
    # Check for a modification.
    normalised_string = __normalise_size_name(size_string)
    if normalised_string.endswith(' landscape'):
        modification = papersize.PaperSize.landscape
        normalised_string = normalised_string[:-10].strip()
    elif normalised_string.endswith(' portrait'):
        modification = papersize.PaperSize.portrait
        normalised_string = normalised_string[:-9].strip()
    else:
        modification = None

    # Try to get the papersize by name.
    size = __parse_paper_size_by_name(normalised_string)
    if size is None:
        # Otherwise interpret it as dimensions, separated by an x.
        width_string, height_string = normalised_string.split('x', 2)
        width_string, width_unit = __extract_unit(width_string, None)
        height_string, height_unit = __extract_unit(height_string, units.pt)
        width = __parse_number(width_string)
        height = __parse_number(height_string) * height_unit
        if width_unit is None:
            width *= height_unit
        else:
            width *= width_unit
        size = papersize.PaperSize(width, height)

    if modification is not None:
        size = modification(size)

    return size

# -----------------------------------------------------------------------
# Internals
# -----------------------------------------------------------------------

__size_units = (
    ('mm', units.mm),
    ('"', units.inch),
    ('in', units.inch),
    ('inch', units.inch),

    ('cm', units.cm),
    ('pt', units.pt),
    ('pts', units.pt),
    ('cms', units.cm),
    ('mms', units.mm),
    ('ins', units.inch),
    ('inches', units.inch),
    ('m', units.m),
    )
def __extract_unit(size_string, default_unit=units.pt):
    """Finds a unit at the end of the given string."""
    unit = default_unit

    size_string = size_string.strip()
    for suffix, unit_value in __size_units:
        if size_string.endswith(suffix):
            unit = unit_value
            size_string = size_string[:-len(suffix)]
            break

    return size_string, unit

__fractions = '⅛¼⅜½⅝¾⅞'
def __parse_number(number_as_string):
    """Parses the given number, which can also include fractions.

    An empty string parses to the value 1.0.
    """
    number_as_string = number_as_string.strip()
    number_as_string_len = len(number_as_string)
    if number_as_string_len == 0:
        return 1.0
    else:
        # Support fractions
        if number_as_string[-1] in __fractions:
            number = (__fractions.index(number_as_string[-1]) + 1) / 8
            if number_as_string_len > 1:
                number += float(number_as_string[:-1])
        else:
            number = float(number_as_string)
        return number

def __normalise_size_name(name):
    """Makes sure the name has the correct capitalisation and punctuation."""
    return name.lower().replace('_', ' ').replace('-', ' ')

__sizes_by_name = dict(
    (__normalise_size_name(name), getattr(papersizes, name))
    for name in dir(papersizes)
    if isinstance(getattr(papersizes, name), papersize.PaperSize))
def __parse_paper_size_by_name(size_string):
    """Parses a name of a paper size, returning the PaperSize object."""
    return __sizes_by_name.get(size_string, None)

