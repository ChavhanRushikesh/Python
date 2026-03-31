#Ass-42

# 1. Implement Simple Linear Regression manually without using any ML library.
# Dataset
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]

# Tasks
# Calculate:
# 1. Mean of X (X̄ )
# 2. Mean of Y (Ȳ)
# 3. Slope (m)
# 4. Intercept (c)


# Expected Output Example
# Mean of X = 3
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4
# Regression Equation:
# Y = 0.4X + 2.4
# Predicted Y for X = 6 : 4.8

import numpy as np

def SimpleLinearRegression():
    
    border = "- " * 50
    # Dataset
        
    # Mean of X:
    # X̄ = sum(X_i) / n
    
    X = [1,2,3,4,5]
    
    # Mean of Y:
    # Ȳ = sum(Y_i) / n
    Y = [3,4,2,4,5]
    print(border)
    
    print("Independent Variable ( X )  :",X)
    print("Dependent Variable ( Y ): ",Y)
    
    print(border)
    
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    
    
    print("Mean of ( X ) is ( Independent Variable) : ", mean_X)
    print("Mean of ( Y ) is ( Dependent variable) : ", mean_Y)
    print(border)
    
    
    # Y = mX + C "intercept of line is C"
    
    # m = (sum(x-X_bar) * (Y- Y_bar)) / (Sum(X- X_bar) **2 )   "m = mean slope" 
    
    # calculate the length of Independent variable 
    
    independentLength  = len(X)
    # print(independentLength)
    # print(border)
    
    numerator =  0
    denominator = 0 
    # numerator   = sum((X_i - X̄) * (Y_i - Ȳ))
    # denominator = sum((X_i - X̄)^2)
    for i in range(independentLength):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X)**2)
        
    
    # Slope (m) formula:
    # m = numerator / denominator
    m = numerator / denominator
    print("Slope (m) :", m)
        
    print(border)
    
    # Intercept (C) formula:
    # C = Ȳ - m * X̄
    C = mean_Y - m * mean_X
    print("Intercept ( C ) : ",C)
    
    print(border)
    
    # Linear Regression Equation:
    # Y = m * X + C
    
    X_array= np.array(X)
    
    m = np.float64(m)
    C = np.float64(C)
    
    Y = m * X_array + C
    print("Linear Equation : ", Y )
    
    X_new = 6
    Y_new = m * X_new + C
    print(f"Predicted Y for X = {X_new}:", Y_new)
    # print(border)
    
    
def main():
    SimpleLinearRegression()

if __name__ == "__main__":
    main()
    