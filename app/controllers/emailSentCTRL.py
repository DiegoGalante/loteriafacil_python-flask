from app.models.DAO import emailSentDAO as _db

def GravaLog(EmailSent):
    return _db.GravaLog(EmailSent)