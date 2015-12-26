# -*- coding: utf-8 -*-
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

cm2inch = cm / inch
cm2m = cm / m
cm2mm = cm / mm
cm2pt = cm

inch2cm = inch / cm
inch2m = inch / m
inch2mm = inch / mm
inch2pt = inch

m2cm = m / cm
m2inch = m / inch
m2mm = m / mm
m2pt = m

mm2cm = mm / cm
mm2inch = mm / inch
mm2m = mm / m
mm2pt = mm

pt2cm = 1.0 / cm
pt2inch = 1.0 / inch
pt2m = 1.0 / m
pt2mm = 1.0 / mm
