import pickle
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

def answer_question(question):

    pdf_reader = PdfReader("PL.pdf")
    
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=500,
        length_function=len
        )
    
    chunks = text_splitter.split_text(text=text)
    # # embeddings
    store_name = "PL"
    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
    else:
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", "wb") as f:
            pickle.dump(VectorStore, f)
            
    docs = VectorStore.similarity_search(question, k=2)
    
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model_name="text-davinci-003", temperature=0)

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that that can answer questions about subjects guides. 
        
        Answer the following question: {question}
        By searching the following information of the guide: {docs}
        
        Only use the factual information from the guide to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be short, and precise.
        """,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=question, docs=docs_page_content)
    response = response.replace("\n", "")
    return response
