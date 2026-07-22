from agents.weather_agent import run_weather_agent

from agents.environment_agent import run_environment_agent



def supervisor_agent(user_input):


    text=user_input



    # 环境任务

    if any(
        word in text
        for word in
        [
        "空气",
        "污染",
        "PM",
        "运动"
        ]
    ):


        return run_environment_agent(
            text
        )



    # 默认天气Agent


    return run_weather_agent(
        text
    )
