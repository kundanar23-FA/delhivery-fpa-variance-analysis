import csv
import random
from datetime import datetime, timedelta

NUM_ROWS = 15000

# Delhivery cost structure
cost_centers = ['Express Parcel (B2C)', 'Part Truckload (PTL)', 'Supply Chain Services', 'Cross-Border', 'Corporate HQ']
weights = [0.45, 0.25, 0.15, 0.05, 0.10]

gl_accounts = {
    'Line-haul Costs (Fuel & Tolls)': 'OPEX',
    'Freight Handling & Contract Labor': 'OPEX',
    'Facility Leases (Hubs & Gateways)': 'OPEX',
    'Employee Benefit Expenses': 'OPEX',
    'Cloud Hosting (Orion Platform)': 'OPEX',
    'Automated Sorter Systems': 'CAPEX',
    'Material Handling Equipment (AGVs)': 'CAPEX',
    'IT Infrastructure (Servers)': 'CAPEX'
}
gl_names = list(gl_accounts.keys())

vendors = ['Indian Oil Corp', 'Reliance BP Mobility', 'AWS India', 'Blue Yonder', 
           'Local Fleet Operator A', 'Local Fleet Operator B', 'Vanderlande Sorters', 'Prologis Warehousing']

start_date = datetime(2024, 4, 1)

print("Generating 15,000 rows of Delhivery ERP data...")

with open('Delhivery_Simulated_GL.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Header row
    writer.writerow(['Transaction_ID', 'Date', 'Cost_Center', 'GL_Account_Name', 'Account_Category', 'Vendor_Name', 'Budget_INR', 'Actual_INR'])

    for i in range(1, NUM_ROWS + 1):
        trx_id = f"GL-{random.randint(100000, 999999)}"
        random_days = random.randint(0, 730)
        trx_date = start_date + timedelta(days=random_days)
        date_str = trx_date.strftime('%Y-%m-%d')
        
        cc = random.choices(cost_centers, weights=weights)[0]
        gl_name = random.choice(gl_names)
        category = gl_accounts[gl_name]
        vendor = random.choice(vendors)
        
        # Introduce a minor vendor typo for data cleaning practice
        if random.random() < 0.02:
            vendor = 'Amazon Web Serv'
            
        budget = round(random.uniform(10000, 500000), 2)
        
        # Q3 Fuel Spike Logic
        is_q3 = trx_date.month in [10, 11, 12]
        if gl_name == 'Line-haul Costs (Fuel & Tolls)' and is_q3:
            actual = budget * random.uniform(1.20, 1.40)
        elif gl_name == 'Cloud Hosting (Orion Platform)':
            actual = budget * random.uniform(1.05, 1.15)
        else:
            actual = budget * random.uniform(0.95, 1.05)
            
        actual = round(actual, 2)
        
        writer.writerow([trx_id, date_str, cc, gl_name, category, vendor, budget, actual])

print("SUCCESS! File saved as 'Delhivery_Simulated_GL.csv' in your current folder.")