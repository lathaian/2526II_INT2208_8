from Triangle import classify_triangle


test_cases = [
    ("TC_01", 0, 50, 50, "invalid input"),
    ("TC_02", 101, 50, 50, "invalid input"),
    ("TC_03", 50, 0, 50, "invalid input"),
    ("TC_04", 50, 50, 101, "invalid input"),

    ("TC_05", 10, 20, 50, "not a triangle"),
    ("TC_06", 1, 2, 3, "not a triangle"),

    ("TC_07", 50, 50, 50, "equilateral"),
    ("TC_08", 100, 100, 100, "equilateral"),

    ("TC_09", 50, 50, 40, "isosceles"),
    ("TC_10", 40, 50, 50, "isosceles"),
    ("TC_11", 50, 40, 50, "isosceles"),

    ("TC_12", 3, 4, 5, "scalene"),
    ("TC_13", 98, 99, 100, "scalene")
]


passed = 0
failed = 0

print("Running triangle classification test suite...\n")

for tc_id, a, b, c, expected in test_cases:
    actual = classify_triangle(a, b, c)

    if actual == expected:
        result = "PASSED"
        passed += 1
    else:
        result = "FAILED"
        failed += 1

    print(f"{tc_id}: input=({a}, {b}, {c}) | expected={expected} | actual={actual} | {result}")

print("\nSummary")
print(f"Total test cases: {len(test_cases)}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")