import streamlit as st
x=st.radio('Are you a working Professional',options=['Yes','No'],index=1)

if(x=="Yes"):
    st.write("Yes he is an working professional")
else:
    st.write("No he is not an working professional")