import unittest
from metar.Datatypes import Pressure, UnitsError


class PressureTest(unittest.TestCase):
    def testDefaults(self):
        self.assertEqual(Pressure("1000").value(), 1000.0)
        self.assertEqual(Pressure("1000", "HPA").value(), 1000.0)
        self.assertEqual(Pressure("30", "in").value(), 30.0)
        self.assertEqual(Pressure("30", "in").string(), "30.00 inches")
        self.assertEqual(Pressure("1000").value("MB"), 1000)
        self.assertEqual(Pressure("1000").string(), "1000.0 mb")
        self.assertEqual(Pressure("1000", "HPA").string(), "1000.0 hPa")

    def testInputs(self):
        self.assertEqual(Pressure("1000").value(), 1000.0)
        self.assertEqual(Pressure("1000.0").value(), 1000.0)
        self.assertEqual(Pressure(1000).value(), 1000.0)
        self.assertEqual(Pressure(1000.0).value(), 1000.0)

        self.assertEqual(Pressure("1000", "mb").value(), 1000.0)
        self.assertEqual(Pressure("1000", "hPa").value(), 1000.0)
        self.assertEqual(Pressure("30.00", "in").value(), 30.0)

        self.assertEqual(Pressure("1000", "MB").value("MB"), 1000.0)
        self.assertEqual(Pressure("1000", "MB").value("HPA"), 1000.0)
        self.assertEqual(Pressure("1000", "HPA").value("mb"), 1000.0)

    def testErrorChecking(self):
        self.assertRaises(ValueError, Pressure, "A2995")
        self.assertRaises(UnitsError, Pressure, "1000", "bars")
        self.assertRaises(UnitsError, Pressure("30.00").value, "psi")
        self.assertRaises(UnitsError, Pressure("32.00").string, "atm")

    def testConversions(self):
        self.assertEqual(Pressure("30", "in").value("in"), 30.0)
        self.assertAlmostEqual(Pressure("30", "in").value("mb"), 1015.92, 2)
        self.assertAlmostEqual(Pressure("30", "in").value("hPa"), 1015.92, 2)

        self.assertEqual(Pressure("30", "in").string("in"), "30.00 inches")
        self.assertEqual(Pressure("30", "in").string("mb"), "1015.9 mb")
        self.assertEqual(Pressure("30", "in").string("hPa"), "1015.9 hPa")

        self.assertEqual(Pressure("1000", "mb").value("mb"), 1000.0)
        self.assertEqual(Pressure("1000", "mb").value("hPa"), 1000.0)
        self.assertAlmostEqual(Pressure("1000", "mb").value("in"), 29.5299, 4)
        self.assertAlmostEqual(Pressure("1000", "hPa").value("in"), 29.5299, 4)


if __name__ == '__main__':
    unittest.main()
