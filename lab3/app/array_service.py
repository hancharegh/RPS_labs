from db import get_connection


def save_array(user_id, original, sorted_arr):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO arrays (user_id, original, sorted) VALUES (?, ?, ?)",
        (user_id, str(original), str(sorted_arr))
    )

    conn.commit()
    conn.close()


def get_arrays(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT original, sorted FROM arrays WHERE user_id=?", (user_id,))
    data = cur.fetchall()

    conn.close()
    return data


def clear_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM arrays")
    conn.commit()
    conn.close()
