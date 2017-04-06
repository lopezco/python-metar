import unittest
from metar.Datatypes import Temperature, UnitsError


class TemperatureTest(unittest.TestCase):
    def testDefaults(self):
        self.assertEqual(Temperature("32").value(), 32.0)
        self.assertEqual(Temperature("32").value("C"), 32.0)
        self.assertEqual(Temperature("32").string(), "32.0 C")
        self.assertEqual(Temperature("32", "F").string(), "32.0 F")

    def testInputs(self):
        self.assertEqual(Temperature("32").value(), 32.0)
        self.assertEqual(Temperature(32).value(), 32.0)
        self.assertEqual(Temperature(32.0).value(), 32.0)

        self.assertEqual(Temperature("32", "c").value(), 32.0)
        self.assertEqual(Temperature("32", "f").value(), 32.0)
        self.assertEqual(Temperature("32", "k").value(), 32.0)

        self.assertEqual(Temperature("50", "F").value("c"), 10.0)
        self.assertEqual(Temperature("50", "f").value("C"), 10.0)

    def testErrorChecking(self):
        self.assertRaises(ValueError, Temperature, "32C")
        self.assertRaises(ValueError, Temperature, "M10F")
        self.assertRaises(UnitsError, Temperature, "32", "J")
        self.assertRaises(UnitsError, Temperature("32").value, "J")
        self.assertRaises(UnitsError, Temperature("32").string, "J")

    def testConversions(self):
        self.assertEqual(Temperature("32", "F").value("F"), 32.0)
        self.assertEqual(Temperature("32", "F").value("C"), 0.0)
        self.assertEqual(Temperature("50", "F").value("C"), 10.0)
        self.assertEqual(Temperature("32", "F").value("K"), 273.15)

        self.assertEqual(Temperature("20", "C").value("C"), 20.0)
        self.assertEqual(Temperature("M10", "C").value("F"), 14.0)
        self.assertEqual(Temperature("M0", "C").value("F"), 32.0)
        self.assertEqual(Temperature("20", "C").value("K"), 293.15)
        self.assertEqual(Temperature("20", "C").value("F"), 68.0)
        self.assertEqual(Temperature("30", "C").value("F"), 86.0)

        self.assertEqual(Temperature("263.15", "K").value("K"), 263.15)
        self.assertEqual(Temperature("263.15", "K").value("C"), -10.0)
        self.assertEqual(Temperature("263.15", "K").value("F"), 14.0)

        self.assertEqual(Temperature("10", "C").string("C"), "10.0 C")
        self.assertEqual(Temperature("10", "C").string("F"), "50.0 F")
        self.assertEqual(Temperature("10", "C").string("K"), "283.1 K")


if __name__ == '__main__':
    unittest.main()
