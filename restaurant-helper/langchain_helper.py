from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

llm = OpenAI(temperature = 0.7)

def get_resturant_name_and_menu(cuisine):
    #Chain for restaurant name
    name_prompt_template = PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant having {cuisine} food. Can you suggest a savvy name for it?'
    )

    name_chain = LLMChain(llm=llm, prompt=name_prompt_template, output_key ='restaurant_name')

    #Chain for menu
    menu_items_prompt_template = PromptTemplate(
        input_variables=['cuisine', 'restaurant_name'],
        template='I want to open a restaurant having {cuisine} food. Can you suggest deconstructed menu items for it?'
    )

    items_chain = LLMChain(llm=llm, prompt=menu_items_prompt_template, output_key ='menu_items')

    #run these chains sequentially
    chain = SequentialChain(
        chains =[name_chain, items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response