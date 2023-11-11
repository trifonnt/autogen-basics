import autogen

# import OpenAI API key
config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# create the assistant agent
assistant = autogen.AssistantAgent(
    name="AI_Assistant"
    , llm_config={"config_list": config_list}
)

# Create the user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="UserProxy", code_execution_config={"work_dir": "generated-code"}
)

# Start the conversation
user_proxy.initiate_chat(
    assistant, message="""Write python code which invoke REST API at this url: https://app-01.trifon.org/api/contacts,
    using HTTP header "Authorization: Bearer " and value which must be read from environment varible "APP01_API_KEY"
    It must be POST request with JSON body like:
    {
        "guid": "contact:<value>",
        "displayName": "Contact <value>",
        "firstName": "",
        "lastName": "",
        "owner": {
            "id": 1001,
            "login": "spam.trifon+101@gmail.com"
        }
    }
    Replace <value> with integer value of 122.
    """
)
