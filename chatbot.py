from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel,Field
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

class Product(BaseModel):

    product_name : str = Field(description='This is the Product Name')
    tentative_price_in_usd : int = Field(description='This is the tentative Price of Product')

prompt = ChatPromptTemplate.from_messages([
    ('system',"You are an helpful assistant with deep knowledge in Sales . The user will give you some product information from which you should tell product name and it's tentative price in us with dollar sign"),
    ('human',"{input}")
])

st.title('Product Price Finder 🚀🚀')

options = ['deepseek-r1-distill-llama-70b','qwen-qwq-32b','llama-3.1-8b-instant']
choice = st.selectbox('Select The Model to predict :',options)

product_details = st.text_input('Enter the Prodcut details Below 🪫🪫')
button = st.button('Fetch Details')

if button and product_details and choice:
    model = ChatGroq(model=choice)
    structured_output = model.with_structured_output(Product)
    chain = prompt | structured_output
    result = chain.invoke({'input':product_details})
    st.write(f'The Product Name is : {result.product_name}')
    st.write(f'The Expected Price of Given product is around $ {result.tentative_price_in_usd}')