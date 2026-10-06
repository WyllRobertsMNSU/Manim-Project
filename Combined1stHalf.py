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

class Combined1stHalf(Scene):


    def animate_step(self, yellow=None, green=None, red=None, clear=None):
        anims = []

        if yellow:
            anims.extend([
                self.bit_boxes[i].animate.set_fill(YELLOW, opacity=0.6)
                for i in yellow
            ])

        if green:
            anims.extend([
                self.bit_boxes[i].animate.set_fill(GREEN, opacity=0.6)
                for i in green
            ])

        if red:
            anims.extend([
                self.bit_boxes[i].animate.set_fill(RED, opacity=0.6)
                for i in red
            ])

        if clear:
            anims.extend([
                self.bit_boxes[i].animate.set_fill(RED, opacity=0.0)
                for i in clear
            ])

        # Step A: Play background highlighting/clearing animations
        if anims:
            self.play(*anims)

        # Step B: Delay while red/yellow squares are highlighted
        if yellow and red:
            self.wait(1.0)  # Pause to let the viewer see the highlighted red squares

            # Calculate parity value
            parity_value = sum(self.grid_values[i] for i in red) % 2
            target_box_index = yellow[0]
            self.grid_values[target_box_index] = parity_value

            # Spawn bit text on the right side of the screen
            parity_text = Text(
                str(parity_value), font_size=30, color=WHITE
            ).move_to([5.5, 0, 0])

            # Animate bit sliding in from the right into the target yellow square
            self.play(
                FadeIn(parity_text, run_time=0.2),
                parity_text.animate.move_to(self.bit_boxes[target_box_index]),
                run_time=0.8,
            )

        self.wait(0.5)

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
        # HAMMING CODE STEPS (PARITY CALCULATION)
        # -----------------------------------

        # Step 1: Parity Bit 1 (Pos 1)
        self.animate_step(yellow=[1], red=[3, 5, 7, 9, 11, 13, 15])

        self.animate_step(green=[1], clear=[3, 5, 7, 9, 11, 13, 15])

        # Step 2: Parity Bit 2 (Pos 2)
        self.animate_step(
            yellow=[2], green=[1], red=[3, 6, 7, 10, 11, 14, 15]
        )

        self.animate_step(green=[1, 2], clear=[3, 6, 7, 10, 11, 14, 15])

        # Step 3: Parity Bit 4 (Pos 4)
        self.animate_step(
            yellow=[4], green=[1, 2], red=[5, 6, 7, 12, 13, 14, 15]
        )

        self.animate_step(green=[1, 2, 4], clear=[5, 6, 7, 12, 13, 14, 15])

        # Step 4: Parity Bit 8 (Pos 8)
        self.animate_step(
            yellow=[8], green=[1, 2, 4], red=[9, 10, 11, 12, 13, 14, 15]
        )

        self.animate_step(
            green=[1, 2, 4, 8], clear=[9, 10, 11, 12, 13, 14, 15]
        )

        # Step 5: Overall Parity Bit 0 (Pos 0)
        self.animate_step(
            yellow=[0], green=[1], red=[2, 4, 6, 8, 10, 12, 14]
        )

        self.animate_step(green=[0, 1, 2, 4, 8], clear=[6, 10, 12, 14])
