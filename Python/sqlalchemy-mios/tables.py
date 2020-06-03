from config import Base
from sqlalchemy import create_engine, ForeignKey, MetaData, Table, func, Float, exc, Boolean, \
    Integer, Column, String, Text, select, event, and_, or_, inspect, DateTime, case, ForeignKeyConstraint
from sqlalchemy.exc import NoSuchTableError, StatementError

from sqlalchemy.ext.declarative import as_declarative, declarative_base, \
    declared_attr, ConcreteBase
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.instrumentation import InstrumentationManager

from sqlalchemy.orm import Session, relationship, joinedload_all, \
    foreign, remote, mapper, backref, sessionmaker, with_polymorphic, join, aliased, \
    query, make_transient, attributes, validates, column_property
from sqlalchemy.orm.collections import attribute_mapped_collection, MappedCollection
from sqlalchemy.orm.attributes import set_attribute, get_attribute, \
    del_attribute
from sqlalchemy.orm.instrumentation import is_instrumented

from sqlalchemy.schema import CreateTable, DropTable
from sqlalchemy.sql.type_api import TypeDecorator

from alchio import ASYNCIO_STRATEGY
from alchio.base import AsyncConnection, AsyncResultProxy, AsyncTransaction


class Config(Base):
    __tablename__ = 'config'
    key = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), primary_key=True, nullable=False)
    strategy = Column(String(255), default=1)
    description = Column(String(255))
    batch_size = Column(Integer, default=100, comment='size (in # of items) '
                                                      'of batch to be retrieved from the server '
                                                      'on each request -extract- '
                                                      '(default: 100 items)')
    batch_time = Column(Integer, default=1, comment='time (in # seconds) to sleep after a batch of '
                                                    'items is retrieved from the server -extract- '
                                                    '(default: 1 second)')
    message_time = Column(Integer, default=3, comment='time (in # seconds) to sleep after every channel '
                                                      '(un)subscription is done -extract/send- '
                                                      '(default: 30 second)')
    channel_time = Column(Integer, default=30, comment='time (in # seconds) to sleep after every message '
                                                       'is sent out -send-'
                                                       '(default: 3 second)')
    capacity = Column(Integer, default=1)
    log_level = Column(String(255), default='DEBUG')
    dry_run = Column(Boolean, default=True)

    def __init__(self, key, name, strategy, description, batch_size=100,
                 batch_time=1, message_time=3, channel_time=30,
                 capacity=1, log_level='DEBUG', dry_run=True):
        self.key = key
        self.name = name
        self.strategy = strategy
        self.description = description
        self.batch_size = batch_size
        self.batch_time = batch_time
        self.message_time = message_time
        self.channel_time = channel_time
        self.capacity = capacity
        self.log_level = log_level
        self.dry_run = dry_run

    def __repr__(self):
        return "Config(name={}, strategy={}, description={}, batch_size={}, batch_time={}, " \
               "message_time={}, channel_time={}, capacity={}, log_level={}, dry_run={})".\
            format(
                self.id,
                self.name,
                self.strategy,
                self.description,
                self.batch_size,
                self.batch_time,
                self.message_time,
                self.channel_time,
                self.capacity,
                self.log_level,
                self.dry_run
            )


