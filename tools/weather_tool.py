from langchain_core.tools import tool
import requests


@tool
def get_weather(city: str) -> str:
    """
    查询城市天气。
    输入城市名称，例如：上海、北京。
    """

    try:

        url = f"https://wttr.in/{city}?format=j1"


        response = requests.get(
            url,
            timeout=10
        )


        data=response.json()


        current=data["current_condition"][0]


        weather=current["weatherDesc"][0]["value"]

        temperature=current["temp_C"]

        feels=current["FeelsLikeC"]

        humidity=current["humidity"]


        return f"""

城市：{city}

天气：{weather}

温度：{temperature}℃

体感温度：{feels}℃

湿度：{humidity}%

"""


    except Exception as e:

        return f"天气查询失败:{str(e)}"