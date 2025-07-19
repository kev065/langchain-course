from dotenv import load_dotenv

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


# def ingest_docs():
#     loader = ReadTheDocsLoader("langchain-docs/langchain.readthedocs.io/en/v0.1")

#     raw_documents = loader.load()
#     print(f"loaded {len(raw_documents)} documents")

#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
#     documents = text_splitter.split_documents(raw_documents)
#     for doc in documents:
#         new_url = doc.metadata["source"]
#         new_url = new_url.replace("langchain-docs", "https:/")
#         doc.metadata.update({"source": new_url})

#     print(f"Going to add {len(documents)} to Pinecone")
#     PineconeVectorStore.from_documents(
#         documents, embeddings, index_name="langchain-doc-index"
#     )
#     print("****Loading to vectorstore done ***")


# if __name__ == "__main__":
#     ingest_docs()

def ingest_docs() -> None:
    langchain_documents_base_urls = [
        "https://python.langchain.com/docs/integrations/chat/anthropic/",
        "https://python.langchain.com/docs/integrations/chat/mistralai/",
        "https://python.langchain.com/docs/integrations/chat/fireworks/",
        "https://python.langchain.com/docs/integrations/chat/openai/",
        "https://python.langchain.com/docs/integrations/chat/google_vertex_ai_palm/",
    ]
 
    for url in langchain_documents_base_urls:
        print(f"Loading documents from {url}")
        loader = FireCrawlLoader(
            url=url,
            mode="crawl",
            params={
                "crawlerOptions": {
                    "limit": 50},
                    "pageOptions": {
                        "onlyMainContent": True},
                        "wait_until_done": True,
                    },
                )
        docs = loader.load()
    print(f"Going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name="langchain-doc-index"
    )
    print("****Loading to vectorstore done ***")

if __name__ == "__main__":
    ingest_docs()
