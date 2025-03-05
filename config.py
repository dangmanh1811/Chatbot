BACKGROUND_IMG_PATH = r"source\images\background.jpg"
LOGO_IMG_PATH = r"source\images\logoFptEdu.png"

# Gemini Configuration
MODEL_NAME = "gemini-2.0-flash"
# Params Documentation : https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters 

# Token sampling parameters 
TOP_P = 0.95 
TOP_K = 32
TEMPERATURE = 1.0

# Stopping parameters
MAX_OUTPUT_TOKENS = 8192

# Token penalization parameters
FREQUENCY_PENALTY = 0.0
PRESENCE_PENALTY = 0.0
