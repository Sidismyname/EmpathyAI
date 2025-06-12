from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_groq import ChatGroq
api_key1="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"
llm = ChatGroq(groq_api_key=api_key1, model_name="llama-3.3-70b-versatile", temperature=0.6)

system_msg_template = SystemMessagePromptTemplate.from_template(template="""
You are EmpathyAI, a warm and friendly mental health companion who genuinely cares about the emotional well-being of others. 
Your goal is to engage in thoughtful, empathetic conversations with elderly individuals to help manage loneliness by discussing 
topics related to mental health. Focus on emotional support, mindfulness, self-care routines, positive affirmations, and coping strategies. 
Stay positive, patient, and compassionate. Avoid discussing topics outside of mental health and emotional well-being.
Limit yourself to 100 words.""")

human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")
buffer_memory = ConversationBufferWindowMemory(k=2, return_messages=True)
prompt_template = ChatPromptTemplate.from_messages([
    system_msg_template,
    MessagesPlaceholder(variable_name="history"),
    human_msg_template
])

conversation = ConversationChain(
    memory=buffer_memory,
    prompt=prompt_template,
    llm=llm,
    verbose=True
)

def generate_response(user_input):
    return conversation.predict(input=user_input)
