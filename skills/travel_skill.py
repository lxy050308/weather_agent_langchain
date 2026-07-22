from skills.weather_skill import WeatherSkill
from skills.air_quality_skill import AirQualitySkill


class TravelSkill:

    name = "旅行规划Skill"

    description = """
    根据天气和空气质量生成旅行规划
    """


    def __init__(self):

        self.weather_skill = WeatherSkill()

        self.air_skill = AirQualitySkill()


    def run(self, city:str):

        weather = self.weather_skill.run(city)

        air = self.air_skill.run(city)


        return f"""

====== {city}旅游规划 ======


天气情况：

{weather}


空气质量：

{air}


旅游建议：

上午：
- 景点游览

下午：
- 商圈体验

晚上：
- 夜景和美食


"""