from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import gradio as gr


# Set up QA chain
model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_model = HuggingFaceEmbeddings(model_name=model_name)

vectorstore = FAISS.load_local("vectorstore_jupyterbook", embeddings=embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever()
llm = Ollama(model="phi3") # Use the Ollama model you downloaded
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# # Test which chunks are retrieved for a given query
# # Fetch relevant chunks for the query
# docs = retriever.get_relevant_documents("Whom are we acknowledging")
#
# # Print the content of each retrieved chunk
# for i, doc in enumerate(docs):
#     print(f"\n--- Chunk {i+1} ---")
#     print(doc.page_content)


def answer_question(query):  # Gradio interface
    return qa.run(query)

gr.Interface(fn=answer_question, inputs="text", outputs="text", title="Ask My Markdown").launch() # share=True To host online