import matplotlib.pyplot as plt
import numpy as np


############################## SCATTER
# X_data = np.random.random(50) * 1000
# Y_data = np.random.random(50) * 1000

# print(X_data)
#
# plt.scatter(X_data,Y_data, c="red", marker="*") #c= as COLOR, marker = as the SYMBOL, s= as the SIZE, alpha= as the OPACITY
# plt.show()
############################## PLOT
# years = [2006 + x for x in range(16)]
# weight = [80,83,84,85,86,82,81,79,83,80,82,81,84,83,85,88]
# print(years)
# plt.plot(years,weight,linestyle="--") #lw= thickness, linestyle = style of the line
# plt.show()
############################## BAR
# x = ["C++","C#","Python","Java","Javascipt"]
# y = [20,50,140,1,45]
# plt.bar(x,y,color="red")#color= as COLOR, align= as the ALIGNMENT of the words,
#                         # width= as the width of the bar,edgecolor= color the border of the bar
# plt.show()
################################ HIST
# ages = np.random.normal(20,1.5,1000) #(mean,standard devriation,number)
# plt.hist(ages)# bins= as the number of bins, cumulative=
# plt.show()
################################ PIE
# langs = ["Python","C++","Java","C#","Js"]
# votes = [50,24,14,6,32]
# explodes = [0.3,0,0,0,0]
#
# plt.pie(votes, labels=langs,explode=explodes,autopct="%.2f%%") #labels = pie labels,explodes= pull out in the pie,
#                                                                #autopct= to put % inside the pie
#                                                                #pctdistance = distance of the pct inside the pie
#                                                                #startangle = to rotate the pie by degree
# plt.savefig("pie.png")
############################### BOXPLOT
# heights = np.random.normal(172,8,300)
# plt.boxplot(heights)
# plt.show()

############################# DESIGNING PLOTTING
# years = [2014,2015,2016,2017,2018,2019,2020,2021]
# income = [55,56,62,61,72,72,73,75]
#
# income_ticks = list(range(50,81,2))
# plt.plot(years,income)
# plt.title("My Income",fontsize=20,fontname="Arial")
# plt.ylabel("Income")
# plt.yticks(income_ticks,[f"{x}k$" for x in income_ticks])
# plt.xlabel("Year")
# plt.show()

# stock_a = [100,102,56,1,101,155,287]
# stock_b = [90,95,106,108,167,170,155]
# stock_c = [105,93,143,167,167,154,155]
#
# plt.plot(stock_a,label="Company 1") #To write a label
# plt.plot(stock_b,label="Company 2")
# plt.plot(stock_c,label="Company 3")
# plt.legend(loc="upper right") #loc= Location of each label
#
# plt.show()
################################# DESIGNING PIE
# from matplotlib import style
#
# style.use("dark_background") #To set the pie dark
#
# votes = [10,2,5,16,22]
# people = ["A","B","C","D","E"]
#
# plt.pie(votes,labels=None)
# plt.legend(labels=people,loc="upper right")
# plt.show()

################# SHOW SEPERATE

# x1, y1 = np.random.random(100), np.random.random(100)
# x2, y2 = np.arange(100), np.random.random(100)
#
# plt.figure(1)
# plt.scatter(x1,y1)
#
# plt.figure(2)
# plt.plot(x2,y2)
# plt.show()

######################## Set graphs in the same figure by rows and columns
# x = np.arange(100)
# fig,axs = plt.subplots(2,2)
# axs[0,0].plot(x,np.sin(x))
# axs[0,0].set_title("Sine Wave")
# fig.suptitle("Four Plots") # The main title of the figure
# plt.show()

# plt.tight_layout() # To avoid overlapping
#
# plt.savefig("fourPlots.png",dpi=,transparent=) # To save by PNG,dpi= FOR RESOLUTION OF THE PIC,transparent= To Save WITHOUT BACKGROUND

######################## 3D PLOTTING
# ax = plt.axes(projection="3d") # set the plt by 3 dimension
# x = np.arange(0,50,0.1)
# y = np.sin(x)
# z = np.cos(x)
# ax.scatter(x,y,z)

# x = np.arange(-5,5,0.1)
# y = np.arange(-5,5,0.1)
#
# X,Y = np.meshgrid(x,y)
# Z = np.sin(X) * np.cos(Y)
#
# ax.plot_surface(X,Y,Z, cmap="Spectral")

# ax.set_title("3D PLOT")
# ax.set_xlabel("test")#label for x
# ax.set_ylabel("test")#label for y
# ax.set_zlabel("test")#label for z
# plt.show()

# import random
#
# heads_tails = [0,0]
# for _ in range(100000):
#     heads_tails[random.randint(0,1)] += 1
#     plt.bar(["Heads","Fails"],heads_tails,color=["red","blue"])
#     plt.pause(0.001)
# plt.show()