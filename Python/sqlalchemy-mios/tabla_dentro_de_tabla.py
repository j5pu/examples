from utils import config
from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.collections import attribute_mapped_collection

from sqlalchemy_utils import generic_repr, URLType, PhoneNumberType, force_instant_defaults, EmailType, ChoiceType, \
    aggregated
import sqlalchemy
import sqlalchemy.exc
import sqlalchemy.orm
from furl import furl

ini, log, Base, engine, Session = config()

session = Session()

@generic_repr
class Url(Base):
    __tablename__ = 'url'
    id = Column(Integer, primary_key=True)
    url = Column(String(128))
    domain = Column(String(32))
    site = Column(Boolean)  # True: site, False: page
    browser = Column(Boolean)  # True: selenium, False: aiohttp
    click = Column(String(32))  # None: <Scroll>, Value: Click
    times_max = Column(Integer)  # Max number of scroll or clicks
    times_real = Column(Integer)  # Real number of scroll or clicks

    megagroup_id = relationship(
        "Url",
        cascade="all, delete-orphan",
        backref=backref("parent", remote_side=url),
        collection_class=attribute_mapped_collection('megagroup_url'),
    )
    # Nota: Child
    parent_url = Column(String(128), ForeignKey(url))
    megagroup_url = Column(String(128))

    def __init__(self, url=None, parent=None, domain=None, site=None, browser=None, click=None, times_max=None,
                 times_real=None,
                 megagroup_url=None):
        self.url = url
        self.domain = domain
        if url:
            self.domain = furl(self.url).host
        self.parent = parent
        self.site = site
        self.browser = browser
        self.click = click
        self.times_max = times_max
        self.times_real = times_real
        self.megagroup_url = megagroup_url



Base.metadata.create_all(engine)
# Nota: Creo PADRE
url = 'https://icorating.com/ico/all'
padre = Url(url, site=True, browser=True, click=None, times_max=180, times_real=161)
session.add(padre)

# Nota: Creo HIJOS
t = 'https:t.me/icorating'
t2 = 'https:t.me/com'

session.add_all([Url(parent=padre, megagroup_url=t), Url(parent=padre, megagroup_url=t2)])
session.commit()

# Nota: Creo PADRE
url = 'https://www.trackico.io'
padre = Url(url, site=True, browser=True, click=None, times_max=180, times_real=161)

# Nota: Creo HIJOS
t = 'https:t.me/trackico'
# Con Url() sin asignar objeto = Url() tengo que hacer:
#       Url() - session.add() - session.commit() sino solo hace commit del ultimo.
hijo1 = Url(parent=padre, megagroup_url=t)
t = 'https:t.me/io'
hijo2 = Url(parent=padre, megagroup_url=t)
session.add_all([padre, hijo1, hijo2])

session.commit()

# Nota: borro una de telegram sola
t = 'https:t.me/io'
session.query(Url).filter_by(megagroup_url=t).delete(synchronize_session=False)
# Tambien se puede hacer si hay uno solo con la key y session.delete:
#       uno = session.query(Url).filter_by(url=t).scalar()
#       session.delete(uno)
session.commit()

# Nota: borro HIJOS de PADRE
url = 'https://icorating.com/ico/all'
# Estas dos queries iguales (pero al borrar quitar.all())
#       session.query(Url).filter_by(parent_id=url).all()
#       session.query(Url).filter(Url.parent_id==url).all()
session.query(Url).filter(Url.parent_url==url).delete(synchronize_session=False)
session.commit()

# Nota: Borro PADRE:
# Nota:             query().delete() borra mas de uno, pero no borra hijos
# Nota:             session.delete() borra uno, pero borra hijos

url = 'https://www.trackico.io'
padre = session.query(Url).filter(Url.url==url).one()
# Como hay columnas con <None> de los hijos se queja con warning, pero lo hace bien al salir una
# y descartar las de los hijos.
#       SAWarning: Got None for value of column url.url;
session.delete(padre)
session.commit()

url = 'https://icorating.com/ico/all'
# session.query(Url).filter(Url.url==url).delete(synchronize_session=False)
padre = session.query(Url).filter_by(url=url).scalar()
# Solo funciona borrando los hijos cuando hay uno solo.
# si hay mas de uno hay que usar el .delete() pero no borra los hijos.

session.delete(padre)
session.commit()
exit(0)

