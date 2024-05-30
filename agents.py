from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
import os

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI(model="gpt-3.5-turbo")

##Genric prompt from hubs
from langchain import hub
prompt=hub.pull("hwchase17/openai-functions-agent")
prompt.messages



tools=[wiki]
#search by order

##Agents 
from langchain.agents import create_openai_tools_agent
agent=create_openai_tools_agent(llm,tools,prompt)

from langchain.agents import AgentExecutor
agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True)
agent_executor


resposne=agent_executor.invoke({"input":"Tell me about AI"})
print(resposne['output'])
