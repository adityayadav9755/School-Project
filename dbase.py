import merasql as sql


def initiate():
    sql.db_creation(dbname="humaradb")
    cd = ""
    sale = ""
    items = ""
    sql.table_creation(struc=cd)
    sql.table_creation(struc=sale)
    sql.table_creation(struc=items)

