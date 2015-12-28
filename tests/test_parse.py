# -*- coding: utf-8 -*-
import unittest

from papersizes.units import *
from papersizes.parse import dimension, paper_size
from papersizes import papersizes

class TestParseDimension(unittest.TestCase):
	def test_mm(self):
		self.assertEqual(dimension('mm'), mm)
		self.assertEqual(dimension('mms'), mm)
		self.assertEqual(dimension('1mm'), mm)
		self.assertEqual(dimension('1.5mm'), 1.5 * mm)
		self.assertEqual(dimension('1.5 mm'), 1.5 * mm)

	def test_inch(self):
		self.assertEqual(dimension('in'), inch)
		self.assertEqual(dimension('"'), inch)
		self.assertEqual(dimension('inch'), inch)
		self.assertEqual(dimension('inches'), inch)
		self.assertEqual(dimension('1inch'), inch)
		self.assertEqual(dimension('1.5inch'), 1.5 * inch)
		self.assertEqual(dimension('1.5"'), 1.5 * inch)
		self.assertEqual(dimension('1.5ins'), 1.5 * inch)
		self.assertEqual(dimension('1.5 inches'), 1.5 * inch)
		self.assertEqual(dimension('1.5 inch'), 1.5 * inch)

	def test_fractional_value(self):
		self.assertEqual(dimension('⅛"'), 0.125 * inch)
		self.assertEqual(dimension('¼"'), 0.25 * inch)
		self.assertEqual(dimension('⅜"'), 0.375 * inch)
		self.assertEqual(dimension('½"'), 0.5 * inch)
		self.assertEqual(dimension('⅝"'), 0.625 * inch)
		self.assertEqual(dimension('¾"'), 0.75 * inch)
		self.assertEqual(dimension('⅞"'), 0.875 * inch)
		self.assertEqual(dimension('2½"'), 2.5 * inch)

	def test_cm_and_m(self):
		self.assertEqual(dimension('cm'), cm)
		self.assertEqual(dimension('m'), m)
		self.assertEqual(dimension('1cm'), cm)
		self.assertEqual(dimension('1.5cm'), 1.5 * cm)
		self.assertEqual(dimension('1.5 m'), 1.5 * m)

class TestParsePaperSize(unittest.TestCase):
	def test_aX(self):
		self.assertEqual(paper_size('a4'), papersizes.A4)
		self.assertEqual(paper_size('A2'), papersizes.A2)

	def test_aX_landscape(self):
		self.assertEqual(
			paper_size('a4 landscape'), papersizes.A4.landscape())
		self.assertEqual(
			paper_size('A2 LANDSCAPE'), papersizes.A2.landscape())

	def test_aX_portrait(self):
		self.assertEqual(
			paper_size('a4 portrait'), papersizes.A4.portrait())
		self.assertEqual(
			paper_size('a3-portrait'), papersizes.A3.portrait())
		self.assertEqual(
			paper_size('a1_portrait'), papersizes.A1.portrait())
		self.assertEqual(
			paper_size('A2 PORTRAIT'), papersizes.A2.portrait())

	def test_letter(self):
		self.assertEqual(paper_size('letter'), papersizes.LETTER)
		self.assertEqual(
			paper_size('LETTER landscape'), papersizes.LETTER.landscape())

	def test_given_size(self):
		self.assertEqual(paper_size('8.5x11"'), papersizes.LETTER)
		self.assertEqual(paper_size('8.5 x 11"'), papersizes.LETTER)
		self.assertEqual(
			paper_size('8.5 inch x 11 inch'), papersizes.LETTER)
		self.assertEqual(paper_size('210 x 297mm'), papersizes.A4)

	def test_given_size_different_units(self):
		self.assertEqual(paper_size('8.5" x 792pt'), papersizes.LETTER)
		self.assertEqual(paper_size('8.5 inch x 792'), papersizes.LETTER)

	def test_landscape_given_size(self):
		self.assertEqual(
			paper_size('8.5x11" landscape'),
			papersizes.LETTER.landscape())
