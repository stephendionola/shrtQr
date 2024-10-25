SQL_INSERT_LINK = "INSERT INTO links (url, short_code) VALUES (%s, %s) RETURNING id"
SQL_SELECT_LINK_BY_CODE = "SELECT * FROM links WHERE short_code = %s"
