#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

import papersizes
from papersizes import mm, inch

def _near_enough(papersize, target, tolerance=0.25*mm):
	return abs(papersize[0] - target[0]) <= tolerance and \
		abs(papersize[1] - target[1]) <= tolerance

class TestASeries(unittest.TestCase):
	def test_a0(self):
		self.assertTrue(_near_enough(papersizes.A0, (841*mm, 1189*mm)))

	def test_a1(self):
		self.assertTrue(_near_enough(papersizes.A1, (594*mm, 841*mm)))

	def test_a2(self):
		self.assertTrue(_near_enough(papersizes.A2, (420*mm, 594*mm)))

	def test_a3(self):
		self.assertTrue(_near_enough(papersizes.A3, (297*mm, 420*mm)))

	def test_a4(self):
		self.assertTrue(_near_enough(papersizes.A4, (210*mm, 297*mm)))

	def test_a5(self):
		self.assertTrue(_near_enough(papersizes.A5, (148*mm, 210*mm)))

class TestBSeries(unittest.TestCase):
	def test_b0(self):
		self.assertTrue(_near_enough(papersizes.B0, (1000*mm, 1414*mm)))

	def test_b3(self):
		self.assertTrue(_near_enough(papersizes.B3, (353*mm, 500*mm)))

	def test_b4(self):
		self.assertTrue(_near_enough(papersizes.B4, (250*mm, 353*mm)))

	def test_b5(self):
		self.assertTrue(_near_enough(papersizes.B5, (176*mm, 250*mm)))

class TestCSeries(unittest.TestCase):
	def test_c4(self):
		self.assertTrue(_near_enough(papersizes.C4, (229*mm, 324*mm)))

	def test_c5(self):
		self.assertTrue(_near_enough(papersizes.C5, (162*mm, 229*mm)))

class TestUntrimmedSeries(unittest.TestCase):
	def test_ra0(self):
		self.assertTrue(_near_enough(papersizes.RA0, (860*mm, 1220*mm)))

	def test_ra1(self):
		self.assertTrue(_near_enough(papersizes.RA1, (610*mm, 860*mm)))

	def test_ra2(self):
		self.assertTrue(_near_enough(papersizes.RA2, (430*mm, 610*mm)))

	def test_ra3(self):
		self.assertTrue(_near_enough(papersizes.RA3, (305*mm, 430*mm)))

	def test_sra0(self):
		self.assertTrue(_near_enough(papersizes.SRA0, (900*mm, 1280*mm)))

	def test_sra1(self):
		self.assertTrue(_near_enough(papersizes.SRA1, (640*mm, 900*mm)))

	def test_sra2(self):
		self.assertTrue(_near_enough(papersizes.SRA2, (450*mm, 640*mm)))

	def test_sra3(self):
		self.assertTrue(_near_enough(papersizes.SRA3, (320*mm, 450*mm)))

class TestJISBSeries(unittest.TestCase):
	def test_jis_b0(self):
		self.assertTrue(_near_enough(papersizes.JIS_B0, (1030*mm, 1456*mm)))

	def test_jis_b3(self):
		self.assertTrue(_near_enough(papersizes.JIS_B3, (364*mm, 515*mm)))

	def test_jis_b4(self):
		self.assertTrue(_near_enough(papersizes.JIS_B4, (257*mm, 364*mm)))

	def test_jis_b5(self):
		self.assertTrue(_near_enough(papersizes.JIS_B5, (182*mm, 257*mm)))