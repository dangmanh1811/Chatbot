from chatbot.model import get_response
contents = []
while True:
	prompt = input("Enter your prompt: ")
	
	content = {'role': 'user', 
				'parts': [{'text' : prompt}]}
	contents.append(content)
	response = get_response(contents)
	print(response)
	contents.append(
		{'role': 'assistant', 
				'parts': [{'text' : response}]})
