# -*- coding: utf-8 -*-
"""
A library of standard paper sizes from around the world.

Paper sizes defined in this module are portrait oriented unless
specifically noted.
"""
import sys
from .units import mm, inch
from .papersize import PaperSize, ISO269Series

def __build_iso_269_series(prefix, initial, start_number=0, end_number=10):
    """Creates a set of ISO 269 paper sizes in this module's globals.

    Calling this function for the A series will create module level
    constants for A0, A1 etc."""
    series = ISO269Series(initial, start_number)

    module = sys.modules[__name__]
    for i in range(start_number, end_number+1):
        setattr(module, "%s%d" % (prefix, i), series[i])

    return series

# ----------------------------------------------------------------------------
# CONSTANTS for specific paper sizes.
# ----------------------------------------------------------------------------

A = __build_iso_269_series('A', PaperSize(841*mm, 1189*mm))
"""The ISO 269 A-series of paper sizes.

These are used as the standard paper size in almost every country of
the world (the US being the most noteable exception).

There are module constants for A0 - A11 sizes, e.g. `papersizes.A4`.
"""

B = __build_iso_269_series('B', PaperSize(1000*mm, 1414*mm))
"""The ISO 269 B-series of paper sizes.

There are module constants for B0 - B11 sizes, e.g. `papersizes.B4`.
"""

C = __build_iso_269_series('C', PaperSize(917*mm, 1297*mm))
"""The ISO 269 C-series of sizes.

These are most commonly used as standard envelope sizes to fit unfolded
paper of the corresponding A-size. So C5 envelopes fit A5 paper, or A4
paper folded in half.

There are module constants for C0-C11 sizes, e.g. `papersizes.C5`.
"""

THIRD_A4 = PaperSize(A4[0], A4[1]/3.0)
"""The size of an A4 page folded in three on its long axis.

This is a common paper size in European businesses, where it acts as a
'compliment slip.

This is in landscape orientation."""

DL = PaperSize(220*mm, 100*mm)
"""The envelope size to fit a third of an A4 sheet.

Though it can be used for :data:`THIRD_A4` compliment slips, envelopes of
this size are more commonly used to hold an A4 sheet folded into three.
This and C5, are the most common envelope size for business communications
in Europe.

This is in landscape orientation.
"""

RA = __build_iso_269_series('RA', PaperSize(860*mm, 1220*mm), 0, 4)
"""A slightly oversized version of the ISO 269 A-series of papers.

This is most commonly used as a printer's paper size, where
the final paper will be cropped down to its corresponding A-series
size. It is not part of ISO 269, but follows the same page
proportions. Its sister-series :data:`SRA` is more common in
commercial printing. Sizes below ``RA4`` are not commonly seen.

There are module constants for RA0 - RA4 sizes, e.g. `papersizes.RA3`.
"""

SRA = __build_iso_269_series('SRA', PaperSize(900*mm, 1280*mm), 0, 4)
"""An oversized version of the ISO 269 A-series of papers.

These are used for full-bleed printing. ``SRA2`` is the most common bulk
paper size for commercial printing, although smaller full-bleed digital
presses use ``SRA3``. Sizes below ``SRA4`` are not commonly seen.

There are module constants for SRA0 - SRA4 sizes, e.g. `papersizes.SRA2`.
"""

A3_PLUS = PaperSize(329*mm, 483*mm)
"""A slightly oversized version of A4 paper.

This is used for full bleed printing on some inkjet printers."""


# Additional Japanese paper sizes
JIS_A = __build_iso_269_series('JIS_A', PaperSize(841*mm, 1189*mm))
"""The Japanese standard (JIS P 0138) A size papers.

Japan doesn't strictly use the ISO 269 page sizes, it has its own
national standard (JIS P 0138). The A-size paper in that standard,
however, conforms to the ISO A-size paper.

The two standards differ in their allowed tolerances (i.e. a paper
size that would 'pass' ISO 269 might not be valid JIS-A), but
the values used in this module for ISO 269 A-series, are within
the JIS-A tolerances. So for the purposes of this module, the two are
synonymous.

There are module constants for JIS_A0 - JIS_A11 sizes,
e.g. `papersizes.JIS_A4`.
"""

JIS_B = __build_iso_269_series('JIS_B', PaperSize(1030*mm, 1456*mm))
"""The Japanese standard (JIS P 0138) B size papers.

Japan has its own national standard B size paper (JIS P 0138) that
follows the ISO 269 page proportions, but has a different reference
size. This object represents that series. The Japanese B size is
slightly larger than its ISO cousin.

There are module constants for JIS_B0 - JIS_B11 sizes,
e.g. `papersizes.JIS_B4`.
"""

SHIROKU_BAN4 = PaperSize(264*mm, 379*mm)
"""The Japanese (JIS P 0138) Shiroku ban size 4, also known as 4x6/4.

Note that the SHIROKU-series don't use the ISO 269 paper proportions,
and so can't be halved to make the next size down."""

