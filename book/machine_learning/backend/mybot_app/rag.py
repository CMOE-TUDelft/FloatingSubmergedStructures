from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path

# Initialize once (on server start)
embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/e5-base",
    encode_kwargs={"normalize_embeddings": True}
)
vectorstore_loc = Path(__file__).parent.parent.parent / "vectorstore_jupyterbook"
vectorstore = FAISS.load_local(vectorstore_loc, embeddings=embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()
llm = OllamaLLM(model="phi3")
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
final_chain = final_prompt | llm | StrOutputParser()

def answer_question(query: str) -> str:
    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join(doc.page_content for doc in docs)
    answer = final_chain.invoke({"context": context, "query": query})
    return answer
