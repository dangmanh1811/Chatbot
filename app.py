from frontend.pages import chatbot_page, login
from frontend.components import add_background

import streamlit as st

from config import *
import sys

if __name__ == '__main__':
	
	if 'logged_in' not in st.session_state:
		st.session_state.logged_in = False
		
	if 'username' not in st.session_state:
		st.session_state.username = ""
		
	st.set_page_config(layout="wide")
	add_background()
	st.image(LOGO_IMG_PATH, width=200)
	
	if st.session_state.logged_in:
		chatbot_page.show_chatbot()
	else:
		st.sidebar.title("Project Chatbot (DAP391m)")
		menu = ["Login", "Sign Up"]
		choice = st.sidebar.radio("Select Option", menu)
		if choice == "Login":
			login.show_login_page()
		elif choice == "Sign Up":
			login.show_register_page()
			