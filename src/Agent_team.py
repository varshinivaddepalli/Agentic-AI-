from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
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


web_agent=Agent(

    name='Web Agent',
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources "],
    show_tool_calls=True,
    markdown=True
)

finance_agent=Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.1-8b-instant"),
    tools= [YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data.","if you don't know the company symbol, please use get_company_symbol tool"],
    # debug_mode=True
)


agent_team=Agent(
    
    team=[web_agent,finance_agent],
    model=Groq(id="deepseek-r1-distill-llama-70b"),
    instructions=["Always include sources","use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendation and share the latest news for TSLA.",stream=True)
# print(YFinanceTools.get_key_financial_ratios(self=YFinanceTools,symbol='NVDA'))