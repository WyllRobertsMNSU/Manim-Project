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
HIGHLIGHT_TIME = 4
class HighlightAnimations():
    def animate_step(scene, orange=None, yellow=None, green=None, red=None, clear=None, potentialBits={}, opac=1, wait_time=0):
        anims = []

        if orange:
            anims.extend([scene.bit_boxes[i].animate.set_fill(ORANGE, opacity=opac) for i in orange])
        if yellow:
            anims.extend([scene.bit_boxes[i].animate.set_fill(YELLOW, opacity=opac) for i in yellow])
        if green:
            anims.extend([scene.bit_boxes[i].animate.set_fill(GREEN, opacity=opac) for i in green])
        if red:
            anims.extend([scene.bit_boxes[i].animate.set_fill(RED, opacity=opac) for i in red])
        if clear:
            clear = set(clear).difference(potentialBits)
            anims.extend([scene.bit_boxes[i].animate.set_fill(RED, opacity=0) for i in clear])

        #Keeps the potential bits highlighted yellow when clearing
        if potentialBits:
            anims.extend([scene.bit_boxes[i].animate.set_fill(YELLOW, opacity=opac) for i in potentialBits])
        scene.play(*anims)

        #Used for the parity bit calculation animation, sets the parity bit to the correct value
        if yellow and red:
            scene.wait(1.0)
            parity_value = sum(scene.grid_values[i] for i in red) % 2
            target_box_index = yellow[0]
            scene.grid_values[target_box_index] = parity_value

            parity_text = Text(str(parity_value), font_size=30, color=WHITE).move_to([5.5, 0, 0])
            scene.play(
                FadeIn(parity_text, run_time=0.2),
                parity_text.animate.move_to(scene.bit_boxes[target_box_index]),
                run_time=0.8,
            )
            scene.bitsVgroup.insert(target_box_index, parity_text)

        if wait_time:
            scene.wait(wait_time)

    def highlightQ1_1(scene):
        HighlightAnimations.animate_step(scene,red=[ 3, 5, 7, 9, 11, 13, 15], orange= [1], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[1, 3, 5, 7, 9, 11, 13, 15])

    def highlightQ1_2(scene):
        HighlightAnimations.animate_step(scene, orange= [0],red=[ 2, 4, 6, 8, 10, 12, 14], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[0, 2, 4, 6, 8, 10, 12, 14])

    def highlightQ2_1(scene, potentialBits):
        HighlightAnimations.animate_step(scene, orange=[2], red=[3, 6, 7, 10, 11, 14, 15], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[2, 3, 6, 7, 10, 11, 14, 15])

    def highlightQ2_2(scene, potentialBits):
        HighlightAnimations.animate_step(scene, orange=[0], red=[1, 4, 5, 8, 9, 12, 13], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[0, 1, 4, 5, 8, 9, 12, 13])

    def highlightQ3_1(scene, potentialBits):
        HighlightAnimations.animate_step(scene,orange=[4], red=[5, 6, 7, 12, 13, 14, 15], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[4, 5, 6, 7, 12, 13, 14, 15],potentialBits=potentialBits, opac=.5)

    def highlightQ3_2(scene, potentialBits):
        HighlightAnimations.animate_step(scene, orange=[0], red=[1, 2, 3, 8, 9, 10, 11], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[0, 1, 2, 3, 8, 9, 10, 11],potentialBits=potentialBits, opac=.5)

    def highlightQ4_1(scene, potentialBits):
        HighlightAnimations.animate_step(scene, orange= [8], red=[ 9, 10, 11, 12, 13, 14, 15], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[8, 9, 10, 11, 12, 13, 14, 15],potentialBits=potentialBits, opac=.5)

    def highlightQ4_2(scene, potentialBits):
        HighlightAnimations.animate_step(scene, orange=[0], red=[1, 2, 3, 4, 5, 6, 7], opac = .5)
        scene.wait(HIGHLIGHT_TIME)
        HighlightAnimations.animate_step(scene, clear=[0, 1, 2, 3, 4, 5, 6, 7],potentialBits=potentialBits, opac=.5)

