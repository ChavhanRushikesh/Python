#Ass-43

# | Sr No | Weather  | Temperature | Play |
# | ----- | -------- | ----------- | ---- |
# | 1     | Sunny    | Hot         | No   |
# | 2     | Sunny    | Hot         | No   |
# | 3     | Overcast | Hot         | Yes  |
# | 4     | Rainy    | Mild        | Yes  |
# | 5     | Rainy    | Cool        | Yes  |
# | 6     | Rainy    | Cool        | No   |
# | 7     | Overcast | Cool        | Yes  |
# | 8     | Sunny    | Mild        | No   |
# | 9     | Sunny    | Cool        | Yes  |
# | 10    | Rainy    | Mild        | Yes  |


# According to above dataset there are two features as
    # 1.Wether
    # 2.Temperature
# We have two labels as
    # 1.Yes
    # 2.No
# There are three types of different entries under Wether as
    # 1.Sunny
    # 2.Overcast
    # 3.Rainy
# There are three types of different entries under Temperature as
    # 1.Hot
    # 2.Cold
    # 3.Mild
    
    
#     Design machine learning application which follows below steps as
# Step 1:
# Get Data
    # Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.
    
# Step 2:
# Clean, Prepare and Manipulate data
    # As we want to use the above data into machine learning application we have prepare
    # that in the format which is accepted by the algorithms.
    # As our dataset contains two features as Wether and Temperature. We have to replace
    # each string field into numeric constants by using LabelEncoder from processing module
    # of sklearn.
    
# Step 3:
# Train Data
    # Now we want to train our data for that we have to select the Machine learning algorithm.
    # For that we select K Nearest Neighbor algorithm.
    # use fit method for training purpose. For training use whole dataset.
    
# Step 4:
# Test Data
    # After successful training now we can test our trained data by passing some value of
    # wether and temperature.
    # As we are using KNN algorithm use value of K as 3.
    # After providing the values check the result and display on screen.
    # Result may be Yes or No.
    
    
# Step 5:
# Calculate Accuracy
    # Write one function as CheckAccuracy() which calculate the accuracy of our algorithm.
    # For calculating the accuracy divide the dataset into two equal parts as Training data and
    # Testing data.
    # Calculate Accuracy by changing value of K.
    
    
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def CheckAccuracy(X, Y):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.5, random_state=42
    )

    print("\nAccuracy for different K values:\n")

    for k in range(1,11):

        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        acc = accuracy_score(Y_test, Y_pred)
        print("K =",k,"Accuracy =",acc)

def KNearestNeighborAlgorithm():
    Border = "- "* 50
    print("\n")
    print(Border)
    
    #-------------------------------------------------------------------------
    # Step 1 :  Load Dataset from csv 
    #-------------------------------------------------------------------------
    df = pd.read_csv("../DataSets/PlayPredictor.csv")
    print(Border)
    print("Step 1 : Load  Dataset from csv file ")
    print(Border)
    
    print("Data From CSV :", df.head())
    
    #--------------------------------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    #--------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data ")
    print(Border)
    
    df.dropna(inplace=True)
    
    print("Total Record : ",df.shape[0])
    print("Total column : ", df.shape[1])
    
    print(Border)
    
    #--------------------------------------------------------------------------
    # Step 3 : Separate teh data 
    #--------------------------------------------------------------------------
    print(Border)
    print("Step 3 : Separate the data  ")
    print(Border)
 
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"],inplace=True)
    print(df.shape)
    
    
    le_whether = LabelEncoder() 
    le_temperature = LabelEncoder()
    le_play= LabelEncoder()
    
    df["Whether"] = le_whether.fit_transform(df['Whether']) # type: ignore
    df["Temperature"] = le_temperature.fit_transform(df['Temperature']) # type: ignore
    df["Play"] = le_play.fit_transform(df['Play']) # type: ignore
    
    X = df[["Whether","Temperature"]]
    Y = df["Play"]
    
    model = KNeighborsClassifier(n_neighbors=3)
    
    model.fit(X,Y)
    
    print(Border)
    
    test_w = "Sunny"
    test_t = "Cool"
    whether = le_whether.transform([test_w])[0] # type: ignore
    tempe = le_temperature.transform([test_t])[0] # type: ignore
    
    
    test_data = pd.DataFrame([[whether, tempe]], columns=["Whether","Temperature"])
    result = model.predict(test_data)

    output = le_play.inverse_transform(result) # reverse teh encode valuse in original values 
    
    print("Whether :",test_w)
    print("Temperature :",test_t)
    print("Play Prediction :",output[0])
    
    CheckAccuracy(X,Y)
    
    
def main():
    KNearestNeighborAlgorithm()

if __name__ == "__main__":
    main()