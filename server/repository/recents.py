from sqlalchemy import func, desc, select

from models.recent import *

def get_recentblogs(session):
    results = session.scalars(select(Recents).order_by(desc(Recents.id)).limit(3)).all()
    for ind, res in enumerate(results):
        results[ind] = dict_from_recents(res)
    return results
