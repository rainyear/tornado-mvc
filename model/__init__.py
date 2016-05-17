import motor.motor_tornado
class DB:
    def __init__(self, Env):
        self._client = motor.motor_tornado.MotorClient(Env.DB_HOST, Env.DB_PORT)
        self._db = self._client[Env.DB_NAME]

    def get_users(self, n = 10):
        pass
