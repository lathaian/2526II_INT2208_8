def classify_triangle(a, b, c):
    # Check invalid input
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        return "invalid input"

    if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100:
        return "invalid input"

    # Check triangle condition
    if not (a + b > c and a + c > b and b + c > a):
        return "not a triangle"

    # Classify triangle
    if a == b and b == c:
        return "equilateral"

    if a == b or b == c or a == c:
        return "isosceles"

    return "scalene"