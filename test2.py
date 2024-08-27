from manim import *

class WriteTextLetterByLetter(Scene):
    def construct(self):
        # Create the text
        f = u'\U0001d453'
        text1 = MarkupText(
            f'if  f (<span fgcolor="{BLUE}">x+1</span>) = <span fgcolor="{BLUE}">x</span>\u2074 - <span fgcolor="{BLUE}">x</span> + 1',
            slant=ITALIC
        )
        text2 = MarkupText(
            f'Then f(<span fgcolor="{BLUE}">0</span>) = ?',
            slant=ITALIC
        )

        # Position text1 and text2
        text1.move_to(ORIGIN)
        text2.next_to(text1, DOWN)

        # Animate the text being written letter by letter
        self.play(Write(text1, run_time=2))
        self.play(Write(text2, run_time=1.5))

        # Create the target position for text1 and text2
        text1.generate_target()
        text2.generate_target()
        text1.target.to_edge(UP)
        text2.target.next_to(text1.target, DOWN)

        # Move text1 and text2 to their new positions with smooth transition
        self.play(MoveToTarget(text1, run_time=1.5, rate_func=smooth))
        self.play(MoveToTarget(text2, run_time=1.5, rate_func=smooth))

        # Extract characters from text1 and text2 to create the new expression
        x_plus_1 = text1[3:8].copy()
        zero = text2[6:7].copy()

        # Create new Text objects for x+1 and 0 with different colors
        new_x_plus_1 = Text("x+1", color=BLUE, font_size=36, slant=ITALIC)
        new_zero = Text("0", color=BLUE, font_size=36, slant=ITALIC)
        new_x_plus_1.move_to(DOWN)

        # Position new_x_plus_1 and equal sign
        equal_sign = Text(" = ", font_size=36, slant=ITALIC)
        equal_sign.next_to(new_x_plus_1, RIGHT)
        new_zero.next_to(equal_sign, RIGHT)

        # Animate the transformation of x+1 and 0 with easing functions
        self.play(TransformFromCopy(x_plus_1, new_x_plus_1, path_arc=90*DEGREES, run_time=1.5))
        self.play(Write(equal_sign, run_time=0.75))
        self.play(TransformFromCopy(zero, new_zero, path_arc=90*DEGREES, run_time=1.5))

        # Group them together
        expression = VGroup(new_x_plus_1, equal_sign, new_zero)

        # Position the expression and animate to its final position
        expression.generate_target()
        expression.target.next_to(text2, DOWN)
        self.play(MoveToTarget(expression, run_time=1.5, rate_func=smooth))

        # Create new Text objects for the final equation components
        copy_x = expression[0].copy()
        new_x = Text("x", color=BLUE, font_size=36, slant=ITALIC)
        new_equal = Text(" = ", font_size=36, slant=ITALIC)
        copy_equal = expression[1].copy()
        new_zero = Text("0", color=BLUE, font_size=36, slant=ITALIC)
        copy_zero = expression[2].copy()
        new_minus = Text(" - ", font_size=36, slant=ITALIC)
        new_one = Text("1", color=BLUE, font_size=36, slant=ITALIC)
        copy_one = expression[0].copy()

        # Position them x + 1 = 0
        new_x.move_to(ORIGIN)
        new_equal.next_to(new_x, RIGHT)
        new_zero.next_to(new_equal, RIGHT)
        new_minus.next_to(new_zero, RIGHT)
        new_one.next_to(new_minus, RIGHT)

        # Animate the transformation to 'x = 0 - 1'
        self.play(TransformFromCopy(copy_x, new_x, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(copy_equal,new_equal, run_time=1.5))
        self.play(TransformFromCopy(copy_zero, new_zero, path_arc=90*DEGREES, run_time=1.5))
        self.play(Write(new_minus, run_time=0.75))
        self.play(TransformFromCopy(copy_one,new_one, path_arc=90*DEGREES, run_time=0.75))

        final_expression = VGroup(new_x, new_equal, new_zero, new_minus, new_one) #x=0-1
        final_expression.generate_target()
        final_expression.target.next_to(expression,DOWN)
        self.play(MoveToTarget(final_expression, run_time=1.5, rate_func=smooth))

        self.play(Transform(expression, final_expression, run_time=1.5, rate_func=smooth))

        final_text = MarkupText(
            f'So, we have <span fgcolor="{BLUE}">x = -1</span>', font_size=36, slant=ITALIC
        )
        final_text.generate_target()
        final_text.target.next_to(text2,DOWN)

        self.play(Transform(final_expression,final_text, run_time=1, rate_func=smooth))
        self.play(FadeOut(expression, run_time=1))

        self.play(
            MoveToTarget(final_text, run_time=1, rate_func=smooth),   
            FadeOut(final_expression, run_time = 1)
        )

        solve_f0 = text2[4:8].copy()
        solve_eq = text1[8:9].copy()
        solve_x4 = text1[9:11].copy()
        solve_minus = text1[11:12].copy()
        solve_mone = text1[12:13].copy()
        solve_plus = text1[13:14].copy()
        solve_one = text1[14:15].copy()

        new_solve_f0 = Text("f(0)", color=BLUE, font_size=36, slant=ITALIC)
        new_solve_eq = Text("=", color=BLUE, font_size=36, slant=ITALIC)
        new_solve_x4 = Text("(-1)\u2074", color=BLUE, font_size=36, slant=ITALIC)
        new_solve_minus = Text("-", color=BLUE, font_size=36, slant=ITALIC)
        new_solve_mone = Text("(-1)", color=BLUE, font_size=36, slant=ITALIC)
        new_solve_plus = Text("+", color=BLUE, font_size=36, slant=ITALIC)
        new_solve_one = Text("1", color=BLUE, font_size=36, slant=ITALIC)

        new_solve_f0.move_to(DOWN)
        new_solve_eq.next_to(new_solve_f0, RIGHT)
        new_solve_x4.next_to(new_solve_eq, RIGHT)
        new_solve_minus.next_to(new_solve_x4, RIGHT)
        new_solve_mone.next_to(new_solve_minus, RIGHT)
        new_solve_plus.next_to(new_solve_mone, RIGHT)
        new_solve_one.next_to(new_solve_plus, RIGHT)

        self.play(TransformFromCopy(solve_f0, new_solve_f0, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(solve_eq ,new_solve_eq, run_time=1.5))
        self.play(TransformFromCopy(solve_x4, new_solve_x4, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(solve_minus, new_solve_minus, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(solve_mone, new_solve_mone, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(solve_plus, new_solve_plus, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(solve_one, new_solve_one, path_arc=90*DEGREES, run_time=1.5))

        final_solve = VGroup(new_solve_f0, new_solve_eq,new_solve_x4,new_solve_minus,new_solve_mone, new_solve_plus,new_solve_one)

        final_solve.generate_target()
        final_solve.target.next_to(final_text, DOWN)
        self.play(MoveToTarget(final_solve, run_time=1.5, rate_func=smooth))

        more_f0 = final_solve[0:2].copy()
        more_x4 = final_solve[2:3].copy()
        more_one = final_solve[3:5].copy()
        more_plus = final_solve[5:6].copy()
        more_aone = final_solve[6:7].copy()

        new_more_f0 = Text("f(0) =", color=BLUE, font_size=36, slant=ITALIC)
        new_more_x4 = Text("1", color=BLUE, font_size=36, slant=ITALIC)
        new_more_one = Text("+ 1", color=BLUE, font_size=36, slant=ITALIC)
        new_more_plus = Text("+", color=BLUE, font_size=36, slant=ITALIC)
        new_more_aone =Text("1", color=BLUE, font_size=36, slant=ITALIC)

        new_more_f0.move_to(DOWN)
        new_more_x4.next_to(new_more_f0,RIGHT)
        new_more_one.next_to(new_more_x4,RIGHT)
        new_more_plus.next_to(new_more_one,RIGHT)
        new_more_aone.next_to(new_more_plus,RIGHT)
        
        self.play(TransformFromCopy(more_f0, new_more_f0, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(more_x4, new_more_x4, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(more_one, new_more_one, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(more_plus, new_more_plus, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(more_aone, new_more_aone, path_arc=90*DEGREES, run_time=1.5))
        
        final_more = VGroup(new_more_f0,new_more_x4, new_more_one, new_more_plus, new_more_aone)

        final_more.generate_target()
        final_more.target.next_to(final_solve, DOWN)
        self.play(MoveToTarget(final_more, run_time=1.5, rate_func=smooth))

        last_f0 = final_more[0:2]
        last_ans = final_more[2:]
        new_last_f0 = Text("f(0) =")
        ans = Text("3")
        new_last_f0.move_to(DOWN)
        ans.next_to(new_last_f0,RIGHT)

        self.play(TransformFromCopy(last_f0, new_last_f0, path_arc=90*DEGREES, run_time=1.5))
        self.play(TransformFromCopy(last_ans, ans, path_arc=90*DEGREES, run_time=1.5))
        






        self.wait(2)

if __name__ == "__main__":
    scene = WriteTextLetterByLetter()
    scene.render()

