# 2. The value of K plays an important role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.
# Dataset
# Use the same dataset as Assignment 1.
# Tasks
# Predict the class of the same new point using:
# • K = 1
# • K = 3
# • K = 5
# Expected Output
# Prediction Results
# K = 1 → Red
# K = 3 → Red
# K = 5 → Blue
# Explain why the prediction changes when K increases.


import math 

def EuclideanX(P1,P2):
    Ans = math.sqrt((P1["X"] - P2["X"])**2 + (P1["Y"] - P2["Y"])**2)
    return Ans

# Function for to check the neighbor by changing  k value and accuracy 
def FunctionCheckKvalue():
    
    border = "- "* 55
    
    print("Original Dataset ")
    data = [    
        {"Point" : "A" ,"X": 1,"Y":2,"Label":"Red"},
        {"Point" : "B" ,"X": 2,"Y":3,"Label":"Red"},
        {"Point" : "C" ,"X": 3,"Y":1,"Label":"Blue"},
        {"Point" : "D" ,"X": 6,"Y":5,"Label":"Blue"}
    ]
    
    
    for idata in data:
        print(idata)
        
    newPoint = {"X":2, "Y":2}
    
    print(border)
    for i in data:
        i["Distance"] = EuclideanX(i,newPoint)
        print(i)
        
            
    print(border)
    # sorted() is used to sort the  distance column in asc order 
    sorted_data = sorted(data,key=lambda item : item["Distance"])
    for sd in sorted_data:
        print("Sorted Data",sd)
        
        
    print(border)
    k = 9
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
    FunctionCheckKvalue()
if __name__ == "__main__":
    main()
    