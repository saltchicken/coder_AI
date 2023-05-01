import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='coder_AI',
    version='0.0.1',
    author='John Eicher',
    author_email='john.eicher89@gmail.com',
    description='Testing installation of Package',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/saltchicken/coder_AI',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/saltchicken/coder_AI/issues"
    # },
    # license='MIT',
    py_modules=['coder_AI'],
    install_requires=['openai', 'langchain', 'dotenv'],
)