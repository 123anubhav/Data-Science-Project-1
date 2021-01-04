


# In[0] :

#LAB 1

#ques 1


import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

f = pd.read_csv("landslide_data3.csv")

Q=list(f["stationid"])
#print(Q)


C=list(f['temperature'])       #converting all the attributes of the data into a list which contain all the values contain by that particular attributes
D=list(f['humidity'])
E=list(f['pressure'])
F=list(f['rain'])
G=list(f['lightavgw/o0']) 
H=list(f['lightmax'])
I=list(f['moisture'])


print("Ques :1")


# fun(T) represent a fuction which return mean,median,mode,min,max,standard deviation of each particular list of all attributes of the given data set
def fun(T):
    T1=np.mean(T)                   #T1=mean
    print("The Mean is :", T1)
    T2=np.median(T)                    #T2=median
    print("The Median is :", T2)
    T3=(statistics.mode(T))           #T3=mode
    print("The Mode is :", T3)
    T4=min(T)                         #T4=min
    print("The Min is :", T4)
    T5=max(T)                         #T5=max
    print("The Max is :", T5)
    l1=[]                                #l1 is list containing square of every element in list(T)
    for i in range(len(T)):
        l1.append(T[i]**2)
    s1=sum(l1)
    T6=(s1/len(T)-(T1**2))**0.5  #standard deviation       #T6=standard deviation
    print("The Standard Deviation is :", T6)
    
l=[C,D,E,F,G,H,I]
l2=['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']   #l2=list representing all the attributes
for i in range(len(l)):                                                                #this loop call the fuction fun for len(l) times
    print("-----------------------------",l2[i],"-----------------------------")
    T=l[i]
    fun(T)                                                                  #return all required values for a particular list
    print("\n")
    
    
# In[1] :

    
print('\n')    
#ques 2    



#2(a)
print("Ques :2(a)")

y1=[C,D,E,G,H,I]  #y1 contains list of all attributes except rain

p1=[' Temperature :Atmospheric temperature around the sensor in Celsius',' Humidity :The concentration of water vapor present in the air','Pressure :Atmospheric pressure in millibars (mb)',' Lightavgw/o0 :The average light throughout the daytime (in lux units)','Lightmax :The maximum lux count by the sensor','Moisture :indicates the water stored in the soil (measured between 0 to 100 percent)']
# scattered_graphrain fuction return all the scattered plot required corresponing to rain with the other attributes
def scattered_graphrain(y1,w1): 
    
        plt.scatter(F, N, c ="pink",  
                    linewidths = 2,  
                    marker ="s",  
                    edgecolor ="black",  
                    s = 50) 

 
        
         
        plt.xlabel("Rain :Measure of rainfall in ml")
         
        plt.ylabel(w1)
        plt.show() 
        
        print('\n')

           
for i in range(len(y1)):           # fuction called for len(y1) times
    print("graph:",i+1)
    N=y1[i]         #the required attributes a that particular time
    w1=p1[i]
    scattered_graphrain(N,w1)   #return the required graph between rain and the other attributes taken
    

#2(b)
print("Ques :2(b)")

y2=[D,E,F,G,H,I]       #y2 contains list of all attributes except temperature

p2=[' Humidity :The concentration of water vapor present in the air','Pressure :Atmospheric pressure in millibars (mb)',"Rain :Measure of rainfall in ml",' Lightavgw/o0 :The average light throughout the daytime (in lux units)','Lightmax :The maximum lux count by the sensor','Moisture :indicates the water stored in the soil (measured between 0 to 100 percent)']

# scattered_graphrain fuction return all the scattered plot required corresponing to temperature with the other attributes
def scattered_graphtemperature(M,w2):
    
        plt.scatter(C, M, c ="pink",  
                    linewidths = 2,  
                    marker ="s",  
                    edgecolor ="black",  
                    s = 50) 

 
        
        plt.xlabel(" Temperature :Atmospheric temperature around the sensor in Celsius") 
        plt.ylabel(w2) 
        plt.show() 
        
        print('\n')

           
