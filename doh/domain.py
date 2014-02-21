from .models import (
    DBSession,
    Tip,
    )

class TipsRepository(object):
    def get_next(self):
        return DBSession.query(Tip).order_by("RANDOM()").first()
