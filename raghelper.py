from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("OPENAI_API_KEY")
my_key_google = os.getenv("GEMINI_API_KEY")

llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-1.5-flash")

embeddings = OpenAIEmbeddings(api_key=my_key_openai)


# speaking with llm
def ask_gemini(prompt):
    ai_response = llm_gemini.invoke(prompt)
    return ai_response.content


# rag - video transcription
def rag_with_video_transcript(transcripted_docs, prompt):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )

    splitted_docs = text_splitter.split_documents(transcripted_docs)
    vector_store = FAISS.from_documents(splitted_docs, embeddings)
    retriever = vector_store.as_retriever()
    relevant_docs = retriever.get_relevant_documents(prompt)

    context_data = ""

    for doc in relevant_docs:
        context_data = context_data + " " + doc.page_content

    final_prompt = f"""I have a question: "{prompt}"
        To answer this question, you have access to the following information: {context_data}.
        Please use **only** the provided information to answer the question. Do not reference, assume, or rely on any external knowledge. 
        Your response must strictly adhere to the given context and remain fully aligned with it.   
        """

    ai_response_content = ask_gemini(final_prompt)
    return ai_response_content, relevant_docs

