
import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home
from src.components.footer import footer_home
def home_screen():
    
    header_home()
    style_background_home()
    style_base_layout()



    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.header("I'm Teacher")
        st.image("https://static.vecteezy.com/system/resources/thumbnails/052/644/668/small/cartoon-style-female-teacher-for-educational-materials-on-transparent-background-png.png",width=145)
        if st.button('Teacher Portal',type="primary",icon=":material/arrow_outward:", icon_position="right"):
            st.session_state['login_type']='teacher'
            st.rerun()
    with col2:
        st.header("I'm Student")
        st.image("https://static.vecteezy.com/system/resources/thumbnails/045/546/274/small/boy-wear-graduation-hat-and-holding-book-3d-free-png.png", width=145)
        if st.button('Student Portal', type="primary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state['login_type']='student'
            st.rerun()
    footer_home()
