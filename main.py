import psycopg2


conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="leonid200955",
    port=5432
)

cur = conn.cursor()


cur.execute("""
    CREATE TABLE IF NOT EXISTS person(
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender CHAR(1)
    );
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
            (1, 'John', 17, 'M'),
            (2, 'Mike', 21, 'M'),
            (3, 'Leonid', 14, 'M');

""")

conn.commit()


cur.close()
conn.close()