SHIROKU_BAN5 = PaperSize(189*mm, 262*mm)
"""The JIS P 0138 Shiroku ban size 5, also known as 4x6/5.

See also :data:`SHIROKU_BAN5_VARIANT`."""

SHIROKU_BAN5_VARIANT = PaperSize(191*mm, 259*mm)
"""A traditional Shiroku ban size 5 variant.

The standard size for Shiroku ban 5 is :data:`SHIROKU_BAN5`. This variant
arises when the paper is cut from a larger sheet. This ambiguity derives
from this paper as a historical paper size, with variations from one
paper-maker to the next. The variant size isn't part of JIS P 0138."""

SHIROKU_BAN6 = PaperSize(127*mm, 188*mm)
"""The JIS P 0138 Shiroku ban size 6, also known as 4x6/6."""


# Sweedish paper sizes
SIS_G5 = PaperSize(169*mm, 239*mm)
"""The Sweedish standard (SIS 014711) G5 paper.

Sweeden uses the ISO 269 paper sizes, but adds additional paper sizes in
its national standard SIS 014711. There are only two common sizes that
are not ISO 269 specified. This one and :data:`SIS_E5`."""

SIS_E5 = PaperSize(155*mm, 220*mm)
"""The Sweedish standard (SIS 014711) E5 paper.

Sweeden uses the ISO 269 paper sizes, but adds additional paper sizes in
its national standard SIS 014711. There are only two common sizes that
are not ISO 269 specified. This one and :data:`SIS_G5`."""


# Australian / Asian
F4 = PaperSize(210*mm, 330*mm)


# US Paper sizes
LETTER = PaperSize(8.5*inch, 11*inch)
"""The most common US paper size.

At one point variations of this paper size were used around the world,
now it is largely confined to the US and its immediate neighbours. It
is the size A in the US national standard ANSI Y 14.1, and is therefore
a synonym of :data:`ANSI_A`."""

LEGAL = PaperSize(8.5*inch, 14*inch)
"""A taller version of the US Letter paper size."""

TABLOID = PaperSize(11*inch, 17*inch)
"""The larger standard US paper size.

This is exactly the size of two :data:`LETTER` sheets. This is a
(more archaic) synonym for :data:`ELEVEN_BY_SEVENTEEN`, but should be
treated as deprecated, since ``TABLOID`` can refer to other sizes in
other contexts (in the printing of newspapers, for example). It also
matches the :data:`ANSI_B` US national standard paper size."""

ELEVEN_BY_SEVENTEEN = TABLOID
"""The larger standard US paper size.

This is exactly the size of two :data:`LETTER` sheets. This is a more
modern synonym for :data:`TABLOID`, and the :data:`ANSI_B` US national
standard paper size."""

LEDGER = PaperSize(17*inch, 11*inch) # landscape version of TABLOID
"""A standard size for old accounding ledgers.

This is the same paper size as the :data:`ELEVEN_BY_SEVENTEEN`, or
:data:`TABLOID` paper, but in landscape orientation."""

ANSI_A = LETTER
"""Size A in the US national standard ANSI Y 14.1.

This is a synonym for :data:`LETTER`. Note that this is a single
paper size, not a series of paper sizes, as per the ISO 269 A-sizes."""

ANSI_B = TABLOID
"""Size B in the US national standard ANSI Y 14.1.

This is a synonym for :data:`ELEVEN_BY_SEVENTEEN`, and :data:`TABLOID`.
Note that this is a single paper size, not a series of paper sizes, as
per the ISO 269 B-sizes."""

ANSI_C = PaperSize(17*inch, 22*inch)
"""Size C in the US national standard ANSI Y 14.1.

Note that this is a single paper size, not a series of paper sizes, as
per the ISO 269 C-sizes."""

ANSI_D = PaperSize(22*inch, 34*inch)
"""Size D in the US national standard ANSI Y 14.1."""

ANSI_E = PaperSize(34*inch, 44*inch)
"""Size E in the US national standard ANSI Y 14.1."""

# Architectural paper sizes.
ARCH_A = PaperSize(9*inch, 12*inch)
ARCH_B = PaperSize(12*inch, 18*inch)
ARCH_C = PaperSize(18*inch, 24*inch)
ARCH_D = PaperSize(24*inch, 36*inch)
ARCH_E = PaperSize(36*inch, 48*inch)
ARCH_E1 = PaperSize(30*inch, 42*inch)

# Personal organizer page sizes.
FILOFAX_MINI = PaperSize(2.625*inch, 4.25*inch)
FILOFAX_POCKET = PaperSize(3.25*inch, 4.75*inch, )
FILOFAX_PERSONAL = PaperSize(3.75*inch, 6.75*inch)
FILOFAX_SLIMLINE = PaperSize(3.75*inch, 6.75*inch)
FILOFAX_A5 = PaperSize(5.75*inch, 8.25*inch)
FRANKLIN_COVEY_POCKET = PaperSize(3.5*inch, 6*inch)
FRANKLIN_COVEY_COMPACT = PaperSize(4.25*inch, 6.75*inch)
FRANKLIN_COVEY_CLASSIC = PaperSize(5.5*inch, 8.5*inch)
ORGANIZER_J = PaperSize(2.75*inch, 5*inch)
ORGANIZER_K = TABLOID
ORGANIZER_L = PaperSize(5.5*inch, 8.5*inch)
ORGANIZER_M = LETTER

