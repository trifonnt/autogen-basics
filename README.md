### AutoGen Basics


**Steps**
1. Create a new project folder.
2. Create a new virtual environment `python -m venv .venv`.
3. Activate the venv `source .venv/bin/activate`
4. Install packages with `pip install pyautogen`.
5. Create the OAI_CONFIG_LIST file.
6. Go to https://platform.openai.com/account/api-keys to create the new OpenAI API key.
7. Paste the generated API key and paste it in the OAI_CONFIG_LIST
8. Create the basic.py file.
9. Import AutoGen
10. Create a config list
11. Create the Assistant Agent
12. Create the User Proxy Agent
13. Initiate Chat.
14. Build Docker image `docker build -t autogen-basic .`
15. Start new docker container with the new image `docker run -it --rm -v ./logs:/var/log -v ./generated-code:/app/generated-code -v ./OAI_CONFIG_LIST:/app/OAI_CONFIG_LIST autogen-basic`
