import os
from pathlib import Path

from dotenv import load_dotenv

# override=True 确保.env文件优先
# 显式指定 .env 路径（相对本文件所在目录），避免依赖运行目录导致找不到
load_dotenv(Path(__file__).parent / '.env', override=True)

# 从环境变量读取配置
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
