import os
from dotenv import load_dotenv
from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.memory import SimpleMemory


def generate_code(LANGUAGE, GOAL, TOKEN):

    # Chain that computes code
    llm = OpenAI(temperature=.7, openai_api_key=TOKEN)
    template = """You are a programmer. Write me {language} code that {goal}. Return only code without an explaination.

    Language: {language}
    Goal: {goal}
    Code: This is the code:"""
    prompt_template = PromptTemplate(input_variables=["language", 'goal'], template=template)
    code_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="code")


    # Chain that computes the filename for given code
    llm = OpenAI(temperature=.7, openai_api_key=TOKEN)
    template = """You are a programmer. Given the code, it is your job to provide a filename. It should have the proper extension for {language}.

    Code:
    {code}
    Filename:"""
    prompt_template = PromptTemplate(input_variables=["code","language"], template=template)
    filename_chain = LLMChain(llm=llm, prompt=prompt_template, output_key="filename")

    # Build the overall chain
    overall_chain = SequentialChain(
        memory=SimpleMemory(memories={"language": LANGUAGE}),
        chains=[code_chain, filename_chain],
        input_variables=["goal"],
        output_variables=["code", "filename"],
        verbose=False)

    return overall_chain({"goal": GOAL})

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv('OPENAI_API_KEY')
    result = generate_code("Python", "Write a replacement for virtual audio cable in python using pyaudio", TOKEN)
    print(result['code'])
    print(result['filename'].strip())
