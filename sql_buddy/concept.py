from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
		Column,
		String,
		Integer
	)
from sqlalchemy_utils import ScalarListType

Base = declarative_base()

class Concept(Base):
	__tablename__ = 'concepts'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	definition = Column(String)
	syntax = Column(String)
	related_concepts = Column(ScalarListType())
	example = Column(String)

	def __repr__(self):
		return f"<Concept(name={self.name}, definition={self.definition}, syntax={self.syntax},\
			related_concepts={self.related_concepts}, example={self.example})>"

	def __str__(self):
		return f"{self.name}: {self.definition}"



