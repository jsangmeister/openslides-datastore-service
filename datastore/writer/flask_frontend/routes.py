from datastore.shared.flask_frontend import unify_urls


URL_PREFIX = "/internal/datastore/writer/"


WRITE_URL = unify_urls(URL_PREFIX, "/write")
RESERVE_IDS_URL = unify_urls(URL_PREFIX, "/reserve_ids")
DELETE_HISTORY_INFORMATION_URL = unify_urls(URL_PREFIX, "/delete_history_information")
TRUNCATE_DB_URL = unify_urls(URL_PREFIX, "/truncate_db")
WRITE_ACTION_WORKER_URL = unify_urls(URL_PREFIX, "/write_action_worker")
