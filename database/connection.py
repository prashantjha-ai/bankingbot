import psycopg2


class DatabaseConnection:
    def __init__(self, host, port, dbname):
        self.host = host
        self.port = port
        self.dbname = dbname
        # self.user = user
        # self.password = password
        self.connection = None

    def connect(self):
        print(self.host, self.port, self.dbname )


        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                    # user=self.user,
                    # password=self.password
            )

            print("Connected to the database successfully.")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
