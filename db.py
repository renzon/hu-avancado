from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    fullname = Column(String(200))
    password = Column(String(200))

    def __repr__(self):
        return (
            f'User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}, '
            f'password={self.password!r})   '
        )


print(repr(User.__table__))

# print('Creating Metadata')
#
# Base.metadata.create_all(engine)
#
# ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
#
# print(f"User's name: {ed_user.name}")
# print(f"User's id before saving: {ed_user.id}")
#
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
#
# session = Session()
# print('Adding Ed to session')
#
# session.add(ed_user)
# print()
# print('Querying user')
#
# first_user = session.query(User).filter_by(name='ed').first()
# print(f'Is Ed the first user? {ed_user==first_user}')
#
# print()
#
# print('Adding 3 users')
# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', password='foobar'),
#     User(name='mary', fullname='Mary Contrary', password='xxg527'),
#     User(name='fred', fullname='Fred Flinstone', password='blah')
# ])
#
# print("Changing Ed's password")
# ed_user.password = 'f8s7ccs'
#
# print("What's changed?", repr(session.dirty))
# print("What's new?", repr(session.new))
# print('Commit everything')
# session.commit()
#
# print()
# print(f"User's id after saving: {ed_user.id}")
# print(f"Changing Ed's name to Edwardo")
# ed_user.name = 'Edwardo'
# fake_user = User(name='fakeuser', fullname='Invalid', password='12345')
# session.add(fake_user)
# print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())
#
# print()
# print('Rolling Back')
# session.rollback()
# print(ed_user.name)
# print(fake_user in session)
# print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())
#
# print()
# print('Querying')
#
# for instance in session.query(User).order_by(User.id):
#     print(instance.name, instance.fullname)
#
# print()
# print('Querying columns')
# for name, fullname in session.query(User.name, User.fullname):
#     print(name, fullname)
#
# print()
# print('Named Tuples')
# for row in session.query(User, User.name).all():
#     print(row.User, row.name)
#
# print()
# print('Renaming Columns')
# for row in session.query(User.name.label('name_label')).all():
#     print(row.name_label)
#
# print()
# print('Using aliases')
# from sqlalchemy.orm import aliased
#
# user_alias = aliased(User, name='user_alias')
# for row in session.query(user_alias, user_alias.name).all():
#     print(row.user_alias)
#
# print()
# print('Limit and offset')
#
# for u in session.query(User).order_by(User.id)[1:3]:
#     print(u)
#
# print()
# print('Filtering')
# for name, in session.query(User.name). \
#         filter(User.fullname == 'Ed Jones'):
#     print(name)
#
# print()
# print('First column of unique row')
# query = session.query(User.id).filter(User.name == 'ed').order_by(User.id)
# print(query.scalar())
#
# print()
# print('Textual SQL')
# from sqlalchemy import text
#
# for user in session.query(User).filter(text("id<224")).order_by(text("id")).all():
#     print(user.name)
#
# print()
# print('Binding parameters')
# session.query(User).filter(text("id<:value and name=:name")). \
#     params(value=224, name='fred').order_by(User.id).one()
#
# print()
# print('Raw select matching model')
# session.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(
#     name='ed').all()
#
# print()
# print('Manual column match')
# stmt = text("SELECT name, id, fullname, password FROM users where name=:name")
# stmt = stmt.columns(User.name, User.id, User.fullname, User.password)
# session.query(User).from_statement(stmt).params(name='ed').all()
#
# print()
# print('Counting (Subquery)')
# session.query(User).filter(User.name.like('%ed')).count()
#
# print()
#
# print('Counting element')
# from sqlalchemy import func
#
# print(session.query(func.count(User.name), User.name).group_by(User.name).all())
#
# print()
# print('Counting with simple query')
# print(session.query(func.count('*')).select_from(User).scalar())
# print(session.query(func.count(User.id)).scalar())
#
# print()
# print('Relationships')
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
#
#
# class Address(Base):
#     __tablename__ = 'addresses'
#     id = Column(Integer, primary_key=True)
#     email_address = Column(String, nullable=False)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="addresses")
#
#     def __repr__(self):
#         return "<Address(email_address='%s')>" % self.email_address
#
#
# User.addresses = relationship(
#     "Address", order_by=Address.id, back_populates="user")
# print()
# print('Creation Address')
# Base.metadata.create_all(engine)
#
# jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
# print(jack.addresses)
#
# jack.addresses = [
#     Address(email_address='jack@google.com'),
#     Address(email_address='j25@yahoo.com')
# ]
# print()
#
# print('Bidrecional relationship')
#
# print(jack.addresses[1])
# print(jack.addresses[1].user)
#
# session.add(jack)
# session.commit()
# print()
#
# print('Lazy loading')
# jack = session.query(User).filter_by(name='jack').one()
# print(jack)
# print(jack.addresses)
# print()
#
# print('Querying User and Address')
# for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(
#         Address.email_address == 'jack@google.com').all():
#     print(u, a)
# print()
#
# print('####### n+1 select issue')
# for user in session.query(User):
#     print(user, user.addresses)
# print()
#
# print('####### Avoiding issue')
# for user in session.query(User).join(Address, User.addresses):
#     print(user, user.addresses)
#
# print()
#
# print('Using aliases for multiple joins')
# adalias1 = aliased(Address)
# adalias2 = aliased(Address)
# for username, email1, email2 in \
#         session.query(User.name, adalias1.email_address, adalias2.email_address). \
#                 join(adalias1, User.addresses). \
#                 join(adalias2, User.addresses). \
#                 filter(adalias1.email_address == 'jack@google.com'). \
#                 filter(adalias2.email_address == 'j25@yahoo.com'):
#     print(username, email1, email2)
#
# print()
# print('Subqueries')
#
# stmt = session.query(
#     Address.user_id,
#     func.count('*').label('address_count')
# ).group_by(Address.user_id).subquery()
#
# print()
# print('Attributes accessible through c')
#
# for u, count in session.query(User, stmt.c.address_count).outerjoin(
#         stmt, User.id == stmt.c.user_id).order_by(User.id):
#     print(u, count)
#
# print()
# print('Aliasing to map subclasses')
#
# stmt = session.query(Address).filter(Address.email_address != 'j25@yahoo.com').subquery()
# adalias = aliased(Address, stmt)
#
# for user, address in session.query(User, adalias).join(adalias, User.addresses):
#     print(user)
#     print(address)
#
# print()
# print('Subquery load')
#
# from sqlalchemy.orm import subqueryload
#
# jack = session.query(User).options(subqueryload(User.addresses)).filter(User.name == 'jack').one()
# print(jack)
# print(jack.addresses)
#
# print()
# print('Joinedload')
#
# from sqlalchemy.orm import joinedload
#
# jack = session.query(User).options(joinedload(User.addresses)).filter(User.name == 'jack').one()
# print(jack)
# print(jack.addresses)
#
# print()
# print('Join + Eagerload')
#
# from sqlalchemy.orm import contains_eager
#
# jacks_addresses = session.query(Address).join(Address.user).filter(User.name == 'jack').options(
#     contains_eager(Address.user)).all()
# print(jacks_addresses)
# print(jacks_addresses[0].user)
