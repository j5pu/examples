from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, Bundle
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import inspect
from sqlalchemy.engine import reflection

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("sqlite:///tbot.db")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
urls = Base.classes.crawl_urls

session = Session(engine)

# for row in session.query(urls.key).all()[1:20]:
#     print(row)
inspector = inspect(engine)

# Get table information
# print(inspector.get_table_names())
#
# # Get column information
# print(inspector.get_columns('crawl_urls'))
#
# # Create a MetaData instance
# metadata = MetaData()
# print(metadata.tables)
#
# # reflect db schema to MetaData
# metadata.reflect(bind=engine)
# print(metadata.tables)
#
# # Create MetaData instance
# metadata = MetaData(engine, reflect=True)
# print(metadata.tables)
#
# # Get Table
# ex_table = metadata.tables['crawl_urls']
# print(ex_table)
# insp = reflection.Inspector.from_engine(engine)
# print(insp.get_table_names())
#
# inspector = inspect(engine)



columns = [i['name'] for i in inspector.get_columns('crawl_urls')]

print(columns)
print(inspector.get_pk_constraint('crawl_urls')['constrained_columns'])
print(inspector.get_indexes('crawl_urls'))
indexes = [i['column_names'][0] for i in inspector.get_indexes('crawl_urls')]
print(indexes)
#columns = [i['constrained_columns'] for i in inspector.get_pk_constraint('crawl_urls')]
#print(columns)
sess = Session(engine)
objects = list(sess.query(urls.__tablename__))
print(objects)
exit(0)

print(inspector.get_foreign_keys('crawl_urls'))
print(inspector.default_schema_name)
print(inspector.get_schema_names())
print(inspector.get_table_names())
print(inspector.get_table_options('crawl_urls'))
print(inspector.get_temp_table_names())
print(inspector.get_temp_view_names())
print(inspector.get_unique_constraints('crawl_urls'))
print(inspector.get_view_definition(inspector.get_view_names()))
print(inspector.get_view_names())
print(inspector.get_indexes('crawl_urls'))
print(inspector.get_sorted_table_and_fkc_names())

meta = MetaData()
table = Table('crawl_urls', meta)
print(inspector.reflecttable(table, None))
print(session.__repr__())
for row, o in session.query(urls.key, urls.url).all():
    print(row, o)
for row in urls.__table__.columns.keys():
    print(row)

def test_orm_full_objects_list():
    """Load fully tracked ORM objects into one big list()."""

    sess = Session(engine)
    objects = list(sess.query(urls).limit(500))
    return objects
print(test_orm_full_objects_list())

def test_orm_full_objects_chunks():
    """Load fully tracked ORM objects a chunk at a time using yield_per()."""

    sess = Session(engine)
    for obj in sess.query(urls).yield_per(1000).limit(500):
        print(obj)

print(test_orm_full_objects_chunks())

def test_orm_bundles():
    """Load lightweight "bundle" objects using the ORM."""

    sess = Session(engine)
    bundle = Bundle('url', urls.key, urls.url)
    for row in sess.query(bundle).yield_per(10000).limit(500):
        print(row)

print(test_orm_bundles())

def test_orm_columns():
    """Load individual columns into named tuples using the ORM."""

    sess = Session(engine)
    for row in sess.query(urls.key, urls.url).yield_per(10000).limit(500):
        print(row)

print(test_orm_columns())

def test_core_fetchall():
    """Load Core result rows using fetchall."""

    with engine.connect() as conn:
        result = conn.execute(urls.__table__.select().limit(500)).fetchall()
        for row in result:
            print(row)

            data = row['key'], row['url']
            print(data)

print(test_core_fetchall())

def test_core_fetchmany_w_streaming():
    """Load Core result rows using fetchmany/streaming."""

    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(urls.__table__.select().limit(500))
        while True:
            chunk = result.fetchmany(10000)
            if not chunk:
                break
            for row in chunk:
                print(row)
                data = row['key'], row['url']
                print(data)

print(test_core_fetchmany_w_streaming())

def test_core_fetchmany():
    """Load Core result rows using Core / fetchmany."""

    with engine.connect() as conn:
        result = conn.execute(urls.__table__.select().limit(500))

        print(result)
        while True:
            chunk = result.fetchmany(10000)
            if not chunk:
                break
            for row in chunk:
                print(row)

                data = row['key'], row['url']
                print(data)

print(test_core_fetchmany())

def mia():
    """Load Core result rows using Core / fetchmany."""

    with engine.connect() as conn:
        result = conn.execute(urls.__table__.select())
        for row in result:
            print(row)
            data = row['key'], row['url']
            print(data)

print(mia())

def mia1():
    """Load Core result rows using Core / fetchmany."""
    for row in engine.connect().execute(urls.__table__.select()):
        print(row)
    sess = Session(engine)

mia1()