import unittest
from metar.Datatypes import Direction


def suite():
    return unittest.makeSuite(DirectionTest)


class DirectionTest(unittest.TestCase):
    def testUsage(self):
        self.assertEqual(Direction("90").value(), 90.0)
        self.assertEqual(Direction(90).value(), 90.0)
        self.assertEqual(Direction(90.0).value(), 90.0)
        self.assertEqual(Direction("90").string(), "90 degrees")
        self.assertEqual(Direction("E").compass(), "E")

    def testErrorChecking(self):
        self.assertRaises(ValueError, Direction, "North")
        self.assertRaises(ValueError, Direction, -10)
        self.assertRaises(ValueError, Direction, "361")

    def testConversion(self):
        self.assertEqual(Direction("N").value(), 0.0)
        self.assertEqual(Direction("NNE").value(), 22.5)
        self.assertEqual(Direction("NE").value(), 45.0)
        self.assertEqual(Direction("ENE").value(), 67.5)
        self.assertEqual(Direction("E").value(), 90.0)
        self.assertEqual(Direction("ESE").value(), 112.5)
        self.assertEqual(Direction("SE").value(), 135.0)
        self.assertEqual(Direction("SSE").value(), 157.5)
        self.assertEqual(Direction("S").value(), 180.0)
        self.assertEqual(Direction("SSW").value(), 202.5)
        self.assertEqual(Direction("SW").value(), 225.0)
        self.assertEqual(Direction("WSW").value(), 247.5)
        self.assertEqual(Direction("W").value(), 270.0)
        self.assertEqual(Direction("WNW").value(), 292.5)
        self.assertEqual(Direction("NW").value(), 315.0)
        self.assertEqual(Direction("NNW").value(), 337.5)

        self.assertEqual(Direction("0").compass(), "N")
        self.assertEqual(Direction("5").compass(), "N")
        self.assertEqual(Direction("355").compass(), "N")
        self.assertEqual(Direction("20").compass(), "NNE")
        self.assertEqual(Direction("60").compass(), "ENE")
        self.assertEqual(Direction("247.5").compass(), "WSW")


if __name__ == '__main__':
    unittest.main()
