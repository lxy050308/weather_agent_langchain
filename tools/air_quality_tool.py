from langchain_core.tools import tool

import requests

import os



@tool
def get_air_quality(city: str) -> str:
    """
    查询城市空气质量。

    输入城市名称，例如：
    shanghai、beijing。

    返回AQI指数和空气质量等级。
    """


    try:


        token = os.getenv(
            "WAQI_API_KEY"
        )


        if not token:

            return "未检测到WAQI_API_KEY，请检查环境变量配置"



        import urllib.parse

        city_map = {
            "上海": "shanghai",
            "北京": "beijing",
            "广州": "guangzhou",
            "深圳": "shenzhen",
            "杭州": "hangzhou",
            "成都": "chengdu",
            "南京": "nanjing",
            "武汉": "wuhan",
            "西安": "xian",
            "重庆": "chongqing",
            "苏州": "suzhou",
            "厦门": "xiamen",
            "青岛": "qingdao",
            "天津": "tianjin",
            "长沙": "changsha",
            "大连": "dalian",
            "郑州": "zhengzhou",
            "昆明": "kunming",
            "济南": "jinan",
            "沈阳": "shenyang",
            "合肥": "hefei",
            "福州": "fuzhou",
            "哈尔滨": "harbin",
            "长春": "changchun",
            "石家庄": "shijiazhuang",
            "太原": "taiyuan",
            "南宁": "nanning",
            "贵阳": "guiyang",
            "兰州": "lanzhou",
            "海口": "haikou",
            "呼和浩特": "hohhot",
            "乌鲁木齐": "urumqi",
        }

        query_city = city_map.get(city)
        if query_city is None:
            query_city = urllib.parse.quote(city)

        url = f"https://api.waqi.info/feed/{query_city}/"



        response = requests.get(

            url,

            params={

                "token": token

            },

            timeout=10

        )



        data = response.json()



        if data.get("status") != "ok":

            return f"""

空气质量查询失败：

{data}

"""



        aqi = data["data"]["aqi"]



        if aqi <= 50:

            level = "优"


        elif aqi <= 100:

            level = "良"


        elif aqi <= 150:

            level = "轻度污染"


        elif aqi <= 200:

            level = "中度污染"


        else:

            level = "重度污染"



        return f"""

城市：{city}

AQI指数：{aqi}

空气质量：{level}

"""



    except Exception as e:


        return f"""

空气质量查询异常：

{str(e)}

"""