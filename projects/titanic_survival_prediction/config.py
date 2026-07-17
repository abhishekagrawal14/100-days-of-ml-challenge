import os 


# humlog base dir find kar le rhe hai jiske or phir waha humlog titanic_pipeline daal rhe hai taki deployment ke time 
# kahi se bhi stramlit cloud run ho usko hamesha file mile otherwise sirf load karne se file not found ka error aa sakta hai

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ALGO_PATH = os.path.join(BASE_DIR , 'models' , 'titanic_pipeline.pkl')
