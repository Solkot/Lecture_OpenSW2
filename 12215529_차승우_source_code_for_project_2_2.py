# 2-2 해당 시즌 연봉 예측
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline

def sort_dataset(dataset_df):
	#TODO: Implement this function
  dataset_df_copy1 = dataset_df.copy().sort_values(by = 'year', ascending = True)
  return dataset_df_copy1

def split_dataset(dataset_df):
	#TODO: Implement this function
	dataset_df_copy2 = dataset_df.copy()
	dataset_df_copy2['salary'] *= 0.001

	return train_test_split(dataset_df_copy2.drop(columns=['salary']), dataset_df_copy2['salary'], test_size=0.1014, shuffle = False)
	#1718행의 기준에 맞게 test_size=0.1014를 조정하여 진행하였습니다.
def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	dataset_df_copy3 = dataset_df.copy()
	dataset_df_copy3_numerical = dataset_df_copy3[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]
	return dataset_df_copy3_numerical

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
	dt_reg = DecisionTreeRegressor()
	dt_reg.fit(X_train, Y_train)
	return dt_reg.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	rf_reg = RandomForestRegressor()
	rf_reg.fit(X_train, Y_train)
	return rf_reg.predict(X_test)
#각각의 함수에 따른 회귀를 진행합니다.
def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	svm_pipe = make_pipeline(
        StandardScaler(),
        SVR() #Pipeline 구조 및 정ㄱ규화 과정을 통해 정확도를 증가시킵니다.
    )
	svm_pipe.fit(X_train, Y_train)
	return svm_pipe.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	return np.sqrt(np.mean((labels - predictions)**2))
	#최소제곱법을 통해 모델의 RMSE를 구해서 진행합니다.

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('/content/drive/MyDrive/2019_kbo_for_kaggle_v2.csv')
  #주소의 경우 변경이 필요합니다.

	sorted_df = sort_dataset(data_df)
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)

	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))
