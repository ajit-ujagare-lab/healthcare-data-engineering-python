# healthcare-data-engineering-python
Python practice projects for Azure Data Engineering using a healthcare domain.


# Python Operators - Healthcare Debt Collection

## Project Overview

This project is part of my Python learning journey for Azure Data Engineering.

The practice uses a fictional healthcare debt collection business scenario to understand Python operators through real-world business problems.

## Business Scenario

A healthcare debt collection company receives past-due medical accounts from healthcare providers in the USA.

The data contains information such as:

- Account ID
- Original bill amount
- Insurance paid
- Patient payment
- Account status
- Remaining balance

The goal is to use Python to calculate balances, validate account data, and apply business rules.

## Starting Dataset

```python
account = {
    "account_id": "ACC1001",
    "bill_amount": 5000,
    "insurance_paid": 3500,
    "payment": 500,
    "status": "IN_COLLECTION"
}
