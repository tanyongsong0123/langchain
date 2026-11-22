import asyncio
from email import header

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

from base_llm.my_llm import deepseek_llm

# 获取 JWT Token
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJteV9hZ2VudCIsImlzcyI6Im15X2NvbXBhbnlfYXV0aF9zZXJ2ZXIiLCJpYXQiOjE3OTUzNDUzMTksImV4cCI6MTc5NTM0ODkxOSwiYXVkIjoiaW50ZXJuYWxfbWNwX3NlcnZlciJ9.EpYz3UMploCVgtE2HCHySmXKfRLGNEAncoqczdePtRsWl1CTpBda0FTDHEOJ-59_xgrgcX8EVX4PZ9Ug0ECbWRY_iz3DZ7nZq4KNJKIAg4lNn8-tyt9yvEmEkBKhV2umHzGbqJeD1kp-yfUsk7wdd55iegzsu4Wd91uj_K00ZmVZyMoSixD7lBfSKNmpzOwD2hRHvAMRpwYi8oWkPhctrZop90_a0J5zp79D3Yk92mWt5jFlilA6FpXmxm2QQRF7rQw7jvzhXMylgLvTFw8kcdftBBl5BRflG8YgUxO2Qj5AhyVeadDccV6pPbqrNVnLj3GzuscXdCwuwSvLCz9QAg"


async def main():
    # 创建client
    client = MultiServerMCPClient(
        {
            "internal_mcp_server": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",
                # 将token添加到headers中
                "headers": {
                    "Authorization": "Bearer " + token
                }
            }
        }
    )

    tools = await client.get_tools()

    agent = create_agent(
        model=deepseek_llm,
        tools=tools,
    )

    result1 = await agent.ainvoke({"messages": [{"role": "user", "content": "查询一下E002员工信息"}]})
    print(result1["messages"][-1].content)

    result2 = await agent.ainvoke({"messages": [{"role": "user", "content": "查询一下财务部的预算"}]})
    print(result2["messages"][-1].content)


if __name__ == '__main__':
    asyncio.run(main())
