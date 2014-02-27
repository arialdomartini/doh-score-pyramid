from .models import (
    DBSession,
    Tip,
    Visit
    )

class TipsRepository(object):
    def get_next(self, session):
        tip = DBSession.query(Tip).outerjoin(Visit, Tip.id == Visit.tip_id and Visit.session == session).filter(Visit.id == None).order_by("RANDOM()").first()
        if tip != None:
            visit = Visit(session, tip.id)
            DBSession.add(visit)
        return tip
        
