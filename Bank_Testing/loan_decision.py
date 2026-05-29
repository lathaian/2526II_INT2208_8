def is_one_decimal(value):
    """
    Kiểm tra income có tối đa 1 chữ số thập phân hay không.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    return round(value, 1) == value


def loan_decision(age, income, credit_score, employment):
    """
    Hàm ra quyết định phê duyệt khoản vay cá nhân.
    """

    # Kiểm tra age
    if not isinstance(age, int) or isinstance(age, bool):
        return "Invalid Input"

    if age < 18 or age > 65:
        return "Invalid Input"

    # Kiểm tra income
    if not isinstance(income, (int, float)) or isinstance(income, bool):
        return "Invalid Input"

    if not is_one_decimal(income):
        return "Invalid Input"

    if income < 5.0 or income > 500.0:
        return "Invalid Input"

    # Kiểm tra credit_score
    if not isinstance(credit_score, int) or isinstance(credit_score, bool):
        return "Invalid Input"

    if credit_score < 300 or credit_score > 850:
        return "Invalid Input"

    # Kiểm tra employment
    if employment not in ["C", "F"]:
        return "Invalid Input"

    # Phân loại rủi ro
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # Logic nghiệp vụ
    if risk == "High":
        return "REJECT"

    if income < 15.0:
        if employment == "F" or risk == "Medium":
            return "REJECT"
        return "MANUAL REVIEW"

    if income >= 15.0:
        if employment == "C":
            return "APPROVE"
        return "MANUAL REVIEW"