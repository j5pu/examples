# # dinamic table (type('Clase', (Base,), attr_dict)
#     extracted = relationship(type(url.url.strip(url.scheme).strip('://').replace('.', '').replace('/', '_').upper(),
#                                   (Base,),
#                                   {'__tablename__':
#                                        url.url.strip(url.scheme).strip('://').replace('.', '').replace('/', '_'),
# 	                               'url': Column(URLType, primary_key=True),
#                                    'url_url': Column(Integer, ForeignKey('url.url'))}), backref='url')
#
# levels = {name: logging_levels[ini['common']['level']]
#           if name in ini['common']['to'] else logging_levels[ini['default'][name]] for name in ini['default']}
#
#
# class Ses(Session):
#     def __init__(self, tablename=None, cls=None, dic=None):
#         super(Ses, self).__init__()
#         self.child_tablename = tablename
#         self.cls = cls
#
#         l = father.child('MySession')
#         db_file = '{}.db'.format(prefix)
#         is_file(db_file)
#
#         url = '{}{}'.format(SQLITE_URL, db_file)
#         if ini['db']['dialect'] == 'mysql':
#             url = '{}{}{}@{}:{}/{}'.format(MYSQL_URL, module, PASSWORD, MYSQL_HOST, MYSQL_PORT, package)
#
#         self.engine = sqlalchemy.create_engine(url, echo=ini.getboolean('db', 'echo'))
#         l.s('COMPLETED: Engine created: class == {} - tablename == {} - engine == {}'.format(
#             self.cls, self.child_tablename, self.engine))
#
#         self.ses = Session(self.engine, autoflush=ini.getboolean('db', 'autoflush'),
#                            autocommit=ini.getboolean('db', 'autocommit'))
#
#         l.s('COMPLETED: Session created: class == {} - tablename == {} - engine == {} - session == {}'
#             .format(self.cls, self.child_tablename, self.engine, self.ses))
#         self.inspect = sqlalchemy.inspect(engine)
#
#         print(dic)
#         print(self.cls.__dict__['__tablename__'])
#         print(self.cls.__dict__['url'])
#         print(self.cls.__dict__['direct'])
#         print(self.inspect.get_pk_constraint(self.cls.__dict__['__tablename__'])['constrained_columns'])
#     def get(self, value='k'):
#         if value == 'k':
#             return self.inspect.get_pk_constraint(self.cls.__dict__['__tablename__'])['constrained_columns']
#         elif value == 'i':
#             return [i['column_names'][0] for i in self.inspect.get_indexes(self.cls.__dict__['__tablename__'])]
#         elif value == 'c':
#             return [i['name'] for i in self.inspect.get_columns(self.cls.__dict__['__tablename__'])]
#
#     def table(self, log=father):
#         l = log.child()
#         return self.query('t', log=l)
#
#     def keys(self, log=father):
#         l = log.child()
#         return self.query('k', log=l)
#
#     def indexes(self, log=father):
#         l = log.child()
#         return self.query('i', log=l)
#
#     def columns(self, log=father):
#         l = log.child()
#         return self.query('c', log=l)
#     def query(self, value, *args, log=father):
#         l = log.child()
#         print(self.ses.query(self.cls).all())
#         print(getattr(self.cls, 'url'))
#         print(self.ses.query(getattr(self.cls, 'url')).all())
#         print(args)
#         parser = argparse.ArgumentParser()
#         args = []
#         for i in self.get('k'):
#             print(i)
#             args.append(getattr(self.cls, str(i)))
#         i = 'url'
#         print(getattr(self.cls, i))
#
#         print(args[0])
#         print(self.ses.query(args[0]).all()[0][0])
#         print('---')
#         print(self.ses.query(*args).all()[0][0])
#         print('---')
#
#         print(getattr(self.cls, 'url'))
#         print(self.ses.query(getattr(self.cls, 'url')).all()[0][0])
#         # print(self.ses.query(args).all())
#         try:
#             if value == 't':
#                 res = self.ses.query(self.cls).all()
#             elif value == 'k':
#                 res = self.ses.query([self.cls.__dict__[i] for i in self.get('k')]).all()
#             elif value == 'i':
#                 res = self.ses.query([getattr(self.cls, i) for i in self.get('i')]).all()
#             elif value == 'c':
#                 res = self.ses.query([getattr(self.cls, i) for i in self.get('c')]).all()
#             else:
#                 res = self.ses.query([getattr(self.cls, i) for i in args]).all()
#         except sqlalchemy.orm.exc.NoResultFound:
#             l.c('NoResultFound: session.query(table == {}'.format(self.child_tablename))
#             self.close(l)
#             raise
#         except sqlalchemy.exc.OperationalError or sqlite3.OperationalError as exc:
#             l.c('session.query(): {}'.format(repr(exc)))
#             self.close(l)
#             raise
#         else:
#             l.i('SUCCESSFUL: session.query(table == {}'.format(self.child_tablename))
#             if not res:
#                 l.c('NO ROWS: query(table == {}'.format(self.child_tablename))
#             return res
#
#     def add(self, instance, _warn=True):
#         return self.ses.add(instance, _warn=True)
#
#     def add_all(self, instances):
#         return self.ses.add_all(instances)
#
#     def commit(self, log=father):
#         l = log.child()
#
#         try:
#             self.ses.commit()
#         except sqlalchemy.exc.IntegrityError or sqlite3.IntegrityError as exc:
#             if 'UNIQUE constraint failed: {}.{}'.format(self.child_tablename, 'url') in repr(exc):
#                 l.e('session.commit(): {}'.format(repr(exc)))
#                 self.ses.rollback()
#                 l.i('SUCCESSFUL: session.rollback()')
#             else:
#                 l.c('session.commit(): {}'.format(repr(exc)))
#                 self.ses.rollback()
#                 l.i('SUCCESSFUL: session.rollback()')
#                 self.ses.close()
#                 l.i('SUCCESSFUL: session.close()')
#                 raise
#         except sqlalchemy.exc.InvalidRequestError as exc:
#             l.e('session.commit(): {}'.format(repr(exc)))
#             self.ses.rollback()
#             l.i('SUCCESSFUL: session.rollback()')
#         else:
#             l.i('SUCCESSFUL: session.commit()')
#
#     def close(self, log=father):
#         l = log.child()
#
#         self.commit()
#         self.ses.close()
#         l.i('SUCCESSFUL: session.close()')
