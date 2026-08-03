import pandas as pd
import json
from typing import Dict, Any


class LogicEngine:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columns = self.df.columns.tolist()
        self.dtypes = {col: str(dtype) for col, dtype in self.df.dtypes.items()}
        self.schema_info = ", ".join([f"{col} ({dtype})" for col, dtype in self.dtypes.items()])

    def get_prompt(self, query: str) -> str:
        sample = self.df.head(3).to_dict(orient='records')
        return f"""
        You are a data analysis expert. Translate the user's query into a JSON plan for Pandas operations.

        Dataset Schema: {self.schema_info}
        Sample Rows: {json.dumps(sample, default=str)}

        User Query: "{query}"

        Return ONLY valid JSON with this structure:
        {{
            "pandas_code": "A single line of pandas code that transforms the dataframe 'df' into 'result_df'. Use only standard pandas/numpy operations.",
            "chart_type": "one of: bar, line, scatter, pie, histogram",
            "x": "column name for x axis",
            "y": "column name for y axis (or null for histogram)",
            "title": "Clear descriptive title for the chart"
        }}

        Rules:
        - pandas_code must assign the result to result_df
        - Use actual column names from the schema above
        - Pick the most suitable chart_type based on the data and query
        - Do NOT use import statements or multi-line code

        Example:
        Query: "Top 10 rows by revenue"
        Output: {{
            "pandas_code": "result_df = df.nlargest(10, 'revenue')",
            "chart_type": "bar",
            "x": "product",
            "y": "revenue",
            "title": "Top 10 Products by Revenue"
        }}
        """

    def process_query(self, query: str, gemini_client) -> Dict[str, Any]:
        prompt = self.get_prompt(query)
        response = gemini_client(prompt)

        try:
            clean_response = response.strip().replace('```json', '').replace('```', '').strip()
            plan = json.loads(clean_response)
            return plan
        except Exception as e:
            return {"error": f"Failed to parse model output: {str(e)}", "raw": response}

    def execute_logic(self, plan: Dict[str, Any]) -> pd.DataFrame:
        import numpy as np
        local_vars = {'df': self.df, 'pd': pd, 'np': np}
        exec(plan['pandas_code'], {"__builtins__": __builtins__, "pd": pd, "np": np}, local_vars)
        return local_vars['result_df']
