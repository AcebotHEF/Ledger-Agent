import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI # <--- CHANGED
from ledger_prompt import ledger_template
from ledger_data import get_ledger

# PASTE YOUR GOOGLE KEY HERE
# GOOGLE_API_KEY
os.environ["GOOGLE_API_KEY"] = "AIzaSyDWMtILwjgxKlZzrioPQAcH4-aWGG5d8CE" 

def run_ledger_analysis():
    df = get_ledger()
    ledger_table = df.to_string(index=False)
    
    prompt = ledger_template.format(ledger_table=ledger_table)
    
    # CHANGED: Using Gemini 1.5 Flash (Fast & Free)
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2
    )
    
    response = llm.invoke(prompt)
    
    return df, response.content