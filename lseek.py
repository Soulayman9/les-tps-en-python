import os  
    
path = './alfa.txt'
  

fd = os.open(path, os.O_RDWR|os.O_CREAT) 
  
s = 'ENSAT cours programmation system'
  
# Convert the string to bytes  
line = str.encode(s) 
 
os.write(fd, line) 

os.lseek(fd, 0, 0) 
  
# Read the file 
s = os.read(fd, 16) 
  
# Print string 
print(s) 
  
# Close the file descriptor  
os.close(fd) 