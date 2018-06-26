from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from sqlalchemy import Column, Integer, String 
from app import db
from flask import json, jsonify
import datetime
import re

from app.controllers.jsonencoder import GenericJsonEncoder
from app.controllers.utilities.enums import TipoJogo as _enumGameType

class Person(object):
		def __init__(self, _id, name, email, password, dtCadastro, active):
				self.id = _id
				self.name = name
				self.email = email
				self.password = password
				self.dtCadastro = dtCadastro
				self.active = active
		
		def __str__(self):
    			return { 'id' : self.id, 'name' : self.name, 'email' : self.email, 'dtCadastro' : GenericJsonEncoder.default(None,self.dtCadastro), 'active' : bool(self.active)  }

		def to_dict(self):	
			return { "id": self.id if self.id else None, "name": str(self.name) if self.name else None,	"email": str(self.email) if self.email else None, "dtCadastro": str(self.dtCadastro) if self.dtCadastro else None }
		# def __repr__(self):
		# 	return "id:'{0}', name:'{1}', email:'{2}', dtCadastro: {3}".format(str(self.id), self.name, self.email, self.dtCadastro)

		def check_password(self, password):
			return check_password_hash(self.password_hash, password)
				
		@validates('name')
		def validate_username(self, key, name):
			if not name:
				raise AssertionError('No username provided')

			# if User.query.filter(Pessoa.name == name).first():
			# 	raise AssertionError('Username is already in use')

			if len(name) < 5 or len(name) > 20:
				raise AssertionError('Username must be between 5 and 20 characters')

			return name

		@validates('email')
		def validate_email(self, key, email):
			if not email:
				raise AssertionError('No email provided')

			if not re.match("[^@]+@[^@]+\.[^@]+", email):
				raise AssertionError('Provided email is not an email address')

			return email
				
		def set_password(self, password):
			if not password:
				raise AssertionError('Password not provided')

			if not re.match('\d.*[A-Z]|[A-Z].*\d', password):
				raise AssertionError('Password must contain 1 capital letter and 1 number')

			if len(password) < 8 or len(password) > 50:
				raise AssertionError('Password must be between 8 and 50 characters')

			self.password_hash = generate_password_hash(password)

class PersonGame(object):
    	
		def __init__(self, _id, concurse, name, game, hits, ticket_amount):
				self.id = _id
				self.concurse = concurse
				self.name = name
				self.game = game
				self.hits = hits
				self.amount = ticket_amount
				pass
	
		def __str__(self):
				return { 'id' : self.id, 'concurse' : self.concurse,'name' : self.name, 'game' : self.game, 'hits' : self.hits, 'amount' : GenericJsonEncoder.default(None,self.amount) }

class JsonDashBoard(object):
		def __init__(self, lot_concurse, dtConcurse, dtExtense, lot_game, hit15, shared15, percent15, hit14, shared14, percent14, hit13, shared13, percent13, hit12, shared12, percent12, hit11, shared11, percent11, amount_tickets):
				self.concurse = lot_concurse
				self.dtConcurse = dtConcurse
				self.dtExtense = dtExtense
				self.game = lot_game
				self.hit15 = hit15
				self.shared15 = shared15
				self.percent15 = percent15
				self.hit14 = hit14
				self.shared14 = shared14
				self.percent14= percent14
				self.hit13 = hit13
				self.shared13 = shared13
				self.percent13= percent13
				self.hit12 = hit12
				self.shared12 = shared12
				self.percent12= percent12
				self.hit11 = hit11
				self.shared11 = shared11
				self.percent11 = percent11
				self.amount_tickets = amount_tickets

		def __str__(self):
    			return { 'concurse' : self.concurse, 'dtConcurse' : self.dtConcurse, 'dtExtense' : self.dtExtense, 'game' : self.game, 'hit15' : self.hit15, 'shared15' : GenericJsonEncoder.default(None,self.shared15), 'percent15' : GenericJsonEncoder.default(None,self.percent15), 'hit14' : self.hit14, 'shared14' : GenericJsonEncoder.default(None,self.shared14), 'percent14' : GenericJsonEncoder.default(None,self.percent14), 'hit13' : self.hit13, 'shared13' : GenericJsonEncoder.default(None,self.shared13), 'percent13' : GenericJsonEncoder.default(None,self.percent13), 'hit12' : self.hit12, 'shared12' : GenericJsonEncoder.default(None,self.shared12), 'percent12' : GenericJsonEncoder.default(None,self.percent12), 'hit11' : self.hit11, 'shared11' : GenericJsonEncoder.default(None,self.shared11), 'percent11' : GenericJsonEncoder.default(None,self.percent11), 'amount_tickets' : GenericJsonEncoder.default(None,self.amount_tickets) }


