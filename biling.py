import zipfile

def parse_file(path_to_file):
    # Enum(env, farm, farm_role, server)
    datafile=path_to_file.split("/")[-1][:-4]
    comma=b','
    archive = zipfile.ZipFile(path_to_file, 'r')
    print(datafile[:-4])
    with archive.open(datafile,'r') as source_info:
        z = source_info.readline()
        print(z)
        # while(z):
        k=0
        while(k<100):
            k=k+1
            d=z.split(comma)
            data=d[-1].split(b":")
            cost=d[-3]
            # print(z.split(comma)[-1])
            if len(data)>4:
                print(data[4])
                print(data[4][:-2])
                print(cost)
                print(cost[1:-1])
            # if d[0:]
            z = source_info.readline()

if __name__ == "__main__":
    parse_file("/home/asmodeyz/Work/TestTask/615271354814-aws-billing-detailed-line-items-with-resources-and-tags-2016-05.csv.zip")
