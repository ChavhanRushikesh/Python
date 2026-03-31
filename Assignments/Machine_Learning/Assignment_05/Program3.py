# 3. Consider below task
# 1. Train linear regression model.
# 2. Predict salary for 6 years of experience.
# 3. Plot regression line using matplotlib.
# Dataset

#     Experience       Salary
#        1             20000
#        2             25000
#        3             30000
#        4             35000
#        5             40000


# Expected Output
# Predicted Salary for 6 Years Experience: ₹45000
# Graph should display:
# • Data points
# • Regression line


# 4. Why is KNN called a lazy learner?
# 5. What happens if K is too small?
# 6. What happens if K is too large?
# 7. Why does linear regression minimize squared error?
# 8. What is the difference between MSE and R2?
# 9. Why R2 cannot be greater than 1?
# 10. Can KNN be used for regression?

import numpy as np
import matplotlib.pyplot as plt 

def SimpleLinearRegression():
    
    border = "- " * 50
    # Dataset
        
    # Mean of X:
    # X̄ = sum(X_i) / n
    
    X = [1,2,3,4,5]
    
    # Mean of Y:
    # Ȳ = sum(Y_i) / n
    
    
    Y = [20000,25000,30000,35000,40000]
    
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
    
    plt.figure(figsize=(8,5))
    plt.scatter(X_new,Y_new)
    plt.xlabel("Year Of Experience")
    plt.ylabel("Predicted salary ")
    plt.grid(True)
    plt.show()
    


def main():
    SimpleLinearRegression()

if __name__ == "__main__":
    main()
    