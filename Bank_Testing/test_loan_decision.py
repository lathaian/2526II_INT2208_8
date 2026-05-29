from loan_decision import loan_decision


test_cases = [
    # Test cases cho age
    ("TC01", 17, 20.0, 750, "C", "Invalid Input"),
    ("TC02", 18, 20.0, 750, "C", "APPROVE"),
    ("TC03", 19, 20.0, 750, "C", "APPROVE"),
    ("TC04", 64, 20.0, 750, "C", "APPROVE"),
    ("TC05", 65, 20.0, 750, "C", "APPROVE"),
    ("TC06", 66, 20.0, 750, "C", "Invalid Input"),
    ("TC07", 18.5, 20.0, 750, "C", "Invalid Input"),

    # Test cases cho income
    ("TC08", 30, 4.9, 750, "C", "Invalid Input"),
    ("TC09", 30, 5.0, 750, "C", "MANUAL REVIEW"),
    ("TC10", 30, 5.1, 750, "C", "MANUAL REVIEW"),
    ("TC11", 30, 14.9, 750, "C", "MANUAL REVIEW"),
    ("TC12", 30, 15.0, 750, "C", "APPROVE"),
    ("TC13", 30, 15.1, 750, "C", "APPROVE"),
    ("TC14", 30, 499.9, 750, "C", "APPROVE"),
    ("TC15", 30, 500.0, 750, "C", "APPROVE"),
    ("TC16", 30, 500.1, 750, "C", "Invalid Input"),
    ("TC17", 30, 15.55, 750, "C", "Invalid Input"),

    # Test cases cho credit_score
    ("TC18", 30, 20.0, 299, "C", "Invalid Input"),
    ("TC19", 30, 20.0, 300, "C", "REJECT"),
    ("TC20", 30, 20.0, 500, "C", "REJECT"),
    ("TC21", 30, 20.0, 501, "C", "APPROVE"),
    ("TC22", 30, 20.0, 700, "C", "APPROVE"),
    ("TC23", 30, 20.0, 701, "C", "APPROVE"),
    ("TC24", 30, 20.0, 850, "C", "APPROVE"),
    ("TC25", 30, 20.0, 851, "C", "Invalid Input"),
    ("TC26", 30, 20.0, 705.5, "C", "Invalid Input"),

    # Test cases cho employment
    ("TC27", 30, 20.0, 750, "C", "APPROVE"),
    ("TC28", 30, 20.0, 750, "F", "MANUAL REVIEW"),
    ("TC29", 30, 20.0, 750, "X", "Invalid Input"),

    # Test cases kiểm tra logic nghiệp vụ
    ("TC30", 30, 20.0, 400, "C", "REJECT"),
    ("TC31", 30, 10.0, 600, "C", "REJECT"),
    ("TC32", 30, 10.0, 750, "F", "REJECT"),
    ("TC33", 30, 10.0, 750, "C", "MANUAL REVIEW"),
    ("TC34", 30, 20.0, 600, "C", "APPROVE"),
    ("TC35", 30, 20.0, 600, "F", "MANUAL REVIEW"),
]


passed = 0
failed = 0

print("KẾT QUẢ CHẠY TEST CASES")
print("-" * 80)

for tc_id, age, income, credit_score, employment, expected in test_cases:
    actual = loan_decision(age, income, credit_score, employment)

    if actual == expected:
        result = "Passed"
        passed += 1
    else:
        result = "Failed"
        failed += 1

    print(
        f"{tc_id}: "
        f"Input=({age}, {income}, {credit_score}, {employment}) | "
        f"Expected={expected} | Actual={actual} | Result={result}"
    )

print("-" * 80)
print(f"Tổng số test cases: {len(test_cases)}")
print(f"Số test cases Passed: {passed}")
print(f"Số test cases Failed: {failed}")

if failed == 0:
    print("Kết luận: Code đã passed qua toàn bộ 35 test cases.")
else:
    print("Kết luận: Code chưa passed toàn bộ test cases.")