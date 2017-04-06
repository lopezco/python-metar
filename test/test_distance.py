import unittest
from metar.Datatypes import Distance, UnitsError


class DistanceTest(unittest.TestCase):
    def testDefaults(self):
        self.assertEqual(Distance("10").value(), 10.0)
        self.assertEqual(Distance("1000").value("M"), 1000.0)
        self.assertEqual(Distance("1500").string(), "1500 meters")
        self.assertEqual(Distance("1500", None).string(), "1500 meters")
        self.assertEqual(Distance("5", "SM").string(), "5 miles")

    def testInputs(self):
        self.assertEqual(Distance("10").value(), 10.0)
        self.assertEqual(Distance(10).value(), 10.0)
        self.assertEqual(Distance(10.0).value(), 10.0)
        self.assertEqual(Distance(10.0, None).value(), 10.0)
        self.assertEqual(Distance("1/2").value(), 0.5)
        self.assertEqual(Distance("1 1/2").value(), 1.5)
        self.assertEqual(Distance("11/2").value(), 1.5)
        self.assertEqual(Distance("10", gtlt=">").value(), 10.0)
        self.assertEqual(Distance("10", None, "<").value(), 10.0)

    def testErrorChecking(self):
        self.assertRaises(ValueError, Distance, "10SM")
        self.assertRaises(ValueError, Distance, "M1/2SM")
        self.assertRaises(ValueError, Distance, "1000", "M", "=")
        self.assertRaises(ValueError, Distance, "1000", "M", "gt")
        self.assertRaises(UnitsError, Distance, "10", "NM")
        self.assertRaises(UnitsError, Distance("1000").value, "furlongs")
        self.assertRaises(UnitsError, Distance("500").string, "yards")

    def testConversions(self):
        self.assertEqual(Distance("5", "SM").value("SM"), 5.0)
        self.assertEqual(Distance("5", "SM").value("MI"), 5.0)
        self.assertAlmostEqual(Distance("5", "SM").value("M"), 8046.7, 1)
        self.assertAlmostEqual(Distance("5", "SM").value("KM"), 8.05, 2)
        self.assertAlmostEqual(Distance("5", "SM").value("FT"), 26400.0, 1)

        self.assertEqual(Distance("5000", "M").value("M"), 5000.0)
        self.assertEqual(Distance("5000", "M").value("KM"), 5.0)
        self.assertAlmostEqual(Distance("5000", "M").value("SM"), 3.1, 1)
        self.assertAlmostEqual(Distance("5000", "M").value("MI"), 3.1, 1)
        self.assertAlmostEqual(Distance("5000", "M").value("FT"), 16404.0, 0)

        self.assertEqual(Distance("5", "KM").value("KM"), 5.0)
        self.assertEqual(Distance("5", "KM").value("M"), 5000.0)
        self.assertAlmostEqual(Distance("5", "KM").value("SM"), 3.1, 1)
        self.assertAlmostEqual(Distance("5", "KM").value("FT"), 16404.0, 0)

        self.assertEqual(Distance("5280", "FT").value("FT"), 5280.0)
        self.assertAlmostEqual(Distance("5280", "FT").value("SM"), 1.0, 5)
        self.assertAlmostEqual(Distance("5280", "FT").value("MI"), 1.0, 5)
        self.assertAlmostEqual(Distance("5280", "FT").value("KM"), 1.609, 3)
        self.assertAlmostEqual(Distance("5280", "FT").value("M"), 1609, 0)

        self.assertAlmostEqual(Distance("1 1/2", "SM").value("FT"), 7920.0, 2)
        self.assertAlmostEqual(Distance("1/4", "SM").value("FT"), 1320.0, 2)

        self.assertEqual(Distance("1 1/2", "SM").string("SM"), "1 1/2 miles")
        self.assertEqual(Distance("3/16", "SM").string("SM"), "3/16 miles")
        self.assertEqual(Distance("1/4", "SM").string("FT"), "1320 feet")
        self.assertEqual(Distance("1/4", "SM", "<").string("SM"), "less than 1/4 miles")
        self.assertEqual(Distance("5280", "FT").string("KM"), "1.6 km")
        self.assertEqual(Distance("10000", "M", ">").string("M"), "greater than 10000 meters")


if __name__ == '__main__':
    unittest.main()
