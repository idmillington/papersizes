# Paper Sizes

This module attempts to solve one small problem: knowing how big pieces
of paper are for code that involves printing.

Install with

    % pip install papersizes

Then

    >>> import papersizes
    >>> make_document(papersizes.A4.landscape())

It has a large selection of paper sizes defined, and a `PaperSize` class
which is a wrapper around a `namedtuple` providing functionality to rotate
and modify sizes.