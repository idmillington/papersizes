"""
Units and unit conversions used in the papersizes module.
"""

# ----------------------------------------------------------------------------
# Basic units in postscript points.
# ----------------------------------------------------------------------------

#: One International inch (defined as 25.4mm).
inch = 72.0

#: One ISO-standard millimeter.
mm = inch / 25.4

#: One ISO-standard centimeter.
cm = mm * 10.0

#: One ISO-standard meter.
m = mm * 1000.0

#: One postscript point.
pt = 1.0

# ----------------------------------------------------------------------------
# Unit conversions
# ----------------------------------------------------------------------------

def __create_conversions(*units):
    """Creates a set of conversion ratios for the given constants."""
    import sys
    module = sys.modules[__name__]
    for from_unit in units:
        from_unit_value = getattr(module, from_unit)
        for to_unit in units:
            if from_unit != to_unit:
                to_unit_value = getattr(module, to_unit)
                conversion = from_unit_value / to_unit_value
                setattr(module, "%s2%s" % (from_unit, to_unit), conversion)
__create_conversions("inch", "mm", "cm", "m", "pt")