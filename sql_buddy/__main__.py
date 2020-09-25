#!/usr/bin/env python3

import argparse
import sqlite3
import csv

from importlib import resources

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from prompt_toolkit import PromptSession

from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.sql import SqlLexer

from sql_buddy.concept import Base, Concept
from sql_buddy.create_objects import create_concepts

from sql_buddy.sql_resources import sql_completer, style

def get_args():
	parser = argparse.ArgumentParser(description='Look up SQL queries and concepts like index cards for study purposes')
	parser.add_argument(
		'-o',
		'--on',
		help='Boolean flag for pure SQL REPL mode',
		action='store_true'
	)
	return parser.parse_args()

def main():

	args = get_args()

	if args.on == False:

		print("\nWelcome to sql-buddy.  Populating In-memory Database...\n")
		concepts_list = create_concepts()

		# In-memory sqlite database
		engine = create_engine('sqlite:///:memory:', echo=False)

		Base.metadata.create_all(engine)

		sqla_session = sessionmaker(bind=engine)
		db_session = sqla_session()
		db_session.add_all(concepts_list)

		db_session.commit()

		# prompt-tookit
		session = PromptSession()

		print("\nPress Esc + ENTER to enter sql_buddy commands.")
		print("Press CTRL-D to quit\n")

		print("Type 'commands' and press Esc + ENTER to get a list of sql_buddy commands")

		while True:
			try:
				text = session.prompt('> ', multiline=True)

				if text == "commands":
					print("\t* list all: lists all the SQL concepts and queries")
					print("\t* list some: list the first 10 concepts in the SQL concepts database")
					print("\t* search=>{concept_name} gives you the definition, syntax, and usage of a specific SQL concept like group_by")
					print("\t\t* i.e. search=>group_by")
					print("\t\t* i.e. search=>order_by")
					print("\t\t* i.e. search=>where")
					print("\t\t* all SQL concept names must be in lowercase and have underscores in place of spaces")

				elif text == "list all":
					for instance in db_session.query(Concept).order_by(Concept.id):
						print(f"\n{instance.name}: \n\n{instance.definition}\n")

				elif text == "list some":
					for instance in db_session.query(Concept).order_by(Concept.id)[:10]:
						print(f"\n{instance.name}: \n\n{instance.definition}\n")

				elif text[:6] == "search":
					search_obj = text[8:]
					instance = db_session.query(Concept).filter(Concept.name == search_obj).first()
					if instance is not None:
						print(f"\n{instance.name}: \n\n{instance.definition}\n")
						print(f"syntax: \n{instance.syntax}\n")
						print(f"usage: \n{instance.example}\n")
						print(f"related concepts: \n{instance.related_concepts}\n")
					else:
						print("\nConcept does not exist in database.  Try again.\n")

			except KeyboardInterrupt:
				continue
			except EOFError:
				break

		print("Goodbye!")

	else:
		print("Entering SQL REPL Mode...")
		print("Creating in-memory database named <deathrow> for SQL experiments.")
		print("Example: select last_name, first_name, execution_date, last_statement from deathrow order by length(last_statement) desc limit 5;")

		connection = sqlite3.connect(':memory:')
		cur = connection.cursor()
		cur.execute("""
			CREATE TABLE deathrow(
				ex_number INTEGER PRIMARY KEY,
				birth_date TEXT,
				date_of_crime TEXT,
				education VARCHAR,
				last_name VARCHAR,
				first_name VARCHAR,
				tdjc_num INTEGER,
				death_date TEXT,
				date_received TEXT,
				execution_date TEXT,
				race VARCHAR,
				county VARCHAR,
				eye_color VARCHAR,
				weight VARCHAR,
				height VARCHAR,
				native_country VARCHAR,
				state VARCHAR,
				last_statement TEXT
			)
		""")
		connection.commit()

		with resources.open_text('sql_buddy', 'tx_deathrow_full.csv') as f:
			reader = csv.reader(f)
			next(reader)
			for row in reader:
				cur.execute(
					"INSERT INTO deathrow VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
					row
				)
		connection.commit()

		session = PromptSession(
			lexer=PygmentsLexer(SqlLexer),
			completer=sql_completer,
			style=style
		)

		print("\nPress Esc + ENTER to enter SQL statments.")
		print("Press CTRL-D to quit\n")

		while True:
			try:
				text = session.prompt('> ', multiline=True)
			except KeyboardInterrupt:
				continue
			except EOFError:
				break

			with connection:
				try:
					messages = connection.execute(text)
				except Exception as e:
					print(repr(e))
				else:
					for message in messages:
						print(f"{message}\n")

		connection.close()
		print('Goodbye!')




if __name__ == '__main__':
	main()




