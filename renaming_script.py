import os 
  
os.chdir(r'C:\tensorflow\unmasked-dataset') 
print(os.getcwd()) 
COUNT = 600
  
def increment(): 
    global COUNT 
    COUNT = COUNT + 1
  
  
for f in os.listdir(): 
    f_name, f_ext = os.path.splitext(f) 
    f_name = int(f_name)+ COUNT 
  
    new_name = '{} {}'.format(f_name, f_ext) 
    os.rename(f, new_name) 