for i in range(len(y2)):    # fuction called for len(y2) times
    print("graph:",7+i)
    M=y2[i]    #the required attributes a that particular time
    w2=p2[i]
    scattered_graphtemperature(M,w2)      #return the required graph between temperature and the other attributes taken
    print('\n')
    

# In[2] :

print('\n')
#ques 3

from scipy.stats import pearsonr


#3(a)
print("Ques :3(a)")

y1=[C,D,E,G,H,I]  # list containg values of all attributes inside a list except rain
y3=['temperature','humidity','pressure','lightavgw/o0','lightmax','moisture']    #list containing name of all attributes except rain

# correlation fuction returns the Pearsons correlation between rain with the other elements of list y3
def correlation(F,K,L):
    
    corr, _ = pearsonr(F,K)     #calculating pearsonr correlation between the 2 attributes
    print('------------------------------------------------------------')
    print('Pearsons correlation between rain and {0}:'.format(L)) 
    print('%.3f' % corr)


for i in range(len(y1)):  # fuction called for len(y1) times
    K=y1[i]
    L=y3[i]
    correlation(F,K,L)
    
print('\n')

#3(b)
print("Ques :3(b)")  
    
y2=[D,E,F,G,H,I]                # list containg values of all attributes inside a list except temperature
y4=['humidity','pressure','rain','lightavgw/o0','lightmax','moisture']              #list containing name of all attributes except temperature

# correlation fuction returns the Pearsons correlation between temperature with the other elements of list y2
def correlation(C,K,L):
    
    corr, _ = pearsonr(C,K)    #calculating pearsonr correlation between the 2 attributes
    print('------------------------------------------------------------')
    print('Pearsons correlation between temperature and {0}:'.format(L)) 
    print('%.3f' % corr)


for i in range(len(y1)):        # fuction called for len(y1) times
    K=y2[i]  
    L=y4[i]
    correlation(C,K,L)
 
print('\n')

# In[3] :

#ques 4
print("Ques :4")
print('\n')
#Required histogram for the attributes ‘rain’ and ‘moisture’ 
print("Histogram of moisture and rain")
df = pd.DataFrame({
    'rain': F,
    'moisture': I
    })
hist = df.hist(bins=5)

plt.show()   #retuen the required histogram
print('\n')


# In[4] :

#ques5
print("Ques :5")


#the reqired histogram of attribute ‘rain’ for each of the 10 stations 
f = pd.read_csv("landslide_data3.csv")

df=pd.DataFrame(f,columns=['stationid','rain'])
r=set(Q)   #r   = {'t15', 't13', 't12', 't6', 't8', 't11', 't7', 't9', 't14', 't10'}
h=list(r)
h.sort()

u=df.groupby(['stationid'])   
for i in h:
    y=u.get_group(i)   #group all elements of the 'stationid' together
    y.hist()
    plt.xlabel("Rain :Measure of rainfall in ml")
    plt.ylabel(i)
    plt.show()  #return the required histogram


# In[5] :

#ques 6

# the required boxplot for the attributes ‘rain’ and ‘moisture’
print('\n')
print("Ques :6")

box_plot_data=[I,F]       #list containing list of rain and moisture

plt.boxplot(box_plot_data,patch_artist=True,labels=['moisture','rain'])     
plt.xlabel("Boxplot of both Moisture and Rain")
plt.ylabel("Values of Moisture and Rain ")
plt.show()    #representing both rain and moisture in a single graph

e=[I]    # list containing list of moisture
plt.boxplot(e,patch_artist=True,labels=['moisture'])
plt.xlabel("Boxplot of Moisture")
plt.ylabel("Values of Moisture")
plt.show()     #representing boxplot of moisture

o=[F]        # list containing list of rain
plt.boxplot(o,patch_artist=True,labels=['rain'])
plt.xlabel("Boxplot of Rain")
plt.ylabel("Values of Rain")
plt.show()     #representing boxplot of rain






