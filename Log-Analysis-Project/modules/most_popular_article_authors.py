from modules import db_connection
from modules import prints_pattern


# most_popular_article_authors
def get_most_popular_article_authors():
    cursor = db_connection.get_connection()
    most_popular_article_author = """\
        SELECT authors.name, count(*) as views
        FROM articles
        JOIN authors
            ON articles.author = authors.id
            JOIN log
            ON articles.slug = substring(log.path, 10)
            WHERE log.status LIKE '200 OK'
            GROUP BY authors.name ORDER BY views DESC;
    """
    cursor.execute(most_popular_article_author)
    return cursor.fetchall()


def print_most_popular_article_authors():
    print("2. Who are the most popular article authors of all time?")
    # prints_pattern.stars_repeater()
    for item in get_most_popular_article_authors():
        print("\t" + item[0] + " - " + str(item[1]) + " views")

    prints_pattern.stars_repeater()
