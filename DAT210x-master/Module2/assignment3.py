import pandas as pd

# Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..
headers = ['motor', 'screw', 'pgain', 'vgain', 'class']
df = pd.read_csv('Datasets/servo.data', names=headers)

# Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..
vgain_slice = df[df.vgain == 5]
print(len(vgain_slice))

# Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
multi_slice = df[(df.motor == 'E') & (df.screw == 'E')]
print(len(multi_slice))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
pgain_slice = df[df.pgain == 4]
print(pgain_slice.describe())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!



