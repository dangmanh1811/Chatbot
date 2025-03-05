from frontend.components import centered_subheader, centered_title
import streamlit as st

from backend.auth import add_user, check_login

# Hàm hiển thị trang đăng ký
def show_register_page():
	centered_subheader("Account Register")
	
	new_user = st.text_input("Username", key='register_username')
	new_password = st.text_input("Password", type='password', key='register_password')
	
	if st.button("Register"):
		flag, message = add_user(new_user, new_password)
		if flag:
			st.success('✅' + message)
		else:
			st.error('⚠️' + message)

# Show Login page
def show_login_page():
	centered_subheader("Login")

	username = st.text_input("Username", key='login_username')
	password = st.text_input("Password", type="password", key='login_password')

	if st.button("Login"):
		flag, message = check_login(username, password)
		if flag:
			st.session_state.logged_in = True #  To note that successfully login
			st.session_state.username = username
			st.success('✅' + message)
			st.rerun()
		else:
			st.error('⚠️' + message)
				