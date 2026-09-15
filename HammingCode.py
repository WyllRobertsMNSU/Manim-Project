from manim import *

class HammingCode(Scene):
    def construct(self):
        bitBoxes = VGroup(Square(side_length= 1) for x in range(16))
        bitBoxes.arrange_in_grid()
        self.add(bitBoxes)
        bit = Text("1")
        bit.add()
        self.wait(1)
        self.play(bit.move_to(bitBoxes[0]).animate())
        