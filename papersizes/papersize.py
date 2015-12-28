# -*- coding: utf-8 -*-
"""
Page sizes and various mechanisms for manipulating them.
"""
import math
import collections
from .units import mm, inch

# ----------------------------------------------------------------------------
# Page size tuple.
# ----------------------------------------------------------------------------

class PaperSize(collections.namedtuple('PaperSize', 'width height')):
    """The size of a piece of paper.

    This class inherits from a named tuple and has an empty ``__slots__``
    property, so it is immutable and inextensible. It is used, rather
    than a raw (width, height) tuple, to allow additonal methods to
    be defined."""
    __slots__ = ()

    @classmethod
    def from_mm(Class, width_in_mm, height_in_mm):
        """Convert from width and height in mm into standard pts."""
        return Class(width_in_mm*mm, height_in_mm*mm)

    @classmethod
    def from_inch(Class, width_in_inch, height_in_inch):
        """Convert from width and height in inches into standard pts."""
        return Class(width_in_inch*inch, height_in_inch*inch)

    @classmethod
    def from_ratio(Class, width=None, height=None, ratio=1.0):
        """Create a new paper size from the given ratio and one dimension.

        Arguments:

        ``ratio``
            The ratio of the height to the width of the resulting page. So
            a ratio of 1.5 (i.e. 3:2) will be 1.5x as tall as it is wide.
            Note that the ``ratio`` property returns
            the ratio of long to short
            side, not height to width. For the same ratio, therefore, this
            function will generate a paper in portrait orientation. The
            ``papersizes.ratios`` module provides a series of common
            ratios.
        """
        if width is None:
            if height is None:
                raise ValueError('width or height must be given')
            else:
                return Class(height / ratio, width)
        else:
            if height is None:
                return Class(width, height * ratio)
            else:
                raise ValueError('only one of width or height may be given')

    @property
    def area_in_sq_pts(self):
        """The area of this paper."""
        return self.width * self.height

    @property
    def ratio(self):
        """The ratio of long to short side."""
        if self.width > self.height:
            return self.width / self.height
        else:
            return self.height / self.width

    def landscape(self):
        """Return a version of this paper size in landscape orientation."""
        if self.width >= self.height:
            return self
        else:
            return self.flip()

    def portrait(self):
        """Return a version of this paper size in portrait orientation."""
        if self.width <= self.height:
            return self
        else:
            return self.flip()

    def flip(self):
        """Return a version of this paper size with dimensions reversed."""
        return PaperSize(self.height, self.width)

    def half(self):
        """Paper half the size of this, cut parallel to the short edge.

        If the original paper is portrait, the returned paper will be also,
        and vice versa.
        """
        if self.height < self.width:
            if self.height > self.width / 2:
                return PaperSize(self.height, self.width / 2)
            else:
                return PaperSize(self.width / 2, self.height)
        else:
            if self.width > self.height / 2:
                return PaperSize(self.height / 2, self.width)
            else:
                return PaperSize(self.width, self.height / 2)

    def small_square(self):
        """Return a square paper size using the smaller dimension."""
        if self.height < self.width:
            return PaperSize(self.height, self.height)
        elif self.height == self.width:
            return self
        else:
            return PaperSize(self.width, self.width)

    def large_square(self):
        """Return a square paper size using the larger dimension."""
        if self.height > self.width:
            return PaperSize(self.height, self.height)
        elif self.height == self.width:
            return self
        else:
            return PaperSize(self.width, self.width)

    def round_to_mm(self):
        """Return a paper size with dimensions rounded to the nearest mm."""
        return PaperSize(round(self.width / mm)*mm, round(self.height / mm)*mm)

    def is_landscape(self):
        """Check if this paper is landscape oriented.

        Square paper is neither landscape or portrait."""
        return self.width > self.height

    def is_portrait(self):
        """Check if this paper is portrait oriented.

        Square paper is neither landscape or portrait."""
        return self.width < self.height

    def is_square(self):
        """Check if this paper is square."""
        return self.width == self.height

    def is_approximately(self, other, tolerance=0.1*mm):
        """Check if the given paper size is roughly the same as this one.

        Arguments:

        ``other``
            The paper size to compare against. This can be given as any
            (width, height) tuple, it doesn't have to be a ``PaperSize``
            instance.
        """
        return abs(self.width - other[0]) <= tolerance and \
            abs(self.height - other[1]) <= tolerance

    def add_bleed(self, bleed):
        """Return a paper size with the given bleed added.

        Standard bleeds are 3mm internationally and 1/8" US. Large images and
        die cuts have a larger bleed."""
        if bleed != 0.0:
            return PaperSize(self.width + bleed*2.0, self.height + bleed*2.0)
        else:
            return self

    def as_pt_str(self):
        """Printable description of the size, to the nearest point."""
        return '{0:.0f}x{1:.0f}pt'.format(self.width, self.height)

    def as_mm_str(self):
        """Printable description of the size, to the nearest mm."""
        return '{0:.0f}x{1:.0f}mm'.format(self.width / mm, self.height / mm)

    def as_inch_str(self, unit='"'):
        """Printable description of the size, to the nearest ⅛ of an inch."""
        EIGHTHS = ('', '⅛', '¼', '⅜', '½', '⅝', '¾', '⅞')
        def _to_eight(val):
            val /= inch
            whole = math.floor(val)
            eighth = round(val * 8) % 8
            return '{0:.0f}{1}'.format(whole, EIGHTHS[eighth])
        return '{0}x{1}{2}'.format(
            _to_eight(self.width), _to_eight(self.height), unit)

    def __repr__(self):
        return 'PaperSize({0:f}, {1:f})'.format(self.width, self.height)

    def __str__(self):
        return '{0} ({1}, {2})'.format(
                self.as_pt_str(), self.as_mm_str(), self.as_inch_str())

