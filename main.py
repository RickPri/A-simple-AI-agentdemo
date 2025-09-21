from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.deepseek import DeepSeekProvider
from pydantic_ai import Agent
import os
import tools
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('DEEPSEEK_API_KEY')
model = OpenAIChatModel('deepseek-chat',
                        provider=DeepSeekProvider(api_key='sk-ae11155b03524ae88397360fc83caa5b'))

agent = Agent(model,
              tools= [tools.read_files,tools.list_files,tools.rename_files]
)

def main():
    while True :
        history = []
        user_input = input("Input:")
        resp = agent.run_sync(user_input,message_history=history)
        history = list(resp.all_messages())
        print(resp.output)

if __name__=="__main__":
    main()