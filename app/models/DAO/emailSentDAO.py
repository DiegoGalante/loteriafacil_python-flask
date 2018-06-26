from app import db
from app.models.tables import EmailSent
from flask import jsonify, json

from app.controllers.jsonencoder import GenericJsonEncoder

# from datetime import *
from decimal import Decimal


def GravaLog(EmailSent):
    sqlCommand = """
                  EXEC SP_SAVE_LOG_EMAIL ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                 """

    formattedSQL = [int(EmailSent.id),
                    int(EmailSent.id_person_who_sent),
                    int(EmailSent.id_person_who_received),
                    EmailSent.ema_person_who_received_email[0],
                    str(EmailSent.ema_bcc),
                    str(EmailSent.ema_cc),
                    '',
                    str(EmailSent.ema_subject),
                    str(EmailSent.ema_message),
                    GenericJsonEncoder.default(None, EmailSent.ema_ticket_amount),
                    int(EmailSent.lot_concurse),
                    bool(EmailSent.ema_success),
                    bool(EmailSent.ema_manually)
                    ]

    # print("EXEC SP_SAVE_LOG_EMAIL {0}".format(formattedSQL))
    cursor = db.engine.raw_connection().cursor()
    cursor.execute(sqlCommand, formattedSQL)
    cursor.commit()
    pass