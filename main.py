from agents.supervisor_agent import supervisor_agent



print("===================")

print("Multi-Agent环境智能助手启动")

print("===================")



while True:


    user=input("\n用户:")



    if user=="exit":

        break



    answer=supervisor_agent(
        user
    )


    print("\nAI:")

    print(answer)