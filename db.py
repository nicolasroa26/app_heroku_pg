from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence
import sqlalchemy 

engine = create_engine('postgres://fhpebriezsuyly:576364a25eed0956440777de9005f84bd021b89d5f65817338be42fc19df35de@ec2-23-23-180-121.compute-1.amazonaws.com:5432/d6b8r5d8bu18ri', echo=True)
metadata = MetaData()
formulario = Table('formulario', metadata,
    Column('id', Integer, primary_key=True),
    Column('post', String),
    Column('tokens', String),
    Column('groups', String),
    Column('notification', String)
)

def insert(groups, usuarios, message):
	conn = engine.connect()
	metadata.create_all(engine)
	ins = formulario.insert().values(post=message, tokens=str(usuarios), groups=groups, notification='Done')
	ins.compile().params
	result = conn.execute(ins)
	ins.bind = engine
	str(ins)
	result.inserted_primary_key