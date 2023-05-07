# coder_AI

## Installation
```bash
pip install git+https://github.com/saltchicken/coder_AI.git
pip install langchain
```
This project requires and OpenAI subscription. You can export the OPENAI_API_KEY environment key yourself or place it in a .env file which will be handled by load_dotenv()
## Usage

```python
load_dotenv()
TOKEN = os.getenv('OPENAI_API_KEY')
result = generate_code("Python", "Write a replacement for virtual audio cable in python using pyaudio", TOKEN)
print(result['code'])
print(result['filename'].strip())
```
