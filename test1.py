# from manim import *

# class PowerGraphs(Scene):
#     def construct(self):
#         # Create axes
#         axes = Axes(
#             x_range=[-2, 2, 1],
#             y_range=[0, 16, 4],
#             axis_config={"color": BLUE}
#         )
        
#         # Add labels to the axes
#         labels = axes.get_axis_labels(x_label="x", y_label="y")
        
#         # Display the axes
#         self.play(Create(axes), Write(labels))
#         self.wait(2)

#         # Plot y = x^2
#         graph_x2 = axes.plot(lambda x: x**2, color=YELLOW, x_range=[-2, 2])
#         label_x2 = MathTex("y = x^2").next_to(graph_x2, RIGHT)
#         self.play(Create(graph_x2), Write(label_x2))
#         self.wait(1)
#         self.play(FadeOut(label_x2))
        
#         # Plot y = x^4
#         graph_x4 = axes.plot(lambda x: x**4, color=RED, x_range=[-2, 2])
#         label_x4 = MathTex("y = x^4").next_to(graph_x4, RIGHT)
#         self.play(Transform(graph_x2, graph_x4), Write(label_x4))
#         self.wait(1)
#         self.play(FadeOut(label_x4))
        
#         # Plot y = x^6
#         graph_x6 = axes.plot(lambda x: x**6, color=GREEN, x_range=[-2, 2])
#         label_x6 = MathTex("y = x^6").next_to(graph_x6, RIGHT)
#         self.play(Transform(graph_x2, graph_x6), Write(label_x6))
#         self.wait(1)
#         self.play(FadeOut(label_x6))
        
#         # Plot y = x^8
#         graph_x8 = axes.plot(lambda x: x**8, color=PURPLE, x_range=[-2, 2])
#         label_x8 = MathTex("y = x^8").next_to(graph_x8, RIGHT)
#         self.play(Transform(graph_x2, graph_x8), Write(label_x8))
#         self.wait(2)

# # If running in an interactive environment like Jupyter notebook, you would use:
# if __name__ == "__main__":
#     scene = PowerGraphs()
#     scene.render()

from manim import *

class PowerGraphs(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-2, 2, 0.5],
            y_range=[0, 16, 2],
            axis_config={"color": BLUE, "font_size": 20}
        ).add_coordinates().scale(0.8)

        
        # Add labels to the axes
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        Title
        title = Text("Graphs of y = x^n", font_size=24)
        title.to_edge(UP)
        
        # Display the title and axes
        self.play(Write(title))
        self.play(Create(axes), Write(labels))
        self.wait(2)

        # Function to create graph with a given exponent and color
        def create_graph(exponent, color):
            return axes.plot(lambda x: x**exponent, color=color, x_range=[-2, 2])
        
        # Display the graphs with labels
        graphs = [
            (2, YELLOW),
            (4, RED),
            (6, GREEN),
            (8, PURPLE)
        ]

        for exponent, color in graphs:
            graph = create_graph(exponent, color)
            label = MathTex(f"y = x^{exponent}").next_to(graph, DOWN)
            self.play(Transform(axes, axes), Create(graph), Write(label))
            self.wait(1)
            self.play(FadeOut(label))
        
        self.wait(2)

if __name__ == "__main__":
    # config.pixel_height = 2160
    # config.pixel_width = 3840
    # config.frame_rate = 60
    scene = PowerGraphs()
    scene.render()
