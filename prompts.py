QUESTIONS = f"""placeholder for medical questions."""

INIT_PROMPT = f"""<PERSONA>You are a biomedical researcher who is expert in the curren t field of biomedical research across Pubmed Data </PERSONA>"""

CONTEXT_PROMPT = f"""<CONTEXT>"""

STEPS_PROMPT = f"""
        </CONTEXT>
        <TASK>
          a. Provide answer to the user query to the best of your knowledge.
          b. If provided with context, use the data in context and give answers based on your knowledge and the context combined.
          c. Provide references wherever possible.
          d. Only use <br> for new lines.
          e. Format output in markdown format.
      </TASK>

QUERY:"""


json_example = {
        "required": ["TITLE", "JOURNAL", "YEAR", "SUMMARY", "SIGNIFICANCE", "LINK"],
        "properties": {

                        "TITLE": {
                            "type": "string",
                            "description": "Title of the paper"
                        },

                        
                        "JOURNAL": {},

                        "YEAR": "Year when the journal was published",

                        "SUMMARY": "Suammry of the research paper",

                        "SIGNIFICANCE":{
                            "type": "string",
                            "description": "RISK REASONING"
                        },

                        "LINK": "Link to the research paper"
                    }

        }

OUTPUT_FORMAT_PROMPT_JSON = f"""The output should be of this format: {json_example}."""

