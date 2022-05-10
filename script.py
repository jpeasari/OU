import os
name1 = 'barcodes.tsv.gz'
name2 = 'matrix.mtx.gz'
name3 = 'features.tsv.gz'
os.chdir('D:/Dave/snRNA/all_data/')

for files in os.listdir():
    print(files)
    
 for samples in os.listdir():
    os.chdir(samples)
    for file in os.listdir():
        split_tup = os.path.splitext(file)
        file_ext = split_tup[1]
        if file.endswith('barcodes.tsv.gz'):
            os.rename(file, name1)
            
        if file.endswith('features.tsv.gz'):
            os.rename(file,name3)
            
        if file.endswith('matrix.mtx.gz'):
                os.rename(file,name2)

    os.chdir('../')
      
