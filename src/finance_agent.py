from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()


def get_company_symbol(company:str)-> str:
    '''use this fuction to get the symbol for a company.

    Args:
        company (str): The name of the comapny.

    Returns: 
        str : the symbol for the company.
    '''
    company=company.lower()
    symbols= {
        "infosys":"INFY",
        "tesla":"TSLA",
        "apple":"AAPL",
        "microsoft":"MSFT",
        "google":"GOOGL",
    }
    return symbols.get(company,"Unknown")


agent=Agent(

    model=Groq(id="llama-3.3-70b-versatile"),
    tools= [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data.","if you don't know the company symbol, please use get_company_symbol tool"],
    debug_mode=True
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA.")
# agent.print_response("Summarize and compare analyst recommendations and fundamentals for Tesla and Google.") 