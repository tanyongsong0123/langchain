from langchain_deepseek import ChatDeepSeek

from env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL

# 创建DeepSeek LLM
deepseek_llm = ChatDeepSeek(
    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
    model="deepseek-chat",
)