# ----------------------------------------------------------------------------
# Page size generator.
# ----------------------------------------------------------------------------

class ISO269Series(object):
    """
    A set of paper sizes conforming to ISO 269.

    ISO 269 specifies tolerances of at least 1mm in page sizes and
    these are often used to make sure that each page size is an
    integer number of mm in each direction. So A4 is of width 210mm,
    although A0 is 841mm wide. This breaks the normal halving rule,
    but is a widespread standard.

    Instances of this class can be used to retrieve paper sizes by
    using subscript notation: ``A[5]``, for example. There is no limit
    to the large (lower numbered) sizes that can be calculated in this
    way, but because this class always rounds to the nearest millimeter,
    very small paper sizes (high numbered) will be meaningless.

    Paper sizes returned by this class are portrait oriented.

    Arguments:

    ``initial_size``
        The 'reference' paper size for this series. This is usually a
        large size, most commonly the 0-size. This can be given as any
        (width, height) tuple, it doesn't have to be a ``PaperSize``
        instance.

    ``initial_number``
        The size number of the initial paper size given in the first
        argument.
    """
    def __init__(self, initial_size, initial_number=0):
        # We might be given a plain tuple, so don't use PaperSize.portrait
        if initial_size[0] > initial_size[1]:
            initial_size = initial_size[1], initial_size[0]
        # Store the size internally in mm, so we can do the simplification.
        initial_in_mm = round(initial_size[0] / mm), round(initial_size[1] / mm)
        self.cache = {initial_number:initial_in_mm}
        self.min_cached = initial_number
        self.max_cached = initial_number
        self.initial_size = initial_size
        self.initial_number = initial_number

    def __repr__(self):
        return "ISO 269 Series, {0} at size {1}".format(
            repr(self.initial_size),
            repr(self.initial_number))

    def __getitem__(self, size):
        if size not in self.cache:
            if size > self.max_cached:
                # We're smaller than the last value cached.
                last = self.cache[self.max_cached]
                for s in range(self.max_cached+1, size+1):
                    next = last[1] // 2, last[0]
                    self.cache[s] = next
                    last = next
                self.max_cached = size
            else:
                # We're larger than the initial.
                last = self.cache[self.min_cached]
                for s in range(self.min_cached-1, size-1, -1):
                    next = last[1], last[0] * 2
                    self.cache[s] = next
                    last = next
                self.min_cached = size

        # Cached data is in mm, so convert to pts.
        return PaperSize.from_mm(*self.cache[size])