# Cards
INDEX_CARD_5X3 = PaperSize(5*inch, 3*inch) #: Landscape orientation
INDEX_CARD_6X4 = PaperSize(6*inch, 4*inch) #: Landscape orientation
INDEX_CARD_8X5 = PaperSize(8*inch, 5*inch) #: Landscape orientation
ISO_BUSINESS_CARD = PaperSize(52.98*mm, 85.60*mm)
US_BUSINESS_CARD = PaperSize(2*inch, 3.5*inch)
UK_BUSINESS_CARD = PaperSize(55*mm, 85*mm)
JAPANESE_BUSINESS_CARD = PaperSize(55*mm, 91*mm)
PLAYING_CARD_POKER = B8
PLAYING_CARD_BRIDGE = PaperSize(56*mm, 88*mm)
PLAYING_CARD = PLAYING_CARD_BRIDGE

# Craft paper sizes
INCHIE = PaperSize(1*inch, 1*inch)
ATC = PaperSize(2.5*inch, 3.5*inch)
SCRAPBOOK_6 = PaperSize(6*inch, 6*inch)
SCRAPBOOK_7 = PaperSize(7*inch, 7*inch)
SCRAPBOOK_8 = PaperSize(8*inch, 8*inch)
SMALL_SCRAPBOOK = SCRAPBOOK_8
LARGE_SCRAPBOOK = PaperSize(12*inch, 12*inch)
SCRAPBOOK = LARGE_SCRAPBOOK
MOO_CARD = PaperSize(28*mm, 70*mm)

# Newspaper sizes
BROADSHEET_NEWSPAPER = PaperSize(600*mm, 750*mm)
BERLINER_NEWSPAPER = PaperSize(315*mm, 470*mm)
MIDI_NEWSPAPER = BERLINER_NEWSPAPER
TABLOID_NEWSPAPER = PaperSize(280*mm, 430*mm)

# Other miscellaneous paper sizes
GOVERNMENT_LEGAL = PaperSize(8.0*inch, 10.5*inch)
JUNIOR_LEGAL = PaperSize(8.0*inch, 5.0*inch) #: Landscape orientation
COMPACT = PaperSize(4.25*inch, 6.75*inch)
MEMO = ORGANIZER_L
STATEMENT = MEMO
HALF_LETTER = MEMO
MONARCH = PaperSize(7.25*inch, 10.5*inch)
EXECUTIVE = MONARCH
FOLIO = PaperSize(8.27*inch, 13*inch)
FOOLSCAP = FOLIO
QUARTO = PaperSize(9*inch, 11*inch)
SUPER_B = PaperSize(13*inch, 19*inch)
POST = PaperSize(15.5*inch, 19.5*inch)
CROWN = PaperSize(15*inch, 20*inch)
LARGE_POST = PaperSize(16.5*inch, 21*inch)
DEMY = PaperSize(17.5*inch, 22.5*inch)
MEDIUM = PaperSize(18*inch, 23*inch)
BROADSHEET = PaperSize(18*inch, 24*inch)
ROYAL = PaperSize(20*inch, 25*inch)
ELEPHANT = PaperSize(23*inch, 28*inch)
DOUBLE_DEMY = PaperSize(22.5*inch, 35*inch)
QUAD_DEMY = PaperSize(35*inch, 45*inch)

# Book page sizes
A_FORMAT_PAPERBACK = PaperSize(110*mm, 178*mm)
B_FORMAT_PAPERBACK = PaperSize(130*mm, 198*mm)
C_FORMAT_PAPERBACK = PaperSize(135*mm, 216*mm)
TRADE_PAPERBACK = C_FORMAT_PAPERBACK

# Lulu Standard book sizes
LULU_US_TRADE_PAPERBACK = PaperSize(6*inch, 9*inch)
LULU_COMIC_BOOK = PaperSize(6.625*inch, 10.25*inch)
LULU_POCKET_BOOK = PaperSize(4.25*inch, 6.875*inch)
LULU_LANDSCAPE_BOOK = PaperSize(9*inch, 7*inch) #: Landscape orientation
LULU_SMALL_SQUARE_BOOK = PaperSize(7.5*inch, 7.5*inch)
LULU_ROYAL_BOOK = PaperSize(6.139*inch, 9.21*inch)
LULU_CROWN_QUARTO_BOOK = PaperSize(7.444*inch, 9.681*inch)
LULU_SQUARE_BOOK = PaperSize(8.5*inch, 8.5*inch)
