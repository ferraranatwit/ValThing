
# import required module
import os
# assign directory
directory = 'labels'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    
    with open(f) as file:
        lines = file.readlines()
        lines.replace('15','0')
            
