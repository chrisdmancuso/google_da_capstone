import pandas as pd

def create_half_csv(file_name):
    print(file_name)
    with open(file_name, 'r') as f:
        data = f.readlines()

    halfway = int(len(data) / 2)
    data[halfway] = f'{data[halfway]}ride_id,rideable_type,started_at,ended_at,start_station_name,start_station_id,end_station_name,end_station_id,start_lat,start_lng,end_lat,end_lng,member_casual\n'
    print(data[halfway])
    with open("copy_" + file_name, 'w') as f:
        f.writelines(data)
    df = pd.read_csv(file_name, nrows=halfway, index_col=False)
    new_file_name = file_name[:-4] + '_1st' + '.csv'
    df.to_csv(new_file_name)
    df = pd.read_csv(file_name, skiprows=halfway+1, index_col=False)
    new_file_name = file_name[:-4] + '_2nd' + '.csv'
    df.to_csv(new_file_name)
        

if __name__ == '__main__':
    while True:
        try:
            file = str(input("Enter file name: \n"))
            create_half_csv(file)
        except:
            print("File not found")
        choice = str(input("Read another file (Y/N): \n"))
        if choice.lower() == 'n':
            break
        
    
