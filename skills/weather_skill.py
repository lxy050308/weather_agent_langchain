from tools.weather_tool import get_weather



class WeatherSkill:


    name="天气Skill"



    def run(self,city):


        weather=get_weather.invoke(

            {
                "city":city
            }

        )


        return weather