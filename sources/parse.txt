Parsing paper sizes (:mod:`papersizes.parse`)
=============================================

This module contains simple parsing methods suitable for use as the ``type``
argument in an argument definition in the ``argparse`` module.

.. code-block:: python

    import papersizes
    from papersizes import parse
    from papersizes.units import mm

    parser.add_argument(
        '-p', '--paper',
        type=parse.paper_size, default=papersizes.A4)
    parser.add_argument(
        '-m', '--margin',
        type=parse.dimension, default=5*mm)

Parsing of dimensions supports a number followed by a unit, for example:

.. code-block:: python

    dimension('3mm')
    dimension('12 inch')

with various synonyms for the units. To support inches, the parser also
copes with fractions.

.. code-block:: python

    dimension('3½"')

Paper sizes supports any of the defined sizes as text, case-insensitive,
with underscores in the variable names converted to spaces:

.. code-block:: python

    dimension('SRA2')

Width and height can also be given separated by ``'x'``, with units following
the second number (and following the first, optionally):

.. code-block:: python

    dimension('8½ x 11"')
    dimension('8½x11"')

Finally, any paper size, defined by name or dimensions, can be followed with
the strings ``' landscape'`` or ``' portrait'`` to change their orientaton.

.. code-block:: python

    dimension('A3 landscape')

Module Content
--------------

.. automodule:: papersizes.parse
    :members:
