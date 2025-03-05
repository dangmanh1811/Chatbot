import bcrypt
from backend.database import users_collection

def add_user(username, password):
	flag = False
	message = None
	if username == '' or password == '':
		message = 'Please fill in all required fields.'
		
	elif users_collection.find_one({"usename": username}):
		message = f'{username} is already registered.'

	else:
		
		# Hash password
		hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		
		# Add user into database
		user_data = {
			"username": username,
			"password": hashed_password
			}
		result = users_collection.insert_one(user_data)
		message = "Registration successful! Please log in."
		flag = True
		
	return flag, message
	
def check_login(username, password):
	flag = False
	message = None
	
	if username == '' or password == '':
		message = 'Please enter both username and password.'
	else:	
		user = users_collection.find_one({"username": username})
		if user:
			if bcrypt.checkpw(password.encode('utf-8'), user['password']):
				flag = True
				message = f"Login successful! Welcome back {username}."
			else:
				message = "Incorrect password."
		else:
			message = f"{username} not found."
	
	return flag, message