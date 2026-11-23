import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from math import pi
from random import randint

from project.circle import area as circle_area
from project.circle import perimeter as circle_perimeter
from project.rectangle import area as rectangle_area
from project.rectangle import perimeter as rectangle_perimeter
from project.square import area as square_area
from project.square import perimeter as square_perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        area = circle_area(0)
        self.assertEqual(area, 0)
        
    def test_one_radius_area(self):
        area = circle_area(1)
        self.assertAlmostEqual(area, pi, delta=0.00001)
        
    def test_pi_radius_area(self):
        area = circle_area(pi)
        self.assertAlmostEqual(area, pi*pi*pi, delta=0.00001)
        
    def test_float_radius_area(self):
        area = circle_area(2.5)
        self.assertAlmostEqual(area, 2.5*2.5*pi, delta=0.00001)
        
    def test_manyints_radius_area(self):
        for i in range (1, 1000):
            with self.subTest(i=i):
                area = circle_area(i)
                self.assertAlmostEqual(area, i*i*pi, delta=0.00001)
    
    def test_zero_radius_perimeter(self):
        perimeter = circle_perimeter(0)
        self.assertEqual(perimeter, 0)
            
    def test_one_radius_perimeter(self):
        perimeter = circle_perimeter(1)
        self.assertAlmostEqual(perimeter, 2*pi, delta=0.00001)
            
    def test_pi_radius_perimeter(self):
        perimeter = circle_perimeter(pi)
        self.assertAlmostEqual(perimeter, 2*pi*pi, delta=0.00001)
            
    def test_float_radius_perimeter(self):
        perimeter = circle_perimeter(2.5)
        self.assertAlmostEqual(perimeter, 2.5*pi*2, delta=0.00001)
            
    def test_manyints_radius_perimeter(self):
        for i in range (1, 1000):
            with self.subTest(i=i):
                perimeter = circle_perimeter(i)
                self.assertAlmostEqual(perimeter, 2*i*pi, delta=0.00001)
    
    
class RectangleTestCase(unittest.TestCase):
    def test_zero_sides_area(self):
        area = rectangle_area(0, 0)
        self.assertEqual(area, 0)
        
    def test_one_sides_area(self):
        area = rectangle_area(1, 1)
        self.assertEqual(area, 1)
        
    def test_equal_sides_area(self):
        for i in range (1, 1000):
            with self.subTest(side=i):
                area = rectangle_area(i, i)
                self.assertEqual(area, i*i)
        
    def test_float_sides_area(self):
        area = rectangle_area(2.5,2.5)
        self.assertAlmostEqual(area, 2.5*2.5, delta=0.00001)
        
    def test_manyints_area(self):
        for i in range (1, 1000):
            a = randint(1, 100000)
            b = randint(1, 100000)
            with self.subTest(sides=(a,b)):
                area = rectangle_area(a, b)
                self.assertEqual(area, a*b)
    
    
    def test_zero_sides_perimeter(self):
        perimeter = rectangle_perimeter(0, 0)
        self.assertEqual(perimeter, 0)
            
    def test_one_sides_perimeter(self):
        perimeter = rectangle_perimeter(1, 1)
        self.assertEqual(perimeter, 2*(1+1))
            
    def test_float_sides_perimeter(self):
        perimeter = rectangle_perimeter(2.5,2.5)
        self.assertAlmostEqual(perimeter, 2*(2.5+2.5), delta=0.00001)
            
    def test_equal_sides_perimeter(self):
        for i in range (1, 1000):
            with self.subTest(side=i):
                perimeter = rectangle_perimeter(i, i)
                self.assertEqual(perimeter, 2*(i+i))
                
    def test_manyints_perimeter(self):
            for i in range (1, 1000):
                a = randint(1, 100000)
                b = randint(1, 100000)
                with self.subTest(sides=(a,b)):
                    perimeter = rectangle_perimeter(a, b)
                    self.assertEqual(perimeter, 2*(a+b))
    
                
class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        area = square_area(0)
        self.assertEqual(area, 0)
        
    def test_one_side_area(self):
        area = square_area(1)
        self.assertEqual(area, 1)
        
    def test_equal_side_area(self):
        for i in range (1, 1000):
            with self.subTest(i=i):
                area = square_area(i)
                self.assertEqual(area, i*i)
        
    def test_float_side_area(self):
        area = square_area(2.5)
        self.assertAlmostEqual(area, 2.5*2.5, delta=0.00001)
        
    def test_manyints_area(self):
        for i in range (1, 1000):
            a = randint(1, 100000)
            with self.subTest(side=a):
                area = square_area(a)
                self.assertEqual(area, a*a)
    
    
    def test_zero_side_perimeter(self):
        area = square_perimeter(0)
        self.assertEqual(area, 0)
            
    def test_one_side_perimeter(self):
        area = square_perimeter(1)
        self.assertEqual(area, 4)
            
    def test_float_side_perimeter(self):
        area = square_perimeter(2.5)
        self.assertAlmostEqual(area, 4*2.5, delta=0.00001)
            
    def test_equal_side_perimeter(self):
        for i in range (1, 1000):
            with self.subTest(sides=i):
                area = square_perimeter(i)
                self.assertEqual(area, 4*i)
                
    def test_manyints_perimeter(self):
            for i in range (1, 1000):
                a = randint(1, 100000)
                with self.subTest(sides=a):
                    area = square_perimeter(a)
                    self.assertEqual(area, 4*a) 
                    
                    

if __name__ == "__main__":
    unittest.main(verbosity=2)
        