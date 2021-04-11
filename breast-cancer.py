import pandas as pd
import numpy as np
import pickle
import streamlit as st


# loading in the model to predict on the data
pickle_in = open('clf_cancer.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
	return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(mean_radius, mean_texture, mean_perimeter, mean_area,mean_smoothness):
    
    prediction = classifier.predict([[mean_radius, mean_texture, mean_perimeter, mean_area,mean_smoothness]])
    print(prediction)
    if prediction==1:
        return 'The patient is suffering from breast cancer'
    else:
        return 'The patient is not suffering from breast cancer'
	

# this is the main function in which we define our webpage
def main():
        
	# giving the webpage a title
	
        st.title("Breast Cancer Prediction")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
        html_temp = """
	<div style ="background-color:red;padding:13px">
	<h1 style ="color:white;text-align:center;">Streamlit Based Breast Cancer Prediction ML App </h1>
	</div>
	"""
       

        
	# this line allows us to display the front end aspects we have
	# defined in the above code
        st.markdown(html_temp, unsafe_allow_html = True)
           ###
        st.markdown(
            """
            <style>
            .reportview-container {
            background: url("http://www.gogreen.org/portals/0/images/health-topic-image.jpg")
            }
            .sidebar .sidebar-content {
            background: url("https://thumbs.dreamstime.com/b/red-squared-background-abstract-mosaic-illustration-vector-61893072.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
        )
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
        
        mean_radius = st.text_input("Mean Radius", "Type Here")
        mean_texture = st.text_input("Mean Texture", "Type Here")
        mean_perimeter = st.text_input("Mean Perimeter", "Type Here")
        mean_area=st.text_input("Mean Area", "Type Here")
        mean_smoothness=st.text_input("Mean Smoothness", "Type Here")
        result =""
	
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
        if st.button("Predict"):
        	result = prediction(mean_radius, mean_texture, mean_perimeter, mean_area,mean_smoothness)
        st.success('{}'.format(result))

if __name__=='__main__':
        main()
