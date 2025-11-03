import json
import openpyxl

def update_excel(entry):
    wb = openpyxl.load_workbook('SpendTracker.xlsx')
    sheet = wb['DailySpend']
    sheet.append([
        entry['date'],
        entry['creditCard'],
        entry['category'],
        float(entry['amount']),
        entry.get('notes', ''),
        float(entry['cashback'])
    ])
    wb.save('SpendTracker.xlsx')

with open('entry.json') as f:
    data = json.load(f)
    update_excel(data)
