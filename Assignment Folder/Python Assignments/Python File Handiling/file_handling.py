import csv 
all_regions_data=open("C:\\Users\\VijayaPrasanthKumarB\\Documents\\all_regions_data.csv","w+") 
all_regions_write_obj=csv.writer(all_regions_data)

def read_data_from_different_regions(region):
    
    try:
        region_data=open(f"C:\\Users\\VijayaPrasanthKumarB\Documents\\{region}Employees.csv","r+") 

        row_obj=csv.reader(region_data) 

        for row in row_obj:
            all_regions_write_obj.writerow(row)
        region_data.close()    



    except FileNotFoundError:
        print(f"File With Name {region}Employees Not Found")  
    except PermissionError:
        print(f"You Don't Have Required Permission To {region} File")  
               


regions=["India","Africa","Europe","Us","Aus","China"] 

for data  in regions:
    read_data_from_different_regions(data) 

all_regions_data.close()



