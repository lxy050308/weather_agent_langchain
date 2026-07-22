import sqlite3



class UserProfileSkill:


    name="用户画像Skill"


    description="""

负责管理用户长期信息：

- 保存用户城市

- 查询用户城市

- 修改用户城市

"""


    def __init__(self):


        self.conn=sqlite3.connect(

            "memory/user_profile.db",

            check_same_thread=False

        )


        self.create_table()



    def create_table(self):


        cursor=self.conn.cursor()


        cursor.execute("""

        CREATE TABLE IF NOT EXISTS user_profile(

            user_id TEXT PRIMARY KEY,

            city TEXT

        )

        """)


        self.conn.commit()




    def save_city(
        self,
        user_id,
        city
    ):


        cursor=self.conn.cursor()


        cursor.execute(
            """
            INSERT OR REPLACE INTO user_profile
            (user_id,city)

            VALUES (?,?)

            """,

            (
                user_id,
                city
            )

        )


        self.conn.commit()


        return f"已经记录您的城市：{city}"




    def get_city(
        self,
        user_id
    ):


        cursor=self.conn.cursor()


        cursor.execute(

            """
            SELECT city
            FROM user_profile
            WHERE user_id=?

            """,

            (
                user_id,
            )

        )


        result=cursor.fetchone()



        if result:

            return result[0]


        return None