#! /usr/bin/env python
from modules import most_popular_article_authors
from modules import error_logs
from modules import most_popular_article


def main():
    most_popular_article.print_top_three_articles()
    most_popular_article_authors.print_most_popular_article_authors()
    error_logs.print_error_logs()


if __name__ == '__main__':
    main()
