import csv
data=[
	['S.no','Roll.no','Name'],
	[1,101,"Abc"],
	[2,202,"Def"],
	[3,303,"Ghi"]
]
#open a file in write mode
with open('sample_table.csv',"w",newline='') as file:
	w=csv.writer(file)
	w.writerows(data)
