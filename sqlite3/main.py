import sqlite3
import csv
from sqlite3.dbapi2 import Cursor


class ex_1:
	def get_cur(): #exercise 1
		conn = sqlite3.connect('database.sqlite')
		cur = conn.cursor()
		return cur, conn

	def execute_query(query):
		cursor.execute(query)
		row_data = cursor.fetchall()

		return row_data



	def get_names(): #exercice 2,3
		query = """
			SELECT name
			FROM 
				sqlite_schema
			WHERE 
				type ='table' AND 
				name NOT LIKE 'sqlite_%';
		"""

		tbl_nms_list = []
		row_data = ex_1.execute_query(query)

		for i in range(0, len(row_data)):
			tbl_nms_list.append(str(row_data[i])[2:-3])

		names_line = 'The database contains the following tables: '

		for i in tbl_nms_list:
			if i == tbl_nms_list[-1]:
				names_line += i + '.'
			else:
				names_line += i + ', '
		return names_line, tbl_nms_list
		
	def get_cnt(tbl_nms_list):
		output_dict = {}
		
		for i in range(0, len(tbl_nms_list)):
			cursor.execute('SELECT COUNT(*) FROM {}'.format(tbl_nms_list[i]))
			answ = str(cursor.fetchall())
			output_dict[tbl_nms_list[i]] = answ[2:-3:1]

		return output_dict



	def write_txt(names_line):
		with open('db_tbl_names.txt', 'w') as f:
			f.write(names_line)
			return True

	def read_txt():
		with open('db_tbl_names.txt', 'r') as f:
			print(f.read())
			return True


	def write_csv(data_dict):
		header = ['table_name', 'row_count']
		
		with open('csv_file.csv', 'w', newline='') as f:
			writer = csv.writer(f)

			writer.writerow(header)
			
			for i in data_dict:
				di1 = [i, data_dict[i]]
				writer.writerow(di1)

		return True


	def read_csv():
		with open('csv_file.csv', newline='') as f:  
			reader = csv.reader(f)
			
			for row in reader:
				if row[0] == 'table_name':
					continue
				else:
					print('Table {} has {} records.'.format(row[0], row[1]))
		return True



if __name__ == "__main__":
	cursor, con = ex_1.get_cur()
	names_line, tbl_nms_list = ex_1.get_names()
	

	print('\n##### Exercise 1.1 - 1.4 #####')
	ex_1.write_txt(names_line) 
	ex_1.read_txt()
	
	
	print('\n##### Exercise 1.5 - 1.6 #####')
	ex_1.write_csv(ex_1.get_cnt(tbl_nms_list))
	ex_1.read_csv()
	print('\n')

	#Close connection with db
	con.close()

# Output:
# ##### Exercise 1.1 - 1.4 #####
# The database contains the following tables: Player_Attributes, Player, Match, League, Country, Team, Team_Attributes.

# ##### Exercise 1.5 - 1.6 #####
# Table Player_Attributes has 183978 records.
# Table Player has 11060 records.
# Table Match has 25979 records.
# Table League has 11 records.
# Table Country has 11 records.
# Table Team has 299 records.
# Table Team_Attributes has 1458 records.
