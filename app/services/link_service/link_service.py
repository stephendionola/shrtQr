# import hashlib
# from app.models.database import get_connection
# from app.schemas import LinkCreate, Link

# class LinkService:
#     def shorten(self, link_data: LinkCreate) -> Link:
#         short_code = self._generate_short_code(link_data.url)
#         with get_connection() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute(
#                     "INSERT INTO links (url, short_code) VALUES (%s, %s)",
#                     (link_data.url, short_code)
#                 )
#                 conn.commit()
#                 link_id = cursor.lastrowid
#         return Link(id=link_id, url=link_data.url, short_code=short_code)

#     def get_by_code(self, short_code: str) -> Link | None:
#         with get_connection() as conn:
#             with conn.cursor() as cursor:
#                 cursor.execute("SELECT * FROM links WHERE short_code = %s", (short_code,))
#                 row = cursor.fetchone()
#                 if row:
#                     return Link(**row)
#         return None

#     def _generate_short_code(self, url: str) -> str:
#         return hashlib.md5(url.encode()).hexdigest()[:6]

import hashlib
from typing import Optional
from app.schemas import LinkCreate, Link
from app.services.db_service import execute_query, fetch_one, insert_one
from app.services.link_service.link_service_scripts import SQL_INSERT_LINK, SQL_SELECT_LINK_BY_CODE

class LinkService:
    def shorten(self, link_data: LinkCreate) -> Link:
        short_code = self._generate_short_code(link_data.url)
        link_id = insert_one(SQL_INSERT_LINK, (link_data.url, short_code))
        return Link(url=link_data.url, short_code=short_code, id=link_id['id'])

    def get_by_code(self, short_code: str) -> Optional[Link] :
        row = fetch_one(SQL_SELECT_LINK_BY_CODE, (short_code,))
        if row:
            return Link(**row)
        return None

    def _generate_short_code(self, url: str) -> str:
        return hashlib.md5(url.encode()).hexdigest()[:6]
