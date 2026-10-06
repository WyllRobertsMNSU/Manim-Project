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
from Animations import HighlightAnimations
from Logic import Logic

class HammingCode(Scene):
    bitsVgroup = []

    def construct(self):
        # Tracking values in grid positions 0 to 15
        self.grid_values = [0] * 16

        bitBoxes = VGroup(*[Square(side_length=1) for _ in range(16)])
        bitBoxes.arrange_in_grid(rows=4, cols=4)
        self.bit_boxes = bitBoxes  # Store reference for animate_step

        parity_boxes = [
            bitBoxes[0],
            bitBoxes[1],
            bitBoxes[2],
            bitBoxes[4],
            bitBoxes[8],
        ]

        function_message = Text(
            "(15, 11) hamming code", font_size=24
        ).move_to([4, 3.5, 0])
        raw_bits_str = "10110101011"
        for bit in raw_bits_str:
            self.bitsVgroup.append(Text(bit))
        bits = Text(raw_bits_str, font_size=30).move_to([4.5, 0.5, 0])
        bits_display = Text(raw_bits_str, font_size=30).move_to([4.5, 0.5, 0])

        box_animation = FadeIn(bitBoxes)
        message_animation = FadeIn(function_message)
        bit_fade_in = FadeIn(bits)
        highlight_animation = [
            box.animate.set_fill(YELLOW, opacity=0.6) for box in parity_boxes
        ]

        self.play(
            *[
                box_animation,
                message_animation,
                bit_fade_in,
                *highlight_animation,
            ]
        )
        self.wait(1)

        bit_box_index_map = {
            0: 3,
            1: 5,
            2: 6,
            3: 7,
            4: 9,
            5: 10,
            6: 11,
            7: 12,
            8: 13,
            9: 14,
            10: 15,
        }

        # Populate tracked values from raw input string
        for bit_idx, box_idx in bit_box_index_map.items():
            self.grid_values[box_idx] = int(raw_bits_str[bit_idx])

        self.play(FadeOut(function_message))
        grid_fill_message = Text(
            "Bits fill grid top to bottom left to right", font_size=24
        ).move_to([4, 3.5, 0])
        self.play(FadeIn(grid_fill_message))

        for bit_index in bit_box_index_map:
            box_index = bit_box_index_map[bit_index]
            self.play(
                bits[bit_index].animate.move_to(bitBoxes[box_index]),
                run_time=0.2,
            )

        self.play(FadeIn(bits_display))
        self.wait(1)

        self.play(FadeOut(grid_fill_message))

        # -----------------------------------
        # CLEAR PARITY SQUARES & REMOVE DISPLAY BITS
        # -----------------------------------
        clear_initial_parity_boxes = [
            box.animate.set_fill(YELLOW, opacity=0.0) for box in parity_boxes
        ]
        self.play(*clear_initial_parity_boxes, FadeOut(bits_display))

        # -----------------------------------
        # EXPLANATION
        # -----------------------------------
        calc_message = Text(
            "Parity bits are calculated by adding the 1's in each section",
            font_size=22,
        ).to_edge(UP)

        self.play(FadeIn(calc_message))
        self.wait(3)  # 3 second pause for the viewer

        even_rule_message = Text(
            "If the number of 1's is even, the parity bit is a 0.", font_size=20
        ).next_to(calc_message, DOWN)

        self.play(FadeIn(even_rule_message))
        self.wait(2)  # Delay before starting calculations

        # -----------------------------------
        # region HAMMING CODE STEPS (PARITY CALCULATION)
        # -----------------------------------

        # Step 1: Parity Bit 1 (Pos 1)
        HighlightAnimations.animate_step(self, yellow=[1], red=[3, 5, 7, 9, 11, 13, 15], opac=0.6, wait_time=0.5)

        HighlightAnimations.animate_step(self, green=[1], clear=[3, 5, 7, 9, 11, 13, 15], opac=0.6, wait_time=0.5)

        # Step 2: Parity Bit 2 (Pos 2)
        HighlightAnimations.animate_step(
            self, yellow=[2], green=[1], red=[3, 6, 7, 10, 11, 14, 15], opac=0.6, wait_time=0.5
        )

        HighlightAnimations.animate_step(self, green=[1, 2], clear=[3, 6, 7, 10, 11, 14, 15], opac=0.6, wait_time=0.5)

        # Step 3: Parity Bit 4 (Pos 4)
        HighlightAnimations.animate_step(
            self, yellow=[4], green=[1, 2], red=[5, 6, 7, 12, 13, 14, 15], opac=0.6, wait_time=0.5
        )

        HighlightAnimations.animate_step(self, green=[1, 2, 4], clear=[5, 6, 7, 12, 13, 14, 15], opac=0.6, wait_time=0.5)

        # Step 4: Parity Bit 8 (Pos 8)
        HighlightAnimations.animate_step(
            self, yellow=[8], green=[1, 2, 4], red=[9, 10, 11, 12, 13, 14, 15], opac=0.6, wait_time=0.5
        )

        HighlightAnimations.animate_step(
            self, green=[1, 2, 4, 8], clear=[9, 10, 11, 12, 13, 14, 15], opac=0.6, wait_time=0.5
        )

        # Step 5: Overall Parity Bit 0 (Pos 0)
        HighlightAnimations.animate_step(
            self, yellow=[0], green=[1], red=[2, 4, 6, 8, 10, 12, 14], opac=0.6, wait_time=0.5
        )

        HighlightAnimations.animate_step(self, green=[0, 1, 2, 4, 8], clear=[6, 10, 12, 14], opac=0.6, wait_time=0.5)
        self.play(FadeOut(even_rule_message))
        self.play(FadeOut(calc_message))
        #endregion
        self.bitsVgroup = VGroup(self.bitsVgroup)

        '''This is where the bit needs to be flipped'''
        print(f"bit at index 13 is {self.bitsVgroup[13]}")
        self.bitsVgroup[13] = Text(str(1))

        #region Error Detection
        errorCheckResults = Logic.detectError(self.bitsVgroup)
        potentialBits1 = []
        
        explanationText = Text("To find the error we will begin by\n checking the parity of columns 1 and 3"
                               , font_size=24).move_to([3, 3.5, 0])
        self.play(FadeIn(explanationText))
        self.wait(5)
        newExplanationText = Text("To do so we will count up the 1s within the red boxes\n and then check whether adding\n the orange box results in an even number", 
                                  font_size=24).move_to([3, 3.5, 0])
        self.play(FadeTransform(explanationText, newExplanationText))
        explanationText = newExplanationText
        self.wait(5)
        
        newExplanationText = Text("If it is even then there is no error",
                                  font_size=24).move_to([3, 3.5, 0])
        self.play(FadeTransform(explanationText, newExplanationText))
        explanationText = newExplanationText
        if(errorCheckResults[1][0]):
            HighlightAnimations.highlightQ1_2(scene=self)
            potentialBits1 = [0, 2, 4, 6, 8, 10, 12, 14]
        else:
            HighlightAnimations.highlightQ1_2(scene=self)
            self.wait(3)
            newExplanationText = Text("Since the error wasn't found we will check\n the parity of the remaining columns",
                                      font_size=24).move_to([3, 3.5, 0])
            self.play(FadeTransform(explanationText, newExplanationText))
            explanationText = newExplanationText
            self.wait(3)
            HighlightAnimations.highlightQ1_1(scene=self)
            potentialBits1 =  [1, 3, 5, 7, 9, 11, 13, 15]
        
        newExplanationText= Text("Now we will check the two left\n most columns for an error",
                                 font_size=24).move_to([3, 3.5, 0])
        self.play(FadeTransform(explanationText, newExplanationText))
        explanationText = newExplanationText
        self.wait(3)
        if(errorCheckResults[1][1]):
            HighlightAnimations.highlightQ2_2(scene=self, potentialBits=potentialBits1)
            potentialBits1 = set(potentialBits1).intersection([0, 1, 4, 5, 8, 9, 12, 13])
        else:
            HighlightAnimations.highlightQ2_2(scene=self, potentialBits=potentialBits1)
            self.wait(3)
            newExplanationText = Text("Since the error wasn't found\n we will check\n the parity of the remaining columns",
                                      font_size=24).move_to([3, 3.5, 0])
            self.play(FadeTransform(explanationText, newExplanationText))
            explanationText = newExplanationText
            self.wait(3)
            HighlightAnimations.highlightQ2_1(scene=self,potentialBits=potentialBits1)
            potentialBits1 = set(potentialBits1).intersection([2, 3, 6, 7, 10, 11, 14, 15])
        
        HighlightAnimations.animate_step(scene=self, yellow = potentialBits1, opac=0.5)
        
        newExplanationText = Text("Now we will perform similiar checks on the rows of the grid\n starting with row 1 and 3",
                                    font_size=24).move_to([3, 3.5, 0])
        self.play(FadeTransform(explanationText, newExplanationText))
        explanationText = newExplanationText
        self.wait(3)
        
        potentialBits2 = []
        if(errorCheckResults[1][2]):
            HighlightAnimations.highlightQ3_2(scene=self, potentialBits= potentialBits1)
            potentialBits2 = [0, 1, 2, 3, 8, 9, 10, 11]
        else:
            HighlightAnimations.highlightQ3_2(scene=self, potentialBits= potentialBits1)
            newExplanationText = Text("Since the error wasn't found we will check\n the parity of the remaining rows",
                                      font_size=24).move_to([3, 3.5, 0])
            self.play(FadeTransform(explanationText, newExplanationText))
            explanationText = newExplanationText
            self.wait(3)
            HighlightAnimations.highlightQ3_1(scene=self, potentialBits= potentialBits1)
            potentialBits2 = [4, 5, 6, 7, 12, 13, 14, 15]
        
        newExplanationText = Text("Now we will perform checks on rows 1 and 2",
                                              font_size=24).move_to([3, 3.5, 0])
        self.play(FadeTransform(explanationText, newExplanationText))
        explanationText = newExplanationText
        if(errorCheckResults[1][3]):
            HighlightAnimations.highlightQ4_2(scene=self, potentialBits=potentialBits1)
            potentialBits2 = set(potentialBits2).intersection([0, 1, 2, 3, 4, 5, 6, 7])
        else:
            HighlightAnimations.highlightQ4_2(scene=self, potentialBits=potentialBits1)
            newExplanationText = Text("Since the error wasn't found we will check\n the parity of the remaining rows",
                                      font_size=24).move_to([3, 3.5, 0])
            self.play(FadeTransform(explanationText, newExplanationText))
            explanationText = newExplanationText
            self.wait(3)
            HighlightAnimations.highlightQ4_1(scene=self, potentialBits=potentialBits1)
            potentialBits2 = set(potentialBits2).intersection([8, 9, 10, 11, 12, 13, 14, 15])
        
        HighlightAnimations.animate_step(scene=self, yellow = potentialBits2, opac=0.5)
        self.wait(2)
        
        HighlightAnimations.animate_step(scene=self, green = errorCheckResults[0], clear=(potentialBits1.union(potentialBits2)).difference(errorCheckResults[0]), opac=.5)
        self.wait(5)
        self.play(FadeOut(explanationText))
        #endregion