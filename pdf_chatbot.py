from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

pdf_path = "./MCU IDE.pdf"
persist_directory = "./storage"

print("Loading Document...")
loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
texts = text_splitter.split_documents(documents)
print("text chunks: {}".format(len(texts)))

print("Setting Embeddings and Saving to VectorDB...")
embeddings = OpenAIEmbeddings()
vectordb = Chroma.from_documents(documents=texts, 
                                 embedding=embeddings,
                                 persist_directory=persist_directory)
vectordb.persist()

retriever = vectordb.as_retriever()
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, verbose=True)

prompt_template = """
You are a marketing expert in software solutions. 
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.
Your product is {context}

Question: {question}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
chain_type_kwargs = {"prompt": PROMPT}
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, chain_type_kwargs=chain_type_kwargs)

while True:
    user_input = input("Enter a question: ")
    if user_input == "exit":
        break

    try:
        llm_response = qa({"query": user_input})
        print(llm_response["result"])
    except Exception as err:
        print('Exception occurred. Please try again', str(err))
