import streamlit as st
from chatbot.model import get_response
import config

def show_chatbot():
	st.subheader(f"Welcome back {st.session_state.username}")
	with st.sidebar:
		st.subheader("Token sampling parameters ")
		config.TEMPERATURE = st.slider("temperature", min_value=0.0, max_value=2.0, value=config.TEMPERATURE)
		config.TOP_P = st.slider("top_p", min_value=0.0, max_value=1.0, value=config.TOP_P)
		config.TOP_K = st.slider("top_k", min_value=1, max_value=40, value=config.TOP_K)
		
		st.subheader("Stopping parameters")
		config.MAX_OUTPUT_TOKENS = st.number_input("max_output_tokens", max_value=8192, value=config.MAX_OUTPUT_TOKENS)
		
		st.subheader("Token penalization parameters")
		config.FREQUENCY_PENALTY = st.slider("frequency penalty", min_value=-2.0, max_value=2.0, value=config.FREQUENCY_PENALTY)
		config.PRESENCE_PENALTY = st.slider("presence penalty", min_value=-2.0, max_value=2.0, value=config.PRESENCE_PENALTY)

		if st.button("👋Log Out"):
			st.session_state.logged_in = False  # Đặt lại trạng thái đăng nhập
			st.session_state.username = ""

			if 'chat_history' in st.session_state:
				st.session_state['chat_history'] = []
				st.experimental_rerun()
				
	# Store LLM generated responses
	if "messages" not in st.session_state.keys():
		st.session_state.messages = [
			{'role': "assistant",
			 'parts': [{'text' : "How may I help you?"}]
			}]
		
	# Display chat messages
	for message in st.session_state.messages:
		with st.chat_message(message["role"]):
			st.write(message["parts"][0]['text'])
	
	# Used-provided prompt
	if prompt := st.chat_input():
		st.session_state.messages.append({
			'role': 'user',
			'parts': [{'text' : prompt}]
			})
		with st.chat_message('user'):	
			st.write(prompt)
			
	# Generate a new response if last message is not from assistant
	if st.session_state.messages[-1]['role'] != 'assistant':
		with st.chat_message("assistant"):
			with st.spinner("Thinking..."):
				response = get_response(st.session_state.messages)
				st.write(response)
            
			message = {'role': "assistant", 
			  			'parts': [{'text' : response}]
					  }
			st.session_state.messages.append(message)
