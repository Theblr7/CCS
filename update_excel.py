import json
import openpyxl
from datetime import datetime

def update_excel(entry):
    wb = openpyxl.load_workbook('SpendTracker.xlsx')
    sheet = wb['DailySpend']
    sheet.append([
        entry['date'],
        entry['category'],
        float(entry['amount']),
        entry.get('notes', '')
    ])
    wb.save('SpendTracker.xlsx')

# Example usage
with open('entry.json') as f:
    data = json.load(f)
    update_excel(data)
