from app import GetHivesList
from os import environ as env


def main():
    params = {
        'mongo_host': env.get('MONGO_HOST', 'localhost'),
        'mongo_port': env.get('MONGO_PORT', '27017'),
        'mongo_db': env.get('MONGO_DB', 'mayaprotect'),
        'default_limit': env.get('DEFAULT_LIMIT', 25)
    }
    app = GetHivesList(params)
    app.run()


if __name__ == '__main__':
    main()
