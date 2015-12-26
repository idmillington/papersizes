# -*- coding: utf-8 -*-
"""
Page height to width ratios for common page types.
"""

FOUR_THIRDS = 4.0 / 3.0
"""A ratio of 4:3.

It was common for papers to be in the 4:3 ratio, also known as the
Quarto ratio, because the pages of quarto books were roughly in this
proportion.

Use with the :meth:`~papersizes.papersize.PaperSize.from_ratio` method.
"""

TWO_THIRDS = 1.5
"""A ratio of 2:3.

Octavo books are half quarto size, and therefore are roughly in the
2:3 proportion.

Use with the :meth:`~papersizes.papersize.PaperSize.from_ratio` method.
"""

ISO_RATIO = 1.4142135623730951 #: sqrt(2) : ISO 269 sizes.
"""The ratio of height to width for ISO-269 paper.

It is the ratio such that, if the paper is cut into two equal sheets,
with the cutparallel to the short side, the two resulting sheets will
be the same ratio.

Use with the :meth:`~papersizes.papersize.PaperSize.from_ratio` method.
"""

GOLDEN_RATIO = 1.6180339887498949 # (1 + sqrt(5)) / 2
"""A ratio considered to be intrinsically beautiful.

This ratio, sometimes known by the greek letter phi, has been identified
in classical architecture and composition. It is the ratio such that,
if the paper is cut to remove a square of the short size, the remaining
portion will be in this same ratio. It is equal to (1+sqrt(5)) / 2.

Use with the :meth:`~papersizes.papersize.PaperSize.from_ratio` method.
"""

PENTAGON_RATIO = 1.5388417685876266 # Ratio of base to height of a pentagon.
"""A ratio considered to be beautiful.

It is the ratio of one side of a regular pentagon to its opposite vertex.

Use with the :meth:`~papersizes.papersize.PaperSize.from_ratio` method.
"""

