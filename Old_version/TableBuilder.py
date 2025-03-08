from database import DatabaseConnection
from config import DB_CONFIG

class TableBuilder:
    def __init__(self, db_connection):
        self.db = db_connection

    def create_tables(self):
        commands = [
            '''
            CREATE TABLE IF NOT EXISTS motherboard (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                form VARCHAR(50) NOT NULL,
                soket VARCHAR(50) NOT NULL,
                type_member VARCHAR(50) NOT NULL,
                interface VARCHAR(50) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS supply (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                power INT NOT NULL,
                type VARCHAR(50) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS gpu (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                frequency INT NOT NULL,
                soket VARCHAR(50) NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS ram (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                frequency INT NOT NULL,
                type_member VARCHAR(50) NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS cpu (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                soket VARCHAR(50) NOT NULL,
                frequency INT NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS cooler (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                speed INT NOT NULL,
                power_use INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS frame (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                form VARCHAR(50) NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS hdd (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                price DECIMAL NOT NULL,
                capacity INT NOT NULL,
                recording INT NOT NULL,
                reading INT NOT NULL
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS configuration(
                conf_id SERIAL PRIMARY KEY,
                motherboard_id INT REFERENCES motherboard(id),
                supply_id INT REFERENCES supply(id),
                cpu_id INT REFERENCES cpu(id),
                gpu_id INT REFERENCES gpu(id),
                cooler_id INT REFERENCES cooler(id),
                ram_id INT REFERENCES ram(id),
                hdd_id INT REFERENCES hdd(id),
                frame_id INT REFERENCES frame(id),
                named VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            '''
        ]

        for command in commands:
            self.db.execute_query(command)
            print(f"Executed: {command}")

if __name__ == "__main__":
    db_connection = DatabaseConnection(**DB_CONFIG)
    table_builder = TableBuilder(db_connection)
    table_builder.create_tables()
    db_connection.close()
