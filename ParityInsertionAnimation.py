# ── locked · read-only boilerplate ──
# imports: manim, numpy (np), pandas (pd), scipy, sympy + stdlib listed below
# anything else is blocked — bespoke needs → contact your instructor
from manim import *
import numpy as np
import pandas as pd
import scipy
import sympy
import math, random, statistics, itertools, functools, collections
import datetime, decimal, fractions, re, string

class HammingCodeCondensed(Scene):
    def animate_step(self, bit, yellow=None, green=None, red=None, clear=None):
        
            if yellow:
                anims.extend([self.bitBoxes[i].animate.set_fill(YELLOW, opacity=1.0) for i in yellow])
            if green:
                anims.extend([self.bitBoxes[i].animate.set_fill(GREEN, opacity=1.0) for i in green])
            if red:
                anims.extend([self.bitBoxes[i].animate.set_fill(RED, opacity=1.0) for i in red])
            if clear:
                anims.extend([self.bitBoxes[i].animate.set_fill(RED, opacity=0.0) for i in clear])

            self.add(bit)
            self.wait(0.5)
            self.play(*anims)
    
    def construct(self):
        self.bitBoxes = VGroup(*[Square(side_length=1) for _ in range(16)])
        self.bitBoxes.arrange_in_grid()
        self.add(self.bitBoxes)

        bit = Text("1")
        bit.add()
        self.wait(1)
        self.play(bit.move_to(self.bitBoxes[0]).animate())

        self.animate_step(
            bit, 
            yellow=[1], 
            red=[3, 5, 7, 9, 11, 13, 15]
        )
        self.animate_step(
            bit, 
            green=[1], 
            clear=[3, 5, 7, 9, 11, 13, 15]
        )

        self.animate_step(
            bit, 
            yellow=[2], 
            green=[1], 
            red=[3, 6, 7, 10, 11, 14, 15]
        )
        self.animate_step(
            bit, 
            green=[1, 2], 
            clear=[3, 6, 7, 10, 11, 14, 15]
        )

        self.animate_step(
            bit, 
            yellow=[4], 
            green=[1, 2], 
            red=[5, 6, 7, 12, 13, 14, 15]
        )
        self.animate_step(
            bit, 
            green=[1, 2, 4], 
            clear=[5, 6, 7, 12, 13, 14, 15]
        )

        self.animate_step(
            bit, 
            yellow=[8], 
            green=[1, 2, 4], 
            red=[9, 10, 11, 12, 13, 14, 15]
        )
        self.animate_step(
            bit, 
            green=[1, 2, 4, 8], 
            red=[9, 10, 11, 12, 13, 14, 15]
        )

        self.animate_step(
            bit, 
            yellow=[0], 
            green=[1], 
            red=[2, 4, 6, 8, 10, 12, 14]
        )
        self.animate_step(
            bit, 
            green=[0, 1, 2, 4, 8], 
            clear=[6, 10, 12, 14]
        )
