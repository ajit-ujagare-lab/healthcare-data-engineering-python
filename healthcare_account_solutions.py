# Python Operators - Healthcare Debt Collection
# Practice Project for Azure Data Engineering

# --------------------------------------------------
# Starting Account
# --------------------------------------------------

account = {
    "account_id": "ACC1001",
    "bill_amount": 5000,
    "insurance_paid": 3500,
    "payment": 500,
    "status": "IN_COLLECTION"
}


# --------------------------------------------------
# Q1. Calculate patient's responsibility after insurance
# --------------------------------------------------

patient_responsibility = (
    account["bill_amount"] - account["insurance_paid"]
)

print("Q1 Patient Responsibility:", patient_responsibility)


# --------------------------------------------------
# Q2. Calculate remaining balance after payment
# --------------------------------------------------

remaining_balance = (
    patient_responsibility - account["payment"]
)

print("Q2 Remaining Balance:", remaining_balance)


# --------------------------------------------------
# Q3. Add remaining balance to account dictionary
# --------------------------------------------------

account["remaining_balance"] = remaining_balance

print("Q3 Account:", account)


# --------------------------------------------------
# Q4. Check whether remaining balance is greater than 0
# --------------------------------------------------

print(
    "Q4 Outstanding Balance:",
    account["remaining_balance"] > 0
)


# --------------------------------------------------
# Q5. Check whether remaining balance is equal to 0
# --------------------------------------------------

print(
    "Q5 Fully Paid:",
    account["remaining_balance"] == 0
)


# --------------------------------------------------
# Q6. Check whether remaining balance is >= $1,000
# --------------------------------------------------

print(
    "Q6 Balance >= $1000:",
    account["remaining_balance"] >= 1000
)


# --------------------------------------------------
# Q7. Outstanding balance AND IN_COLLECTION
# --------------------------------------------------

print(
    "Q7 Requires Collection:",
    account["remaining_balance"] > 0
    and account["status"] == "IN_COLLECTION"
)


# --------------------------------------------------
# Q8. Status is PAID OR CLOSED
# --------------------------------------------------

print(
    "Q8 Account Closed:",
    account["status"] == "PAID"
    or account["status"] == "CLOSED"
)


# --------------------------------------------------
# Q9. Check whether account does NOT have zero balance
# --------------------------------------------------

print(
    "Q9 Has Outstanding Balance:",
    not (account["remaining_balance"] == 0)
)


# --------------------------------------------------
# Q10. Check whether status is valid
# --------------------------------------------------

valid_statuses = [
    "NEW",
    "IN_COLLECTION",
    "PROMISE_TO_PAY",
    "PAID",
    "CLOSED"
]

print(
    "Q10 Valid Status:",
    account["status"] in valid_statuses
)


# --------------------------------------------------
# Q11. Check whether UNKNOWN status is invalid
# --------------------------------------------------

account["status"] = "UNKNOWN"

print(
    "Q11 Invalid Status:",
    account["status"] not in valid_statuses
)


# Reset status for remaining exercises
account["status"] = "IN_COLLECTION"


# --------------------------------------------------
# Q12. Check whether phone number is missing
# --------------------------------------------------

phone = None

print(
    "Q12 Phone Missing:",
    phone is None
)


# --------------------------------------------------
# Q13. Add $200 new payment
# --------------------------------------------------

account["payment"] += 200

print(
    "Q13 Updated Payment:",
    account["payment"]
)


# --------------------------------------------------
# Q14. Reduce remaining balance by $200
# --------------------------------------------------

account["remaining_balance"] -= 200

print(
    "Q14 Updated Remaining Balance:",
    account["remaining_balance"]
)


# --------------------------------------------------
# Q15. Insurance paid <= bill amount
# --------------------------------------------------

print(
    "Q15 Insurance Payment Valid:",
    account["insurance_paid"] <= account["bill_amount"]
)


# --------------------------------------------------
# Q16. Payment <= patient responsibility
# --------------------------------------------------

print(
    "Q16 Payment Valid:",
    account["payment"] <= patient_responsibility
)


# --------------------------------------------------
# Q17. Percentage of bill paid by insurance
# --------------------------------------------------

insurance_percentage = (
    account["insurance_paid"]
    / account["bill_amount"]
    * 100
)

print(
    "Q17 Insurance Percentage:",
    insurance_percentage,
    "%"
)


# --------------------------------------------------
# Q18. Outstanding balance OR IN_COLLECTION
# --------------------------------------------------

print(
    "Q18 Active Collection:",
    account["remaining_balance"] > 0
    or account["status"] == "IN_COLLECTION"
)


# --------------------------------------------------
# Q19. Validate account using multiple business rules
# --------------------------------------------------

account_is_valid = (
    account["bill_amount"] > 0
    and account["insurance_paid"] <= account["bill_amount"]
    and account["payment"] <= patient_responsibility
    and account["status"] in valid_statuses
)

print(
    "Q19 Account Valid:",
    account_is_valid
)


# --------------------------------------------------
# Q20. Should account be sent to collection agent?
# --------------------------------------------------

send_to_collection = (
    account["remaining_balance"] > 0
    and account["status"] == "IN_COLLECTION"
    and account["remaining_balance"] >= 500
)

print(
    "Q20 Send to Collection:",
    send_to_collection
)


# --------------------------------------------------
# Q21. Calculate unpaid percentage
# --------------------------------------------------

unpaid_percentage = (
    account["remaining_balance"]
    / patient_responsibility
    * 100
)

print(
    "Q21 Unpaid Percentage:",
    unpaid_percentage,
    "%"
)


# --------------------------------------------------
# Q22. Check whether balance is between $500 and $2,000
# --------------------------------------------------

balance_between_range = (
    account["remaining_balance"] >= 500
    and account["remaining_balance"] <= 2000
)

print(
    "Q22 Balance Between $500 and $2000:",
    balance_between_range
)


# --------------------------------------------------
# Q23. Check whether status is neither PAID nor CLOSED
# --------------------------------------------------

active_collection_status = (
    account["status"] != "PAID"
    and account["status"] != "CLOSED"
)

print(
    "Q23 Active Status:",
    active_collection_status
)


# --------------------------------------------------
# Q24. Payment > 0 AND outstanding balance
# --------------------------------------------------

payment_and_balance_valid = (
    account["payment"] > 0
    and account["remaining_balance"] > 0
)

print(
    "Q24 Payment and Balance Valid:",
    payment_and_balance_valid
)


# --------------------------------------------------
# Q25. Number of $250 payments required
# --------------------------------------------------

number_of_payments = (
    account["remaining_balance"] / 250
)

print(
    "Q25 Number of $250 Payments:",
    number_of_payments
)
