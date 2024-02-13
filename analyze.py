# Place code below to do the analysis part of the assignment.

import csv

data_file = open("data/clean_data.csv", "r")
reader = csv.DictReader(data_file)

decade_totals = {}
decade_counts = {}

line = next(reader, None)
while line:
    if line['Year'].isdigit():
        year_int = int(line['Year'])
        decade_key = (year_int // 10) * 10
        monthly_values = []
        month_index = 0

        months= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        while month_index < len(months):
            month = months[month_index]
            if line[month].strip() and line[month] != '****':
                monthly_values.append(float(line[month]))
            month_index+= 1
        
        if monthly_values:
            annual_sum = sum(monthly_values)
            if decade_key not in decade_totals:
                decade_totals[decade_key] = 0
                decade_counts[decade_key] = 0
            decade_totals[decade_key] += annual_sum
            decade_counts[decade_key] += len(monthly_values)
    
    line = next(reader, None)


data_file.close()

decade = 1880
while decade<= (year_int // 10) * 10:
    start_year= decade
    end_year= decade + 9
    if end_year > year_int:
        end_year = year_int 
        
    total_anomaly = decade_totals.get(decade, 0)
    total_count = decade_counts.get(decade, 0)
    average_anomaly = (total_anomaly / total_count) if total_count else 0
    print(f"From {start_year} to {end_year} ：{average_anomaly / 12:.2f}°F")
    decade+= 10