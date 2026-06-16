import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
                .stApp{
                      background-color:#52AEFE !important;
                }
                .stApp div[data-testid="stColumn"]{
                   background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
                
                }


        </style>   """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp{
                      background-color:#EEF2FF !important;
                }
                


        </style>        
      

 
                     """,
                     unsafe_allow_html=True)














def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
               

                .block-container{
                        padding-top: 0.4rem !important;
                        padding-bottom: 0rem !important;
                        padding-left: 2rem !important;
                        padding-right: 2rem !important;

                        
                }
                 #MainMenu, footer , header{
                visibility:hidden;
                }

                h1 {
                font-family:'Climate Crisis', sans-serif !important;
                font-size:2.5rem !important;
                line-height:1.1 !important;
                margin:0rem !important;
                
                }
                
                h2 {
                font-family:'Climate Crisis', sans-serif !important;
                font-size:1.7rem !important;
                line-height:1.2 !important;
                margin:0rem !important;
                
                }
                h3,h4,p{
                font-family:'Outfit',sans-serif;
                }

                button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background:#EC4899 !important;
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition :transform 0.25s ease-in-out !important;
                }
                
                
                button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background:#2563EB !important;
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition :transform 0.25s ease-in-out !important;
                }
                
                
                button[kind="primary"]{
                border-radius: 1.5rem !important;
                background:#4F46E5 !important;
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition :transform 0.25s ease-in-out !important;
                }
                button{
                border-radius: 1.5rem !important;
                background:#4F46E5 !important;
                color:white !important;
                padding:10px 20px !important;
                border:none !important;
                transition :transform 0.25s ease-in-out !important;
                }

                button:hover{
                transform : scale(1.05) !important;
                }
                
                .stApp {
                overflow: hidden ! important;
            }


                


        </style>


               
      

 
                     """,
                     unsafe_allow_html=True)