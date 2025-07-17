from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import gradio as gr

# --- RAG setup ---
embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/e5-base",
    encode_kwargs={"normalize_embeddings": True}
)
vectorstore = FAISS.load_local(
    "vectorstore_jupyterbook",
    embeddings=embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever()
llm = OllamaLLM(model="phi3")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# # Prompt templates
# rewrite_template = PromptTemplate(
#     input_variables=["query"],
#     template="""Rewrite the following query to be more specific and complete for document search:
# Query: "{query}"
# Rewritten Query:"""
# )
# rewrite_chain = rewrite_template | llm | StrOutputParser()

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

# Utility
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def answer_question(query: str) -> str:
    # Optional: rewritten = rewrite_chain.invoke({"query": query})
    rewritten = query  # Use directly for now
    docs = retriever.get_relevant_documents(rewritten)
    context = format_docs(docs)
    final_chain = final_prompt | llm | StrOutputParser()
    answer = final_chain.invoke({"context": context, "query": rewritten})
    return answer

# --- FastAPI backend for frontend use ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or "*" for testing
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query(req: QueryRequest):
    answer = answer_question(req.question)
    return {"answer": answer}