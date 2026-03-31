#Ass-41

# 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.



# The program should:
# • Calculate Euclidean distance
# • Sort distances
# • Select K nearest neighbors
# • Predict the class based on majority voting
# Dataset


# Tasks
# 1. Accept X and Y coordinates of a new point from the user.
# 2. Compute Euclidean distance from all dataset points.
# 3. Sort the distances.
# 4. Select K = 3 nearest neighbors.
# 5. Predict the class label.

# Input Format
# Enter X coordinate: 2
# Enter Y coordinate: 2
# Expected Output
# Nearest Neighbors:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41
# Predicted Class: Red.


# Dataset 

#      Point  X   Y   Label
    #   A     1   2   Red
    #   B     2   3   Red
    #   C     3   1   Blue
    #   D     6   5   Blue



import math

def EuclideanX(Point1 , Point2):
    Ans = math.sqrt((Point1["X"] - Point2["X"])**2 + (Point1["Y"] - Point2["Y"])**2)
    return Ans

def NeighborsClassifierFunc():
    border = "- " * 55
    
    print(border)
    print("Print the dataset : ")
    print(border)
    data = [    
        {"Point" : "A" ,"X": 1,"Y":2,"Label":"Red"},
        {"Point" : "B" ,"X": 2,"Y":3,"Label":"Red"},
        {"Point" : "C" ,"X": 3,"Y":1,"Label":"Blue"},
        {"Point" : "D" ,"X": 6,"Y":5,"Label":"Blue"}
    ]
    
    for idata in data:
        print(idata)
        
    # calculate the new point  = 2,2
    
    newPoint = {'X':2,"Y":2}
    
    for i in data:# add the distance column 
        i["Distance"] = EuclideanX(i,newPoint)

    print(border)
    for idata in data:
        print("Distance Calculated : ",idata)
        
    print(border)
    # sorted() is used to sort the  distance column in asc order 
    sorted_data = sorted(data,key=lambda item : item["Distance"])
    for sd in sorted_data:
        print("Sorted Data",sd)
        
    
    print(border)
    k = 3 
    nearestValues = sorted_data[:k]

    for nV  in nearestValues:
        print(f"Nearest Neighbor : {nV["Point"]} - Distance : {nV["Distance"]}")
    
    vote = {}
    print(border)
    for neighbor in nearestValues:
        label = neighbor["Label"]
        
        print("Label printing ",label)
        vote[label] = vote.get(label,0)+1
    
    for i in vote:
        print(f"Name :{i}, Number of vote : {vote[i]}")
    
    print(border)
    predictedClass = max(vote,key=vote.get) # type: ignore
    
    
    print("Predicted class is : ",predictedClass)
def main():
    NeighborsClassifierFunc()

if __name__ == "__main__":
    main()
    