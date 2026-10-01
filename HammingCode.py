from manim import *

class HammingCode(Scene):
    def construct(self):
        bitBoxes = VGroup(Square(side_length= 1) for _ in range(16))
        bitBoxes.arrange_in_grid()
        parity_boxes = [bitBoxes[0], bitBoxes[1], bitBoxes[2], bitBoxes[4], bitBoxes[8]]

        function_message = Text("(15, 11) hamming code", font_size=24).move_to([4, 3.5, 0])
        bits = Text("10110101011", font_size=30).move_to([4.5, 0.5, 0])
        bits_display = Text("10110101011", font_size=30).move_to([4.5, 0.5, 0])

        
        box_animation = FadeIn(bitBoxes)
        message_animation = FadeIn(function_message)
        bit_fade_in = FadeIn(bits)
        highlight_animation = [box.animate.set_fill(YELLOW, opacity = 0.6) for box in parity_boxes]
        

        self.play(*[box_animation, message_animation, bit_fade_in, highlight_animation])
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
            10: 15 
        }
        self.play(FadeOut(function_message))
        grid_fill_message = Text("Bits fill grid top to bottom left to right", font_size=24).move_to([4, 3.5, 0])
        self.play(FadeIn(grid_fill_message))
        for bit_index in bit_box_index_map:
            box_index = bit_box_index_map[bit_index] #get the value of dict
            self.play(bits[bit_index].animate.move_to(bitBoxes[box_index]), run_time=0.2)
        self.play(FadeIn(bits_display))
        self.wait(1)

        self.play(FadeOut(grid_fill_message))
        
        