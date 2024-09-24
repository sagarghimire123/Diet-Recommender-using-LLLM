
#3 import necessary libraries
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain.chains import LLMChain
from langchain.llms import OpenAI
# Import necessary libraries
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client with your API key
llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Define the prompt template for getting the diet plan
diet_prompt = PromptTemplate(
    input_variables=["meal", "height", "weight", "goal", "sex"],
    template="I want you to recommend a diet plan based on my meal preference: {meal}, height: {height}, weight: {weight}, goal: {goal}, and sex: {sex}. Also, suggest some healthy recipes as my goal is to lose weight."
)

# Create the diet chain
diet_chain = LLMChain(llm=llm, prompt=diet_prompt)

# Get user inputs
meal = input("Enter your meal preference (e.g., vegetarian, non-vegetarian): ")
height = input("Enter your height (e.g., 175 cm): ")
weight = input("Enter your weight (e.g., 70 kg): ")
goal = input("Enter your goal (e.g., lose weight): ")
sex = input("Enter your sex (e.g., female, male): ")

# Prepare the input data
input_data = {
    "meal": meal,
    "height": height,
    "weight": weight,
    "goal": goal,
    "sex": sex
}

# Invoke the chain with the input data
response = diet_chain.invoke(input_data)

# Print the response
print(response)
