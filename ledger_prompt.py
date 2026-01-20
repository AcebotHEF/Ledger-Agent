# We use langchain_core to avoid the "ImportError"
from langchain_core.prompts import PromptTemplate

ledger_template = PromptTemplate.from_template("""
You are a financial ledger analyst AI. Analyze the following transactions:

{ledger_table}

Tasks:
1. Identify if the debits equal credits.
2. Highlight any imbalances or potential errors.
3. Provide a one-paragraph explanation of the ledger status.
""")