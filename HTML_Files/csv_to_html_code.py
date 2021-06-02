# Use pandas to convert csv to HTML table
import pandas as pd
import os
  
# Get path where csv exists
path = os.path.join('Resources', 'cities.csv')

# Read csv file
cities_df = pd.read_csv(path)
  
# Save as html file
table_html = cities_df.to_html('Resources/table.html', index=False, classes=['table', 'table-striped'])