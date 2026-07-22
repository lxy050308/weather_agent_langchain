"""
RAG检索模块

作用：

用户问题
 ↓
向量搜索
 ↓
返回相关知识
"""


import os


# ======================
# 向量数据库路径
# ======================

VECTOR_PATH = "./rag/vector_db"

# 懒加载
_vector_db = None
_rag_available = True
_rag_error = None


def _get_vector_db():
    global _vector_db, _rag_available, _rag_error
    if _vector_db is None and _rag_available:
        try:
            from langchain_community.embeddings import HuggingFaceEmbeddings
            from langchain_community.vectorstores import Chroma

            embedding_model = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )

            _vector_db = Chroma(
                persist_directory=VECTOR_PATH,
                embedding_function=embedding_model
            )
        except Exception as e:
            _rag_available = False
            _rag_error = str(e)

    return _vector_db


# ======================
# 查询知识库
# ======================


def search_environment_rule(query: str):
    """
    根据问题检索环境知识
    """
    global _rag_available, _rag_error
    if not _rag_available:
        return f"[知识库暂时不可用: {_rag_error}]"

    vector_db = _get_vector_db()
    if vector_db is None:
        return "[知识库暂时不可用]"

    results = vector_db.similarity_search(query, k=3)

    knowledge = ""

    for doc in results:
        knowledge += (doc.page_content + "\n")

    return knowledge






# 测试

if __name__=="__main__":


    result=search_environment_rule(

        "PM2.5超过150适合运动吗"

    )


    print(result)
