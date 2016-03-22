from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
record = Table('record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('record', String(length=30)),
    Column('type', String(length=10)),
    Column('line_type', String(length=20)),
    Column('value', String(length=100)),
    Column('weight', String(length=100)),
    Column('mx', String(length=20)),
    Column('ttl', Integer),
    Column('dname_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['record'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['record'].drop()
