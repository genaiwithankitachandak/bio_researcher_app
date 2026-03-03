import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
from google import genai
from google.genai import types
from serpapi import GoogleSearch
import os
import json
from config import CONFIG
from prompts import INIT_PROMPT, CONTEXT_PROMPT, STEPS_PROMPT
import logging

logging.getLogger().setLevel(logging.INFO)

MODEL_ID = CONFIG.gemini_model
MED_MODEL_ID = CONFIG.med_gemini_model

class ChatMedLLM:
    def __init__(self):
        """
        Initializes the ChatLLM.
        """
        # Initialize Gemini model (replace with your Gemini model setup)

        vertexai.init(project=CONFIG.project_id, location=CONFIG.project_location)

        self.safety_settings = [
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=SafetySetting.HarmBlockThreshold.OFF
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=SafetySetting.HarmBlockThreshold.OFF
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=SafetySetting.HarmBlockThreshold.OFF
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=SafetySetting.HarmBlockThreshold.OFF
            ),
        ]

        self.generation_config = {
            "max_output_tokens": 8192,
            "temperature": 1,
            "top_p": 0.95,
            "response_mime_type": "application/json",
        }

        # tool = Tool.from_google_search_retrieval(grounding.GoogleSearchRetrieval())
        self.model = GenerativeModel(MED_MODEL_ID, system_instruction=None)

        self.chat = self.model.start_chat()


    def multiturn_generate_content(
        self,
        query: str,
        context: str=""
    ):

        if CONFIG.test:
            with open('sample_response.md', 'r') as f:
                markdown_content = f.read()
                # markdown_content = json.load(f)
            return markdown_content

        input_text = " ".join([INIT_PROMPT, CONTEXT_PROMPT, context, STEPS_PROMPT, query])
        logging.info(input_text)

        text_response = []
        responses = self.chat.send_message(
            input_text,
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
            stream=True
        )
        for chunk in responses:
            text_response.append(chunk.text)

        return "".join(text_response)

class ChatLLM:
    def __init__(self):
        """
        Initializes the ChatLLM.
        """
        # Initialize Gemini model (replace with your Gemini model setup)

        self.client = genai.Client(
            vertexai=True,
            project=CONFIG.project_id,
            location=CONFIG.project_location
        )

        self.tools = [
            types.Tool(google_search=types.GoogleSearch())
        ]

        self.generate_content_config = types.GenerateContentConfig(
            temperature = 1,
            top_p = 0.95,
            max_output_tokens = 8192,
            response_modalities = ["TEXT"],
            safety_settings = [
                types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="OFF"
                ),
                types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="OFF"
                ),
                types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="OFF"
                ),
                types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="OFF"
                )
            ],
            tools = self.tools
        )
        self.chat = self.client.chats.create(model=MODEL_ID, config=self.generate_content_config)


    def multiturn_generate_content(
        self,
        query: str,
        context: str="",
        uploaded_files=[]
    ):

        if CONFIG.test:
            with open('sample_response.md', 'r') as f:
                markdown_content = f.read()
                # markdown_content = json.load(f)
            return markdown_content
        refrence_docs = []
        for doc in uploaded_files:
            types.Part.from_bytes(
                data=base64.b64decode(doc),
                mime_type="application/pdf")

        input_text = " ".join([INIT_PROMPT, CONTEXT_PROMPT, context, STEPS_PROMPT, query])
        logging.info(input_text)

        contents = [
            types.Content(
                role="user",
                parts=refrence_docs+[types.Part.from_text(text=input_text)]
            ),
        ]

        text_response = []
        responses = self.chat.send_message_stream(
            input_text
        )

        for chunk in responses:
            text_response.append(chunk.text)

        return "".join(text_response)            

        for chunk in self.client.models.generate_content_stream(
            model = self.model,
            contents = contents,
            config = self.generate_content_config,
        ):
            text_response.append(chunk.text)

        return "".join(text_response)