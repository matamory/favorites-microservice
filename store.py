import sqlite3

DB_NAME = "favorites.db"


def init_db():
    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            app_id TEXT NOT NULL,
            username TEXT NOT NULL,
            item_id TEXT NOT NULL,
            UNIQUE(app_id, username, item_id)
        )
    """)

    connection.commit()
    connection.close()


# Insert

def insert(app_id, username, item_id):
    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        INSERT INTO favorites (app_id, username, item_id)
        VALUES (?, ?, ?)
    """, (app_id, username, item_id))

    connection.commit()
    connection.close()


# Exists

def exists(app_id, username, item_id):
    connection = sqlite3.connect(DB_NAME)

    result = connection.execute("""
        SELECT 1
        FROM favorites
        WHERE app_id = ? AND username = ? AND item_id = ?
    """, (app_id, username, item_id)).fetchone()

    connection.close()

    return result is not None


# List Favorites

def list_favorites(app_id, username):
    connection = sqlite3.connect(DB_NAME)

    rows = connection.execute("""
        SELECT item_id
        FROM favorites
        WHERE app_id = ? AND username = ?
    """, (app_id, username)).fetchall()

    connection.close()

    return [row[0] for row in rows]


# Delete

def delete(app_id, username, item_id):
    connection = sqlite3.connect(DB_NAME)

    connection.execute("""
        DELETE FROM favorites
        WHERE app_id = ? AND username = ? AND item_id = ?
    """, (app_id, username, item_id))

    connection.commit()
    connection.close()




if __name__ == "__main__":
    init_db()