import csv
import pandas as pd
import glob

csv_files = glob.glob('*.{}'.format('csv'))
print(csv_files)

data = pd.DataFrame()

for file in csv_files:
	file_tmp = pd.read_csv(file,)
	data = data.append(file_tmp, ignore_index = True)

print (data)

with open ('pink_morsel_sales_data.csv', 'w', newline = '') as csv_write:
	fieldnames = ['sales', 'date', 'region']
	csv_writer = csv.DictWriter(csv_write, fieldnames = fieldnames)
	csv_writer.writeheader()

	for ind in data.index:
		print (data['product'][ind])
		if data['product'][ind] == 'pink morsel':
			sales = float(data['price'][ind].strip('$'))*float(data['quantity'][ind])
			out = {'sales':sales, 'date': data['date'][ind], 'region':data['region'][ind]}
			csv_writer.writerow(out)


#with open('daily_sales_data_0.csv', 'r') as csv_file0:
    #csv_reader0 = csv.DictReader(csv_file0)

    #with open ('pink_morsel_sales_data.csv', 'w', newline = '') as csv_write_file:
        #fieldnames = ['sales', 'date', 'region']
        #csv_writer0 = csv.DictWriter(csv_write_file, fieldnames = fieldnames)
        #csv_writer0.writeheader()

        #for row in csv_reader0:
    	    #if row['product']== 'pink morsel':
    		    #sales = float(row['price'].strip('$'))*float(row['quantity'])
    		    #out = {'sales': '$'+str(sales), 'date': row['date'], 'region': row['region']}
    		    #csv_writer0.writerow(out)
