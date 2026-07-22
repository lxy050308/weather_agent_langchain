from tools.air_quality_tool import get_air_quality




class AirQualitySkill:


    name="空气质量Skill"



    description="""

    查询空气质量，

    判断是否适合户外活动。

    """



    def run(self,city:str):


        air=get_air_quality.invoke(

            {

                "city":city

            }

        )


        advice=self.analyze(

            air

        )


        return f"""

{air}


空气建议:

{advice}

"""




    def analyze(self,air):


        if "污染" in air:


            return "空气质量较差，不建议长时间户外运动。"


        elif "优" in air:


            return "空气很好，适合户外活动。"



        else:


            return "空气质量一般，建议适量运动。"