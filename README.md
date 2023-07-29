# LangChainDemo

https://github.com/emarco177/ice_breaker

pdf langchain code: https://blog.nextideatech.com/chat-with-documents-using-langchain-gpt-4-python/

## PDF CHATBOT
 - problems: when asked "what track record do you have?", it starts to make things up. Not sure how to prevent it from making things up.

## Section 3
 - Chat Models
 - Chains
 - Agents
 - Tools

## TODOS 
 - Token Limitation Problem:
    - Stuffing
    - MapReduce
    - Refine
    - Map-Rerank

 - is breaking docs into vectors and storing sufficient?
 - how to store large documents --> token limitation problem


## Introduction to Vector Databases
 - Embeddings
 - Vector stores (Pinecone)
 - VectorDBQA Chain
 - Langchain document loaders
 - Langchain text splitters

### Langchain text splitters

Idea is to split a large document into chunks, and then only send relevant chunks (that we need to answer our question) to the LLM.

### Embeddings (and Vectors)

 - Words come in, an array of numbers representing data in a multi-dimentional space comes out (called vector).
 - The distance between 2 vectors represents some sort of semantic meaning. (In other words, similar words have short distance and vice versa).
 - It sounds very crazy, but people actually converted the entire wikipedia into embeddings
 - Generating text to embedding reqiures calling openAI's API

 ### CharacterTextSplitter
  - Fine-tune chunk_size and chunk_overlap based on our needs
  
### Vector Database
 - Pinecone

### Chunking strategy
 - recommend around 4-5 contexts (num of vector in original format from pinecone) (500 tokens per context)

### ConversationalRetrievalChain
 - Used to include Chat history
 - However, not feasible if chat history too long (will provide fix later)
 - Under the hood, just adds prompt engineering

## Code Interpreter
 - code interpreter is actually an agent built on top of ChatGPT4 that is able to write code, and execute and output code execution.


## Handling token limitation problem

 - Token Limit includes our prompt and our response
 - Solutions
   - Stuffing
   - Map Reduce
   - Refine (just processing things one by one)

## Memory
 - LLMs are stateless, so you pretty much have to feed it chat history for it to remember.
 - Several ways:
    - Feed entire chat history (but may exceed token limit)
    - Feed last n chat history
    - Feed a summarized version of chat history
    - Feed a summarized version of chat history + last n chat history
    - store chat history in vector db and fetch it based on prompt (based will have slow response time)
