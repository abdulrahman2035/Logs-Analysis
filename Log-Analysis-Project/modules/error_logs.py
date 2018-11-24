from modules import db_connection
from modules import prints_pattern


def get_requests_errors():
    cursor = db_connection.get_connection()

    error_reports = """select date(time),round(100.0*sum(case log.status when '200 OK'
        then 0 else 1 end)/count(log.status),2) as "Percent_Error"
        from log group by date(time)
        order by "Percent_Error" desc;"""
    cursor.execute(error_reports)
    return cursor.fetchall()


def print_error_logs():
    print("3. On which days did more than 1% of requests lead to errors?")
    # prints_pattern.stars_repeater()
    for item in get_requests_errors():
        if float(item[1]) > 1:
            print('\t' + str(item[0]) + ' ---> ' + str(item[1]) + ' %')
        pass

    prints_pattern.stars_repeater()
