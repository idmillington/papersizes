.. Papersizes documentation master file, created by
   sphinx-quickstart on Thu Feb 12 22:10:49 2015.

Papersizes
==========

Papersizes contains constants and methods representing the sizes of standard
papers around the world. It is intended to be used for any output rendering
/ printing or PDF generation task.

The main content is in the
:mod:`papersizes` module (i.e. the module has the same name as the whole
package). This list of paper sizes is imported when you import the package, e.g.

.. code-block:: python

    import papersizes
    make_document(papersizes.A4.landscape())


To access other facilities, such as the
:class:`~papersizes.papersize.PaperSize`
class, import one of the other modules directly, e.g.

.. code-block:: python

	from papersizes.papersize import PaperSize

This package uses postscript points (defined as 1/72 inch) as its standard
units, because this is the standard unit for PDF files. The
:mod:`~papersizes.units` module contains other units and conversions.



Contents:

.. toctree::
   :maxdepth: 2

   papersizes
   papersize
   ratios
   units

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

