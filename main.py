from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Load your document
loader = PyPDFLoader("dino.pdf")
documents = loader.load()

# Split it into smaller parts
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Turn text into searchable numbers (embeddings)
embedding_model = OpenAIEmbeddings()
vector_db = Chroma.from_documents(chunks, embedding_model)

# Connect the language model with the search system
retriever = vector_db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)

# Ask a question
question = "Tell me about gallimimus"
answer = qa_chain.run(question)
print(answer)
