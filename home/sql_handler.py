from django.db import connection

def insert(a,b,c,d):
    tester = connection.cursor()
    tester.execute("INSERT INTO home_comment (comment_id, op_id, comment_text, author) VALUES ( %s, %s, %s, %s)", [a,b,c,d])
    return id

'''def delete(a):
    tester = connection.cursor()
    tester.execute("DELETE FROM polls_Game Where name=%s", [a])
    return a'''