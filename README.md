# Bio Researcher

**AI research assistant for biomedical literature.**

## Description
This application allows biomedical researchers to quickly and easily analyze a collection of research papers. Just chat out-of-the-box or simply upload your PDFs and start chatting with the app to explore the data and findings within them.

**Features:**

  * **Multiple PDF Upload:**  Upload numerous research papers simultaneously for analysis.
  * **AI-Powered Chat:** Interact with a powerful AI to ask questions and gain insights from the uploaded documents.
  * **Comparative Language Model Study:**  Utilizes both MedLM and Gemini 2.0 in a comparative study, showcasing the strengths of each model in understanding and analyzing biomedical literature.
  * **Vertex AI Integration:** Leverages Vertex AI chat APIs for a robust and responsive chat experience.

**How it works:**

1.  **Upload (Optional):**  Drag and drop or select multiple PDF files.
2.  **Process:** The app processes the PDFs, extracting key information and preparing them for analysis.
3.  **Chat:** Ask questions about the uploaded papers in natural language. The AI will provide summaries, comparisons, and insights based on the data.

**Technology Stack:**

  * **Streamlit:**  Frontend framework for building interactive web applications.
  * **MedLM:** A large language model specifically trained for medical research.
  * **Gemini 2.0:** Google's next-generation large language model with enhanced capabilities.
  * **Vertex AI SDK:** Google Cloud's machine learning platform, providing the chat API functionality.

**Installation:**

```
cd existing_repo
git remote add origin https://gitlab.com/google-cloud-ce/communities/NATT-AIML/genai-fsa/northam/expert_requests/wssv/bio_researcher_app.git
git branch -M main
git push -uf origin main
```

1.  Clone the repository: `git clone https://gitlab.com/google-cloud-ce/communities/NATT-AIML/genai-fsa/northam/expert_requests/wssv/bio_researcher_app.git`
2. `cd bio_researcher_app`
3.  Install dependencies: `pip install -r requirements.txt`
4.  Set up Vertex AI credentials: `gcloud auth application-default login`.
5. set project_id and location in `config.yaml`
5.  Run the app: `streamlit run app.py`

**Contributing:**

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.


**Disclaimer:**

This application is intended for research purposes and should not be used as a substitute for professional medical advice.

## Authors and acknowledgment
Ankita Chandak | ankitachandak@google.com

## License
For open source projects, say how it is licensed.

## Project status
Currently uses MedLM and Gemini2.0

Future work to incorporate comparison and evaluations on results.