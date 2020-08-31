# %%

# import modules
import numpy as np
import itertools

# generate random data which basically performs sine function
sample_args = np.linspace(-np.pi, +np.pi, 19)
sample_vals = np.sin(sample_args)

# write generated data to file for further reading
np.savetxt("sample_data.txt", np.column_stack((sample_args, sample_vals)))

# load all data from file
args, vals = np.loadtxt("sample_data.txt", unpack=True)
print("\n\n--> All data loaded and arguments and values are stored in seperate arrays: \n")
print(args)
print(vals)

# grab only values
vals = np.loadtxt("sample_data.txt", usecols=(1))
print("\n\n--> Only value column is loaded from file: \n")
print(vals)

# skip first 5 rows then load all
'''first add dummy header to the file with new line below'''
header = "Dummy header for data file"
with open("sample_data.txt", 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header.rstrip('\r\n') + '\n\n' + content)

vals = np.loadtxt("sample_data.txt", usecols=(1), skiprows=2)
print("\n\n--> Header is ignored and only data is retrieved: \n")
print(vals)

# load specific lines of file
'''differently from above itertools to slice file portion'''
vals = np.loadtxt("sample_data.txt", usecols=(1), skiprows=6, max_rows=5)
print("\n\n--> Line datas between 5-10 loaded only: \n")
print(vals)

