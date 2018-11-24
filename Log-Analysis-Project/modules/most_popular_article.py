from modules import db_connection
from modules import prints_pattern


# get_most_popular_article
def get_most_popular_article():
    cursor = db_connection.get_connection()
    top_three_articles = ("""
        SELECT title, path, COUNT(path) AS hits, authors.name
        FROM articles
        JOIN authors
        ON articles.author = authors.id
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY title, path, authors.name
        ORDER BY hits DESC LIMIT 3;
    """)
    cursor.execute(top_three_articles)
    return cursor


def print_top_three_articles():
    request_1 = "1. What are the most popular three articles of all time?"
    print(request_1)

    # prints_pattern.stars_repeater()
    for items in get_most_popular_article():
        print("\t" + "%s - %s" % (items[0], items[2]) + " Views")

    prints_pattern.stars_repeater()
