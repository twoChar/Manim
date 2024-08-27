
from manim import *

class AnimateText(Scene):
    def construct(self):
        # The string to animate
        text = "Let x > 0 and assume x ≥ 1 / x"
        
        # Create a MathTex object for the text
        text_obj = MathTex(r"\text{Let } x > 0 \text{ and assume } x \geq \frac{1}{x}", font_size=36, color=YELLOW)
        
        # Position the text at the top of the screen
        text_obj.to_edge(UP)
        
        # Animate the text letter by letter
        self.play(Write(text_obj, run_time=1, rate_func=linear))

        start_point = LEFT
        end_point = RIGHT

        # Create the base line
        base_line = Line(start_point, end_point)

        # Create a curly brace below the base line
        base_brace = Brace(base_line, DOWN)

        # Create a MathTex object for the length of the side with smaller font size
        base_length_text = MathTex("2", font_size=24, color=GREEN).next_to(base_brace, DOWN)

        # Add the vertical line from the end point upwards
        vertical_line = Line(end_point, end_point + UP * 2)

        # Create a curly brace to the right of the vertical line
        vertical_brace = Brace(vertical_line, RIGHT)

        # Create a MathTex object for the length of the vertical side with smaller font size
        vertical_length_text = MathTex(r"x - \frac{1}{x}", font_size=24, color=RED).next_to(vertical_brace, RIGHT)

        # Create the hypotenuse
        hypo = Line(start_point, end_point + UP * 2)

        # Create the triangle and fill it with color
        triangle = Polygon(start_point, end_point, end_point + UP * 2, fill_color=BLUE, fill_opacity=0.5)

        # Create the text for the hypotenuse length with smaller font size
        hypo_text = MathTex(r"\sqrt{2^2 + \left( x - \frac{1}{x} \right)^2}", font_size=24, color=ORANGE)
        hypo_copy = hypo_text.copy()
        
        # Rotate the text to align with the hypotenuse
        angle = hypo.get_angle()
        hypo_text.rotate(angle)
        
        # Position the text in the middle of the hypotenuse
        hypo_text.move_to(hypo.get_center() + UP * 0.6 + LEFT * 0.2)

        # Group all elements related to the triangle
        triangle_group = VGroup(base_line, base_brace, base_length_text, vertical_line, vertical_brace, vertical_length_text, hypo, triangle, hypo_text)
        
        # Shift the entire triangle group downwards
        triangle_group.shift(DOWN * 2)

        # Add the base line, vertical line, and hypotenuse to the scene
        self.play(Create(base_line))
        self.play(Create(base_brace))
        self.play(Write(base_length_text))
        self.play(Create(vertical_line))
        self.play(Create(vertical_brace))
        self.play(Write(vertical_length_text))
        self.play(Create(hypo))
        self.play(Create(triangle))
        self.play(Write(hypo_text))

        # Transform hypo_text
        new_hypo = MathTex(r"x + \frac{1}{x}", font_size=24, color=PURPLE)
        angle = hypo.get_angle()
        new_hypo.rotate(angle)
        new_hypo.move_to(hypo_text)
        self.play(Transform(hypo_text, new_hypo, run_time=1.5, rate_func=smooth))

        # Fade out the vertical line, triangle, braces, and vertical_length_text
        self.play(
            FadeOut(vertical_line),
            FadeOut(triangle),
            FadeOut(vertical_brace),
            FadeOut(base_brace),
            FadeOut(vertical_length_text)
        )
        target_angle = -hypo.get_angle()
        self.play(
            Rotate(hypo, target_angle, about_point=start_point),
            Rotate(hypo_text, target_angle, about_point=hypo_text.get_center())
        )

        add_on = MathTex(r"\geq", font_size=36, color=WHITE).next_to(new_hypo, RIGHT)
        self.play(Write(add_on))
        base_length_text.generate_target()
        base_length_text.target.next_to(add_on, RIGHT)
        self.play(MoveToTarget(base_length_text, run_time=1.5, rate_func=smooth))

        angle = base_line.get_angle()
        hypo_text.rotate(angle)
        newx = VGroup(hypo_text, add_on, base_length_text)
        self.play(newx.animate.shift(DOWN * 3))

        # Fade out the base_line and hypo
        self.play(FadeOut(base_line), FadeOut(hypo))
    
        # Recreate the triangle
        self.play(Create(triangle))
        self.play(Write(MathTex("2", font_size=24, color=GREEN).next_to(triangle, DOWN)))
        self.play(Write(vertical_length_text.next_to(triangle, RIGHT)))

        # Rotate the text to align with the hypotenuse
        hypon = Line(start_point, end_point + UP * 2)
        angle = hypon.get_angle()
        hypo_copy.rotate(angle)

        # Position the text in the middle of the hypotenuse
        hypo_copy.move_to(triangle.get_center() + UP * 0.6 + LEFT * 0.2)

        self.play(Write(hypo_copy))

        self.wait(2)

if __name__ == "__main__":
    scene = AnimateText()
    scene.render()
