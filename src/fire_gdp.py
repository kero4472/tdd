import csv

def get_data(file_name,
             query_column=None,
             query_value=None,
             return_header=False):
    
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
      
        header = next(reader)

        rows = []
        for row in reader:
            if query_column is None or query_value is None:
                rows.append(row)
            elif row[query_column] == query_value:
                rows.append(row)

    if return_header:
        return header, rows

    return rows


def get_column_index(header, column_name):
    
    try:
        return header.index(column_name)
    
    except ValueError:
        return None


def get_fire_gdp_year_data(co2_file, gdp_file, country):

    co2_header, co2_rows = get_data(
        co2_file, 
        query_column=0,
        query_value=country,
        return_header=True
    )

    gdp_header, gdp_rows = get_data(
        gdp_file,
        query_column=0,
        query_value=country,
        return_header=True
    )

    fire_index = get_column_index(co2_header, 'Forest fires')

    results = []

    for row in co2_rows:
        year = row[1]

        forest_fires = row[fire_index]
  

        if forest_fires == '':
            continue

        forest_fires = float(forest_fires)

        gdp_year_idx = get_column_index(gdp_header, year)

        if gdp_year_idx is None:
            continue

        gdp_value = gdp_rows[0][gdp_year_idx]

        if gdp_value == '':
            continue

        year = int(year)

        gdp_value = float(gdp_value)

        results.append([year, forest_fires, gdp_value])

    return results