class Lottery(object):
	def __init__(self, _id, concurse, dtConcurse, game, hit15, hit14, hit13, hit12, hit11, shared15, shared14, shared13, shared12, shared11, dtNextConcurse, tpj_id=2):
    		self.id = _id
    		self.concurse = concurse
    		self.dtConcurse = dtConcurse
    		self.game = game
    		self.hit15 = hit15
    		self.hit14 = hit14
    		self.hit13 = hit13
    		self.hit12 = hit12
    		self.hit11 = hit11
    		self.shared15 = shared15
    		self.shared14 = shared14
    		self.shared13 = shared13
    		self.shared12 = shared12
    		self.shared11 = shared11
    		self.dtNextConcurse = dtNextConcurse
    		self.tpj_id = tpj_id

	def __str__(self):
    		return { 'id' : self.id, 'concurse' :  self.concurse, 'dtConcurse': GenericJsonEncoder.default(None, self.dtConcurse), 'game': self.game, 'hit15': self.hit15, 'hit14': self.hit14, 'hit13': self.hit13, 'hit12': self.hit12, 'hit11': self.hit11, 'shared15': GenericJsonEncoder.default(None,self.shared15), 'shared14': GenericJsonEncoder.default(None,self.shared14), 'shared13': GenericJsonEncoder.default(None,self.shared13), 'shared12': GenericJsonEncoder.default(None,self.shared12), 'shared11': GenericJsonEncoder.default(None,self.shared11), 'dtNextConcurse': GenericJsonEncoder.default(None, self.dtNextConcurse) ,'gameType': self.tpj_id}
	
class Configuration(object):
    	def __init__(self, _id, calculate_tens_without_success, send_email_manually, send_email_automatically, check_game_online, min_amount_to_send_email, person = None):
    			self.id = _id
    			self.calculate_tens_without_success = calculate_tens_without_success
    			self.send_email_manually = send_email_manually
    			self.send_email_automatically = send_email_automatically
    			self.check_game_online = check_game_online
    			self.min_amount_to_send_email = min_amount_to_send_email
    			self.person = person
		
    	def __str__(self):
    			return { 'id' : self.id, 'calculate_tens_without_success': self.calculate_tens_without_success, 'send_email_manually': self.send_email_manually, 'send_email_automatically' : self.send_email_automatically, 'check_game_online': self.check_game_online, 'min_amount_to_send_email' : GenericJsonEncoder.default(None,self.min_amount_to_send_email), 'person' : self.person}

class EmailSent(object):
    	def __init__(self, _id, id_person_who_sent, id_person_who_received, ema_person_who_received_email, ema_bcc, ema_cc, ema_dtSent, ema_subject, ema_message, ema_ticket_amount, lot_concurse, ema_success, ema_manually):
    			self.id = _id
    			self.id_person_who_sent = id_person_who_sent
    			self.id_person_who_received = id_person_who_received
    			self.ema_person_who_received_email = ema_person_who_received_email,
    			self.ema_bcc = ema_bcc
    			self.ema_cc = ema_cc 
    			self.ema_dtSent = ema_dtSent
    			self.ema_subject = ema_subject 
    			self.ema_message = ema_message
    			self.ema_ticket_amount = ema_ticket_amount
    			self.lot_concurse = lot_concurse
    			self.ema_success = ema_success
    			self.ema_manually = ema_manually
    			pass

    	def __str__(self):
    			return { 'id' : self.id, 'id_person_who_sent': self.id_person_who_sent, 'id_person_who_received': self.id_person_who_received, 'ema_person_who_received_email' : str(self.ema_person_who_received_email), 'ema_bcc': self.ema_bcc, 'ema_cc' : self.ema_bcc, 'ema_dtSent' : GenericJsonEncoder.default(None,self.ema_dtSent), 'ema_subject': self.ema_subject, 'ema_message': self.ema_message, 'ema_ticket_amount': GenericJsonEncoder.default(None, self.ema_ticket_amount), 'lot_concurse' : self.lot_concurse, 'ema_success' : self.ema_success, 'ema_manually' : self.ema_manually }
				
				