class MegaGroups(Base):
    __tablename__ = 'megagroups'
    key = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    url = Column(String(255), primary_key=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    hash = Column(Integer)

    megagroupsusers = relationship("MegaGroupsUsers", lazy="dynamic", cascade="all, delete-orphan")
    megagroupsurls = relationship("MegaGroupsUrls", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, url, id, hash):
        self.url = url
        self.id = id
        self.hash = hash

    def __repr__(self):
        return "MegaGroups(url={}".format(self.url)

    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
            "\n" + \
            "".join([
                c.dump(_indent + 1)
                for c in self.megagroupsusers.values()
            ])


class MegaGroupsUrls(Base):
    __tablename__ = 'megagroupsurls'
    key = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    megagroups_key = Column(Integer, ForeignKey('megagroups.key'))

    url = Column(String(255), primary_key=True, nullable=False)
    valid = Column(Boolean, nullable=False, default=True)

    def __init__(self, url):
        self.url = url

class MegaGroupsUsers(Base):
    __tablename__ = 'megagroupsusers'
    key = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    megagroups_key = Column(Integer, ForeignKey('megagroups.key'))
    users_key = Column(Integer, ForeignKey('users.key'))


    def __init__(self, member, parent_id):
        self.parent_id = parent_id
        self.member = member

    def __repr__(self):
        return "Groups(parent_id={}, member={}".format(
            self.parent_id,
            self.member
        )

class Users(Base):
    __tablename__ = 'users'
    key = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    hash = Column(Integer)
    username = Column(String(50))
    firstname = Column(String(50))
    lastname = Column(String(50))

    megagroupsusers = relationship("MegaGroupsUsers", lazy="dynamic", cascade="all, delete-orphan")


    def __init__(self, member, parent_id):
        self.parent_id = parent_id
        self.member = member

    def __repr__(self):
        return "Users(parent_id={}, member={}".format(
            self.parent_id,
            self.member
        )


class Campaings(Base):
    __tablename__ = 'campaings'
    key = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(255))
    phoneusername = relationship("CampaingsPhonesUsernames", lazy="dynamic", cascade="all, delete-orphan")
    messages = relationship("CampaingsMessages", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Campaings(name={}".format(self.name)

    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
            "\n" + \
            "".join([
                c.dump(_indent + 1)
                for c in self.messages.values()
            ])

class CampaingsPhonesUsernames(Base):
    __tablename__ = 'campaingsphoneusernames'
    key = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    phoneusername = Column(String(255), ForeignKey('campaings.key'), primary_key=True, unique=True, nullable=False)

    messages = relationship("CampaingsMessages", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "Campaings(username={}".format(self.username)

    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
            "\n" + \
            "".join([
                c.dump(_indent + 1)
                for c in self.messages.values()
            ])

class CampaingsMessages(Base):
    __tablename__ = 'campaingsmessages'
    key = Column(Integer, primary_key=True, autoincrement=True)
    campaings_key = Column(Integer, ForeignKey('campaings.key'))
    campaings_pictures_key = Column(Integer, ForeignKey('campaingspictures.key'))
    name = Column(String(255))
    message = Column(String(255))
    percentage = Column(Integer)
    url = Column(String(255))
    picture = Column(String(255)) # Nota: imagen nesteada o algo por si se repiten a una de fotos

    stats = relationship("CampaingsStats", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, parent_id, name, percentage, message, url, picture):
        self.name = parent_id
        self.name = name
        self.percentage = percentage
        self.message = message
        self.url = url
        self.picture = picture

    def __repr__(self):
        return "Groups(name={}, percentage={}, url={}, picture={}".format(
            self.parent_id,
            self.name,
            self.percentage,
            self.message,
            self.url,
            self.picture
        )

    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
            "\n" + \
            "".join([
                c.dump(_indent + 1)
                for c in self.stats.values()
            ])


class CampaingsPictures(Base):
    __tablename__ = 'campaingspictures'
    key = Column(Integer, primary_key=True, autoincrement=True)
    campaings_key = Column(Integer, ForeignKey('campaings.key'))
    name = Column(String(255))
    url = Column(String(255))
    picture = Column(String(255)) # Nota: imagen nesteada o algo por si se repiten a una de fotos

    stats = relationship("CampaingsMessages", lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, parent_id, name, percentage, message, url, picture):
        self.name = parent_id
        self.name = name
        self.percentage = percentage
        self.message = message
        self.url = url
        self.picture = picture

    def __repr__(self):
        return "CampaingsPictures(name={}, percentage={}, url={}, picture={}".format(
            self.parent_id,
            self.name,
            self.percentage,
            self.message,
            self.url,
            self.picture
        )

    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
            "\n" + \
            "".join([
                c.dump(_indent + 1)
                for c in self.stats.values()
            ])


class CampaingsStats(Base):
    __tablename__ = 'campaingsstats'
    key = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey('campaingsmessages.id'))

    icossubscribed = Column(Integer, comment='Number of successful subscriptions to ICO megagroups')
    icosunsubscribed = Column(Integer, comment='Number of successful unsubscriptions from ICO '
                                               'megagroups channelnotexistenterror')
    channelnotexistenterror = Column(Integer, comment='Number of ICO urls not existing in Telegram '
                                                      'but included in txt file')
    unexpectedrpcerror = Column(Integer, comment='Number of RPC errors received not expected explicitly')
    participantsretrieved = Column(Integer, comment='Number of participants retrieved from server')
    participantscontactedtotal = Column(Integer, comment='Number of ICO participants contacted so far')
    participantscontactedok = Column(Integer, comment='Number of ICO participants successfully '
                                                      'contacted so far')
    participantscontactedko = Column(Integer, comment='Number of ICO participants unsuccessfully '
                                                      'contacted so far (400, Bad Request RPC Error)')
    userunauthorizedflooderror = Column(Integer, comment='Number of flood errors received when trying '
                                                         'to authorize user (420, Flood Wait RPC Error)')
    joinchannelrequestflooderror = Column(Integer, comment='Number of flood errors received when trying to subscribe '
                                                           'to ICO megagroup (420, Flood Wait RPC  Error)')
    leavechannelrequestflooderror = Column(Integer, comment='Number of flood errors received when trying to unsubscribe'
                                                            ' from ICO megagroups (420, Flood Wait RPC Error)')
    getparticipantsrequestflooderror = Column(Integer, comment='Number of flood errors received when trying '
                                                               'to get all participants from ICO megagroups '
                                                               '(420, Flood Wait RPC Error)')
    deletehistoryrequestflooderror = Column(Integer, comment='Number of flood errors received when trying to delete '
                                                             'the history associated to a certain participant in '
                                                             'ICO megagroups (420, Flood Wait RPC Error)')
    unexpectederror = Column(Integer, comment='Number of unexpected exceptions received')

    def __init__(self, parent):
        self.parent_id = parent
        self.icossubscribed = 0
        self.icosunsubscribed = 0
        self.channelnotexistenterror = 0
        self.unexpectedrpcerror = 0
        self.participantsretrieved = 0
        self.participantscontactedtotal = 0
        self.participantscontactedok = 0
        self.participantscontactedko = 0
        self.userunauthorizedflooderror = 0
        self.joinchannelrequestflooderror = 0
        self.leavechannelrequestflooderror = 0
        self.getparticipantsrequestflooderror = 0
        self.deletehistoryrequestflooderror = 0
        self.unexpectederror = 0

    def __repr__(self):
        return "Config(parent_id={}, icossubscribed={}, icosunsubscribed={}, channelnotexistenterror={}, " \
            "unexpectedrpcerror={}, participantsretrieved={}, participantscontactedtotal={}, " \
            "participantscontactedok={}, participantscontactedko={}, userunauthorizedflooderror={}, " \
            "joinchannelrequestflooderror={}, leavechannelrequestflooderror={}, " \
            "getparticipantsrequestflooderror={}, deletehistoryrequestflooderror={}, " \
            "unexpectederror={})".\
            format(
                self.parent_id,
                self.icossubscribed,
                self.icosunsubscribed,
                self.channelnotexistenterror,
                self.unexpectedrpcerror,
                self.participantsretrieved,
                self.participantscontactedtotal,
                self.participantscontactedok,
                self.participantscontactedko,
                self.userunauthorizedflooderror,
                self.joinchannelrequestflooderror,
                self.leavechannelrequestflooderror,
                self.getparticipantsrequestflooderror,
                self.deletehistoryrequestflooderror,
                self.unexpectederror
            )
class Emails(Base):
    __tablename__ = 'emails'
    email = Column(String(32), primary_key=True, unique=True, nullable=False)

    bot = relationship("Bots", backref="emails")

    def __init__(self, email):
        self.email = email


    def __repr__(self):
        return "{}(email: {})".format(self.__tablename__, self.email)

    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
            "\n" + \
            "".join([
                c.dump(_indent + 1)
                for c in self.bot.values()
            ])


class Phones(Base):
    __tablename__ = 'phones'
    phone = Column(String(19), primary_key=True, unique=True, nullable=False)

    bot = relationship("Bots",  backref="phones", uselist=False)

    def __init__(self, phone):
        self.phone = phone

    def __repr__(self):
        return "{}(phone: {})".format(self.__tablename__, self.phone)


    def dump(self, _indent=0):
        return "   " * _indent + repr(self) + \
               "\n" + \
               "".join(self.bot.dump(_indent + 1))


class Bots(Base):
    __tablename__ = 'bots'
    api_id = Column(Integer, primary_key=True, unique=True, nullable=False)
    api_hash = Column(String(32), primary_key=True, unique=True, nullable=False)

    phone = Column(String(19), ForeignKey('phones.phone'))
    email = Column(String(32), ForeignKey('emails.email'))


    def __init__(self, api_id=None, api_hash=None):
        self.api_id = api_id
        self.api_hash = api_hash


    def __repr__(self):
        return "{}(api_id: {}, api_hash: {}, phone: {}, email: {})"\
            .format(self.__tablename__, self.api_id, self.api_hash, self.phone, self.email)

    def dump(self, _indent=0):
        return "   " * _indent + repr(self)

# create emails
session.add_all(Emails('a1981@tushmail.com'), Emails('b1981@tushmail.com'), Emails('c1981@tushmail.com'),
                Emails('d1981@tushmail.com'), Emails('e1981@tushmail.com'), Emails('f1981@tushmail.com'),
                Emails('fp1981@tushmail.com'), Emails('ivan.mullergomez@yandex.com'))
session.commit()

# create phones
session.add_all(Phones('+12056864923'), Phones('+14805267610'), Phones('+14804368887'), Phones('+14804368909'),
                Phones('+14804395438'), Phones('+14807191900'), Phones('+14806464849'), Phones('+15012467473'),
                Phones('+15012324043'), Phones('+15014996246'), Phones('+15018596601'), Phones('+15017628667'),
                Phones('+12092135309'), Phones('+12094093716'), Phones('+12097835168'), Phones('+12093794179'),
                Phones('+12096768802'), Phones('+12097484715'), Phones('+12094989410'), Phones('+12132613339'),
                Phones('+12132613207'), Phones('+12135148075'), Phones('+13109287096'), Phones('+13107517323'))
session.commit()

session.add_all(Bots('325518', 'f7cacb97cbfcc0caa56e645fb00ef961', ))