import json
from phi.model.openai import OpenAIChat
from phi.agent.duckdb import DuckDbAgent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

data_analyst = DuckDbAgent(
    model=Groq(id="llama-3.3-70b-specdec"),
    semantic_model=json.dumps(
        {
            "tables": [
                {
                    "name": "Crop_recommendation",
                    "description": "Contains information about Crop.",
                    "path": "Crop_recommendation.csv",
                }
            ]
        }
    ),
    markdown=True,
)
data_analyst.print_response(
    "Show me a histogram of label. "
    "Choose an appropriate bucket size but share how you chose it. "
    "Show me the result as a pretty ascii diagram"
    "give me python code.",
    stream=True,
)