from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from dotenv import load_dotenv

import os
import sqlite3

from langgraph.checkpoint.sqlite import SqliteSaver


from skills.weather_skill import WeatherSkill
from skills.user_profile_skill import UserProfileSkill
from skills.travel_skill import TravelSkill



load_dotenv()



# ======================
# Skill
# ======================

weather_skill = WeatherSkill()

profile_skill = UserProfileSkill()

travel_skill = TravelSkill()



USER_ID="user_001"



# ======================
# 用户画像Tool
# ======================


@tool
def save_user_city(city:str)->str:

    """
    保存用户城市
    """

    return profile_skill.save_city(
        USER_ID,
        city
    )




@tool
def get_user_city()->str:

    """
    获取用户城市
    """

    city = profile_skill.get_city(
        USER_ID
    )


    if city:
        return city

    return "没有记录城市"





# ======================
# 天气Tool
# ======================


@tool
def weather_query(city:str)->str:

    """
    查询城市天气
    """

    return weather_skill.run(city)






# ======================
# 旅游Tool
# ======================


@tool
def travel_plan(city:str)->str:

    """
    根据天气生成旅游规划
    """

    return travel_skill.run(city)






# ======================
# DeepSeek
# ======================


llm = ChatOpenAI(

    model="deepseek-chat",

    api_key=os.getenv(
        "DEEPSEEK_API_KEY"
    ),

    base_url="https://api.deepseek.com",

    temperature=0

)





# ======================
# Memory
# ======================


conn = sqlite3.connect(

    "memory/weather_memory.db",

    check_same_thread=False

)


memory = SqliteSaver(conn)






# ======================
# Weather Agent
# ======================


weather_agent = create_agent(


    model=llm,


    tools=[

        save_user_city,

        get_user_city,

        weather_query,

        travel_plan

    ],



    system_prompt="""


你是天气旅行Agent。


你的职责：

1. 管理用户城市


用户告诉城市：

例如：

我在上海

调用：

save_user_city



----------------


2. 查询天气


用户询问天气：

先调用：

get_user_city


然后：

weather_query



----------------


3. 旅游规划


用户询问：

旅游

出去玩

行程安排


调用：

get_user_city


然后：

travel_plan



不要处理空气质量问题。


""",


    checkpointer=memory

)





def run_weather_agent(message):


    config={

        "configurable":{

            "thread_id":USER_ID

        }

    }


    result=weather_agent.invoke(


        {

        "messages":[

            {

            "role":"user",

            "content":message

            }

        ]

        },


        config=config

    )


    return result["messages"][-1].content