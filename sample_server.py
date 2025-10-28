import click
import logging
from mcp.server.fastmcp import FastMCP

#配置日志
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

#创建一个FastMCP对象
mcp = FastMCP("演示",port=5050)

#添加一个计算器工具
@mcp.tool(name='calculate', description='计算数学表达式')
def calculate(expression: str) :
    """计算数学表达式"""
    try:
        result = eval(expression)
        return f"计算结果为：{result}"
    except Exception as e:
        return f"计算错误：{str(e)}"
@mcp.tool(name='add', description='计算两个数的和')
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool(name='multiply', description='计算两个数的积')
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

def main() -> int:
    logging.info("正在初始化MCP演示服务")
    #启动SSE
    logger.info("使用SSE传输模式启动MCP服务")
    print("请使用浏览器访问 http://localhost:5050/sse 来查看MCP服务")
    try:
        #启动FastMCP服务
        mcp.run(transport="sse")
    except Exception as e:
        logger.error(f"启动MCP服务时出错：{str(e)}")
        print(f"启动MCP服务时出错：{str(e)}")
    #等待用户输入
if __name__ == "__main__":
    main()
