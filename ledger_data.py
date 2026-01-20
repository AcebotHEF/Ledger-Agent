import pandas as pd

def get_ledger():
    data = {
        "Date": ["2025-07-01", "2025-07-01", "2025-07-02", "2025-07-02", "2025-07-03"],
        "Description": ["Customer Payment", "Revenue Recorded", "Office Supplies", "Cash Paid", "Consulting Income"],
        "Account": ["Accounts Receivable", "Revenue", "Office Supplies", "Cash", "Revenue"],
        "Debit": [0, 500, 100, 100, 0],
        "Credit": [500, 0, 0, 0, 1500],
    }
    df = pd.DataFrame(data)
    return df