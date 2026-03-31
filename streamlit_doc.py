import streamlit as st
import pandas as pd

st.title("Stratup Dashboard")
st.header("I am learning streamlit")
st.subheader("Aman")

st.write("I am writing")

st.markdown('''
### My Favorite Move
- Race 3
- kick
- Mr. X
''')

st.code('''
def foo(x):
     return foo**2

y = foo(x)
''')

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
        'name':['Aman','Rajat','Shubham'],
        'marks':[50,60,70],
        'package':[12,23,45]
})

st.dataframe(df)

st.metric('Revenue','3L Rs','3%')

st.image('AmanSign.jpg')

st.sidebar.title("SideBar Title")

col1, col2, col3 = st.columns(3)

with col1:
        st.image("AmanSign.jpg")

with col2:
        st.image("AmanSign.jpg")     

with col3:
        st.image("AmanSign.jpg")           

st.error("Error")

st.success("Success")
st.info("Info")
st.warning("warning")

bar = st.progress(0)

for i in range(1,101):
        bar.progress(i)

email = st.text_input("Enter Email")
age = st.number_input("Enter Age")

# another part
email = st.text_input("Enter email")
password = st.text_input("Enter Password")

gender = st.selectbox("Select Gender",['male','female','other'])

btn =st.button("Login")

# if button cliked
if btn:
        if email == "kushwahaaman6103@gmail.com" and password == '1234':
                st.balloons()
                st.write(gender)

        else:
                st.error("Login failed")        

file = st.file_uploader('upload a csv file')

if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df.describe())