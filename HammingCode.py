from manim import *
from Logic import Logic
from Animations import HighlightAnimations
'''
class HammingCode(Scene):
    def construct(self):

        #region Intro Sequence
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
        #end sequence
'''
class DetectError(Scene):  
    def construct(self):
        self.findError()


    def  findError(self):
        #region Remove After scene completion
        bitBoxes = VGroup(Square(side_length= 1) for _ in range(16))
        bitBoxes.arrange_in_grid()
        parity_boxes = [bitBoxes[0], bitBoxes[1], bitBoxes[2], bitBoxes[4], bitBoxes[8]]

        bits = VGroup(Text('0'), Text('1'), Text('0'), Text('1'), 
                Text('0'), Text('0'), Text('1'), Text('1'), 
                Text('1'), Text('0'), Text('1'), Text('1'), 
                Text('0'), Text('1'), Text('1'), Text('0'))

        for bit, box in zip(bits, bitBoxes):
            bit.move_to(box)
            

        self.add(bits)
        self.add(bitBoxes)
        self.bitBoxes = bitBoxes

        errorCheckResults = Logic.detectError(bits)
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

    