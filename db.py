from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Sequence
import sqlalchemy 

engine = create_engine('postgres://vrfquhfgopxcmj:85439f192f94c7d9150bba204fda4ca245bbecb98ed07e726a5ccaa48b059a5a@ec2-107-21-103-146.compute-1.amazonaws.com:5432/d43mf9ol0g57b', echo=True)
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