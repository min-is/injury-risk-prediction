import snowflake.connector
import os

class SnowflakeClient:
    def __init__(self):
        self.conn = snowflake.connector.connect(
            user=os.getenv('SNOWFLAKE_USER'),
            password=os.getenv('SNOWFLAKE_PASSWORD'),
            account=os.getenv('SNOWFLAKE_ACCOUNT'),
            warehouse='ATHLETE_WH',
            database='INJURY_RISK',
            schema='ATHLETE_DATA'
        )
    
    def execute_query(self, query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            cursor.close()
    
    def insert_biomechanical_data(self, data):
        query = """
            INSERT INTO biomechanical_readings 
            (athlete_id, session_id, left_force, right_force)
            VALUES (%s, %s, %s, %s)
        """
        self.conn.cursor().execute(query, (
            data['athlete_id'],
            data['session_id'],
            data['left_force'],
            data['right_force']
        ))