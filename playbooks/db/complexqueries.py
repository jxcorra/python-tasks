from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Float, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, backref
from sqlalchemy_utils import create_database, database_exists
import environ


env = environ.Env()
env.read_env()

DB_USER: str = env.str('DB_USER')
DB_PASSWORD: str = env.str('DB_PASSWORD')
DB_NAME: str = env.str('DB_NAME')
DB_HOST: str = env.str('DB_HOST')
DB_PORT: int = env.int('DB_PORT')
DB_ECHO: bool = env.bool('DB_ECHO')

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=DB_ECHO)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)

    artist = relationship('Artist', foreign_keys='Album.artist_id', backref='albums')


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

artist = Artist(name='MyBand')
album = Album(name='MyAlbum', artist=artist)

session.add_all([artist, album])
session.commit()


class Booklet(Base):
    __tablename__ = 'booklet'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    album_id = Column(Integer, ForeignKey('album.id'), nullable=False)

    album = relationship('Album', foreign_keys='Booklet.album_id', backref=backref('booklet', uselist=False))


Base.metadata.create_all(engine)

booklet = Booklet(description='blabla', album=album)
print(album.booklet.description)
print(booklet.album.name)


association_table = Table(
    'association',
    Base.metadata,
    Column('album_id', Integer, ForeignKey('album.id')),
    Column('track_id', Integer, ForeignKey('track.id'))
)


class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Float)
    albums = relationship('Album', secondary=association_table, backref='tracks')


Base.metadata.create_all(engine)