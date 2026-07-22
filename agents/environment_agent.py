from langchain.agents import create_agent

from langchain_openai import ChatOpenAI

from langchain_core.tools import tool


from dotenv import load_dotenv

import os


from skills.air_quality_skill import AirQualitySkill
from skills.user_profile_skill import UserProfileSkill
from rag.rag_retriever import search_environment_rule


load_dotenv()



air_skill=AirQualitySkill()
profile_skill = UserProfileSkill()

USER_ID = "user_001"




@tool
def air_quality_query(city:str)->str:

    """
    查询空气质量
    """

    return air_skill.run(city)


@tool
def environment_knowledge(query:str)->str:
    """
    查询环境知识库。

    用于：
    - 空气质量标准
    - 是否适合运动
    - 环境影响分析
    - 旅游环境规则
    """

    return search_environment_rule(query)


@tool
def get_user_city()->str:
    """
    获取用户保存的城市
    """
    city = profile_skill.get_city(USER_ID)
    if city:
        return city
    return "没有记录城市"


@tool
def save_user_city(city:str)->str:
    """
    保存用户城市
    """
    return profile_skill.save_city(USER_ID, city)




llm=ChatOpenAI(

    model="deepseek-chat",

    api_key=os.getenv(
        "DEEPSEEK_API_KEY"
    ),

    base_url="https://api.deepseek.com",

    temperature=0

)





environment_agent=create_agent(


model=llm,


tools=[

    air_quality_query,
    environment_knowledge,
    get_user_city,
    save_user_city

],



system_prompt="""


你是环境分析Agent。


负责：

1. 空气质量查询


用户问：

空气怎么样

污染严重吗

适合运动吗


如果用户没有指定城市：
先调用 get_user_city 获取保存的城市
然后调用 air_quality_query


如果用户指定了城市：
直接调用 air_quality_query


用户告诉你城市：
例如：我在上海
调用 save_user_city 保存


2. 环境建议


结合：

空气质量

天气情况

生成环境建议。


不要处理旅游规划。


当需要判断：

- 是否适合运动
- 空气污染影响
- 环境健康建议
- 旅游环境因素


可以调用 environment_knowledge 查询知识库获取环境标准。


回答必须结合：

实时空气数据
+
知识库规则（如有）


"""

)





def run_environment_agent(message):


    result=environment_agent.invoke(

        {

        "messages":[

            {

            "role":"user",

            "content":message

            }

        ]

        }

    )


    return result["messages"][-1].content