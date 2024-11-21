import numpy as np

#axis = 0 == ROWS
#axis = 1 == COLUMNS

#LIST = slow
#NUMPY = fast with more methods

#NUMPY read less bytes of memory

#Initializing Ex:

# a = np.array([1,2,3],dtype="int16")
# b = np.array([[1,3,4,6,3,2],[3,5,6,3,4,6]],dtype="int32")
# # print(b.ndim) # Get dimension
# # print(b.shape) # Get Shape
#
# # print(a.dtype) # Print the data type
# # print(b.itemsize) # Print the itemsize by bytes
#
# print(b.size)

############################### ACCESSING CHANGING SPECIFIC ELEMENTS FOR ROW AND COL

# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
#Get by index
# print(a[1,5])
# print(a[0,]) # OUTPUT [1,2,3,4,5,6,7]
# print(a[:,2]) # OUTPUT [3,10]

##[startI:endI:step]
# print(a[0,1:6:2])
# a[1,5] = 20 # Specific change
# a[0,1:-1]= 5
# a[:,2] = [1,2]
# print(a)

## 3D
# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b[0,1,1]) # OUTPUT 4
# print(b[0,1,:]) # OUTPUT [3,4]
# print(b[:,1,:]) # OUTPUT [3,4],[7,8]
# print(b[:,:,1]) # OUTPUT [2,4][6,8]

############################# INITIALIZING DIFFERENT TYPES OF ARRAYS

# c = np.zeros([5,3]) # Generate full 0 arrays
# print(c)
# c = np.ones([5,3,5]) # Generate full 1 arrays
# print(c)
# c = np.full([2,2,3],55) # Generate full of given number or string
# print(c)
# c = np.full_like(b,5) # Generate full of the given data type array
# print(b.shape)
# print(c)
# c = np.empty((3,4))
# print(c)

## Filling arrays
# c = np.arange(0,1001,5) #[start,bound,step]
# print(c)

# c = np.linspace(0,1000,5) #[start,bound,number of we want to generate]
# print(c)

## NONE and INFINITY
# print(np.nan)
# print(np.inf)
# ## Boolean
# np.isnan
# np.inf

# SAmple of them is sqrt of -1 is nan and num divided by 0 is undefine or infinity

################################# PERFORM MATHEMATICAL OPERATION

# a = np.array([1,2,3])
# b = np.array([4,5,6]) # OUTPUT [5,7,9]

# a = np.array([1,2,3])
# b = np.array([[1],
#               [2]]) # OUTPUT [[2 3 4],[3 4 5]]
# print(a + b) #ALL works also for * / -

# a = np.array([5,6,7])
# print(np.sqrt(a))
# print(np.cos(a)) #[sin,tan,arcten,exp,log,log10]

################################ ARRAY FUNCTION

# a = np.array([1,2,3])
# a = np.append(a,[5,6,7]) # OUTPUT [1 2 3 5 6 7]
# a = np.insert(a, [3], 4) # OUTPUT [1 2 3 4 5 6 7]

# a = np.array([[1,2,3],[4,5,6]])
# a = np.delete(a,1,0) #NOT USE BRACKET
# print(a)

################################ STRUCTURING METHODS
# a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# a = a.reshape([10,2]) # ANYTHING THAT CAN BE MULTIPLY BY THE SIZE AND IT NEEDS TO BE ASSIGN

# a.resize([2,10]) # RESIZE NO NEED TO ASSIGN

# var = a.flatten() # SHOW THE VIEW FLATTEN OF THE ARRAY
# var[2] = 100
# var = a.ravel() # REAL FLATTING THE ARRAY
# var[2] = 100
# print(a.shape)
# print(a)

# var = [v for v in a.flat]
# print(var)

# print(a.transpose()) # BY COLUMN and can use a.T
# print(a.swapaxes(0,1))

############################### CONCATINATING, STACKING, SPLITTING
# a1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# a2 = np.array([[11,12,13,14,15],[16,17,18,19,20]])

# a = np.concatenate([a1,a2], axis=0)
# a = np.stack([a1,a2]) # Act as stack

# a = np.vstack([a1,a2]) # STACKING VERTICAL
# a = np.hstack([a1,a2]) # STACKING HORIZONTAL

# print(a)

# a = np.array([[1,2,3,4,5,6],
#               [7,8,9,10,11,12],
#               [13,14,15,16,17,18],
#               [19,20,21,22,23,24]])

# print(np.split(a,2,axis=0))
## AGGREGATE FUNCTIONS
# print(a.max())
# print(a.min())
# print(a.mean())
# print(a.std())
# print(a.sum())
# print(np.median(a))

############################ RANDOM
# numbers = np.random.randint(90, 100,size=[2,3,4])
# numbers = np.random.binomial(2,p=0.5,size=(5,10)) # p = possibility
# numbers = np.random.choice([10,20,30,40,50],size=(5,4))
# print(numbers)

# a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# np.save("myarray.npy",a)

# a = np.load("myarray.npy") # Save as  npy
# np.savetxt("myarray.csv",a,delimiter=":")
# a = np.loadtxt("myarray.csv",delimiter=":")
# print(a)
