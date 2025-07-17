from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
import gradio as gr
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# Set up QA chain
embedding_model = HuggingFaceEmbeddings(model_name="intfloat/e5-base", encode_kwargs={"normalize_embeddings": True})

vectorstore = FAISS.load_local("vectorstore_jupyterbook", embeddings=embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()
llm = OllamaLLM(model="phi3")  # Use the Ollama model you downloaded
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Rewrite query template
rewrite_template = PromptTemplate(
    input_variables=["query"],
    template="""
Rewrite the following query to be more specific and complete for document search:
Query: "{query}"
Rewritten Query:"""
)
rewrite_chain = rewrite_template | llm | StrOutputParser()

# Final prompt template
final_prompt = PromptTemplate(
    input_variables=["context", "query"],
    template="""
You are a helpful assistant. Based on the context provided, answer the question clearly and accurately.

Context:
{context}

Question:
{query}

Answer:
"""
)

query_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
Question:
{query}

Answer:
"""
)


# Helper to extract content from docs
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Full answer pipeline
def answer_question(query):
    # # Step 1: Rewrite the query
    # rewritten = rewrite_chain.invoke({"query": query})
    # print(f"\n🔁 Rewritten Query:\n{rewritten.strip()}")
    rewritten = f"query: {query.strip()}"
    # Step 2: Retrieve relevant documents
    docs = retriever.get_relevant_documents(rewritten)
    print("\n📚 Retrieved Chunks:")
    for i, doc in enumerate(docs):
        print(f"\n--- Chunk {i+1} ---")
        print(doc.page_content)

    # Step 3: Feed query + context into the LLM
    context = format_docs(docs)
    final_chain = final_prompt | llm | StrOutputParser()
    return final_chain.invoke({"context": context, "query": rewritten})


gr.Interface(fn=answer_question, inputs="text", outputs="text", title="Ask My Markdown").launch() # share=True To host online