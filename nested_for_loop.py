# colors = ['red', 'blue', 'green']
# sizes = ['L', 'M', 'S']
# for color in colors:
#     for size in sizes:
#         print(f"{color} - Size {size}")

# years = [1997, 1998]
# months = ['jan', 'feb']
# days = range(1, 29)

# for y in years:
#     for m in months:
#         for d in days:
#             print(f"report_{d}_{m}_{y}.csv")

# Writing SQL Query
# Metadata driven pipeline for data engineering
tables = ['users', 'location', 'contact', 'master', 'sales', 'purchase', 'reports', 'surveys']
fields = ['id', 'email']
for table in tables:
    for field in fields:
        print(f"SELECT count(*) FROM {table} WHERE {field} IS NULL;")

