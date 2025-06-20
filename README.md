# 📐 Visualizing an Inequality with Manim

This project uses **Manim**, a Python library for animations, to show a visual explanation of the inequality:

\[
x + \frac{1}{x} \geq 2 \quad \text{(for all } x > 0\text{)}
\]

---

## 🎬 What the Animation Shows

1. It starts with a math assumption:  
   \( x > 0 \) and \( x \geq \frac{1}{x} \)

2. Then it draws a right triangle:
   - The base is 2 units long
   - The height is \( x - \frac{1}{x} \)
   - The hypotenuse is calculated using the Pythagorean Theorem

3. The hypotenuse is transformed into a straight line showing \( x + \frac{1}{x} \)

4. Finally, it compares that to 2, showing that the inequality is true.

It's like a visual proof using geometry, not just algebra.

---

## ▶️ How to Run This

Make sure you have **Manim** installed. You can install it using pip:

```bash
pip install manim
manim -pql animate_proof.py AnimateText
