from fastmcp import FastMCP
from fastmcp.server.auth import JWTVerifier

# 1. 传入公钥
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp05a1pHZFZIZvGvzVSj7
Cboiifc+8F3Twl/l/XWbOz7EcdUciP8mCT/ePf8XKS8pSKm6mqZqNdwUrixa/LNe
Q+u9vc8Jp4Um6FbxSfcKX9NAq3u9cJpVaZVZ74JerP+QXcNkvMBlQ023WBGBvmNc
Cef4/xLN/Pa1zNyqlSB4UX9Y6UH9Q7j3BhfIiH32djBl0kWsBzUDiqr/9ziPIeuF
t+tif+0Owhicl41uP2AieXYCSXCKw8tjeQE5jnpY4RaSoaxGyY8BVCZUQC+OiKTc
go4CwxADdbunL7ltxHVgDFVrgElj5O0hcDTGA/R3/Qs9ddUFInwBheu7ySJxWPmD
FQIDAQAB
-----END PUBLIC KEY-----"""

# 2. Mcp Server 使用 公钥验证 JWT Token
auth = JWTVerifier(
    public_key=PUBLIC_KEY,
    issuer="my_company_auth_server",
    audience="internal_mcp_server",
    algorithm="RS256"
)

# 3. 创建带有认证的MCP Server
mcp = FastMCP("internal_mcp_server", auth=auth)

# 模拟数据
EMPLOYEE_DB = {
    "E001": {"name": "张三", "department": "技术部", "position": "高级工程师"},
    "E002": {"name": "李四", "department": "财务部", "position": "财务经理"},
    "E003": {"name": "王五", "department": "市场部", "position": "市场总监"},
}

BUDGET_DB = {
    "技术部": {"total": 5000000, "used": 3200000, "remaining": 1800000},
    "财务部": {"total": 1500000, "used": 900000, "remaining": 600000},
    "市场部": {"total": 3000000, "used": 2100000, "remaining": 900000},
}


# 定义工具
@mcp.tool()
def query_employee(employee_id: str):
    """查询员工信息"""
    employee = EMPLOYEE_DB.get(employee_id)
    if not employee:
        return f"员工 {employee_id} 不存在"
    return f"员工信息: 姓名={employee['name']}，部门={employee['department']}，岗位={employee['position']}"


@mcp.tool()
def query_department_budget(department_name: str):
    """查询部门预算"""
    budget = BUDGET_DB.get(department_name)
    if not budget:
        return f"部门 {department_name} 不存在"
    return f"部门预算: 总预算={budget['total']}，已用预算={budget['used']}，剩余预算={budget['remaining']}"


if __name__ == '__main__':
    mcp.run(transport="http", port=8000, host="0.0.0.0")
