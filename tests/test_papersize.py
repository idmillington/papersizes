# -*- coding: utf-8 -*-
import unittest

from papersizes.papersize import PaperSize
from papersizes.units import mm, inch

class PaperSizeTest(unittest.TestCase):
	def test_landscape(self):
		self.assertEqual(PaperSize(100, 200).landscape(), PaperSize(200, 100))
		self.assertEqual(PaperSize(200, 100).landscape(), PaperSize(200, 100))
		p = PaperSize(200, 200)
		self.assertEqual(p, p.landscape())

	def test_is_landscape(self):
		self.assertTrue(PaperSize(200, 100).is_landscape())
		self.assertFalse(PaperSize(100, 200).is_landscape())
		self.assertFalse(PaperSize(200, 200).is_landscape())

	def test_portrait(self):
		self.assertEqual(PaperSize(100, 200).portrait(), PaperSize(100, 200))
		self.assertEqual(PaperSize(200, 100).portrait(), PaperSize(100, 200))
		p = PaperSize(200, 200)
		self.assertEqual(p, p.portrait())

	def test_is_portrait(self):
		self.assertFalse(PaperSize(200, 100).is_portrait())
		self.assertTrue(PaperSize(100, 200).is_portrait())
		self.assertFalse(PaperSize(200, 200).is_portrait())

	def test_is_square(self):
		self.assertFalse(PaperSize(200, 100).is_square())
		self.assertFalse(PaperSize(100, 200).is_square())
		self.assertTrue(PaperSize(200, 200).is_square())

	def test_flip(self):
		self.assertEqual(PaperSize(100, 200).flip(), PaperSize(200, 100))
		self.assertEqual(PaperSize(200, 100).flip(), PaperSize(100, 200))
		p = PaperSize(200, 200)
		self.assertEqual(p, p.flip())

	def test_small_square(self):
		self.assertEqual(
			PaperSize(100, 200).small_square(), PaperSize(100, 100))
		self.assertEqual(
			PaperSize(200, 100).small_square(), PaperSize(100, 100))
		p = PaperSize(200, 200)
		self.assertEqual(p, p.small_square())

	def test_large_square(self):
		self.assertEqual(
			PaperSize(100, 200).large_square(), PaperSize(200, 200))
		self.assertEqual(
			PaperSize(200, 100).large_square(), PaperSize(200, 200))
		p = PaperSize(200, 200)
		self.assertEqual(p, p.large_square())

	def test_add_bleed(self):
		self.assertEqual(
			PaperSize(100, 200).add_bleed(10), PaperSize(120, 220))
		self.assertEqual(
			PaperSize(200, 100).add_bleed(10), PaperSize(220, 120))

	def test_half(self):
		self.assertEqual(PaperSize(100, 150).half(), PaperSize(75, 100))
		self.assertEqual(PaperSize(150, 100).half(), PaperSize(100, 75))
		self.assertEqual(PaperSize(100, 200).half(), PaperSize(100, 100))
		self.assertEqual(PaperSize(200, 100).half(), PaperSize(100, 100))
		self.assertEqual(PaperSize(100, 300).half(), PaperSize(100, 150))
		self.assertEqual(PaperSize(300, 100).half(), PaperSize(150, 100))

	def test_ratio(self):
		self.assertEqual(PaperSize(100, 150).ratio, 1.5)
		self.assertEqual(PaperSize(150, 100).ratio, 1.5)
		self.assertEqual(PaperSize(100, 100).ratio, 1)
		p = PaperSize(120.3, 143.2)
		self.assertEqual(p.portrait().ratio, p.landscape().ratio)

	def test_area_in_sq_pts(self):
		self.assertEqual(PaperSize(100, 150).area_in_sq_pts, 15000)
		self.assertEqual(PaperSize(150, 100).area_in_sq_pts, 15000)

	def test_as_mm_str(self):
		self.assertEqual(PaperSize(100*mm, 150*mm).as_mm_str(), '100x150mm')

	def test_from_mm(self):
		self.assertEqual(PaperSize.from_mm(100, 150), PaperSize(100*mm, 150*mm))

	def test_round_to_mm(self):
		self.assertEqual(
			PaperSize(210.4*mm, 296.9*mm).round_to_mm(),
			PaperSize.from_mm(210, 297))

	def test_as_inch_str(self):
		self.assertEqual(PaperSize(8*inch, 5*inch).as_inch_str(), '8x5"')
		self.assertEqual(PaperSize(8*inch, 5*inch).as_inch_str('in'), '8x5in')
		self.assertEqual(PaperSize(8.1*inch, 5.51*inch).as_inch_str(), '8⅛x5½"')

	def test_from_inch(self):
		self.assertEqual(
			PaperSize.from_inch(8.5, 11), PaperSize(8.5*inch, 11*inch))

	def test_as_pt_str(self):
		self.assertEqual(PaperSize(100, 150).as_pt_str(), '100x150pt')

	def test_repr(self):
		p1 = PaperSize(100, 150)
		p2 = eval(repr(p1))
		self.assertEqual(p1, p2)

	def test_str(self):
		self.assertEqual(
			str(PaperSize(8.125*inch, 5.5*inch)),
			'585x396pt (206x140mm, 8⅛x5½")')

