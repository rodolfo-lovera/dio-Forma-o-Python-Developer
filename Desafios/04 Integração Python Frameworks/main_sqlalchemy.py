from matplotlib.pyplot import connect
from sqlalchemy import(
    create_engine, Column, Integer, String, inspect, ForeignKey, Select, func
)
from sqlalchemy.orm import(
    declarative_base, relationship, Session
)

engine = create_engine('sqlite:///memory')
Base = declarative_base()

class Cliente(Base):
    # Criação da estrutura da tabela Cliente
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = relationship("Conta", back_populates='cliente')

class Conta(Base):
    # Criação da estrutura da tabela Conta
    __tablename__ = 'conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=True)
    agencia = Column(String)
    num = Column(Integer, nullable=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"),nullable=False)

    cliente = relationship("Cliente", back_populates="endereco")

def cria_tabelas():
    # Geração das tabelas

    Base.metadata.create_all(engine)

cria_tabelas()

insp = inspect(engine)
print(insp.get_table_names())

# Inserção de dados nas tabelas

with Session(engine) as session:
    clienteAAA = Cliente(
        nome="AAAAA AAAAA",
        cpf="12345678901",
        endereco = [Conta(agencia='0001')]
    )
    clienteBBB = Cliente(
        nome="BBBBB BBBBB",
        cpf="23456789012",
        endereco = [Conta(agencia='0001')]
    )
    clienteCCC = Cliente(
        nome="CCCCC CCCCC",
        cpf="34567890123",
        endereco = [Conta(agencia='0001')]
    )

session.add_all([clienteAAA,clienteBBB,clienteCCC])

session.commit()

print(select(Cliente))
stmt = select(Cliente)

connection = engine.connect()
results = connection.execute(stmt).fetchall()

for result in results:
    print(result)
    
stmt_count = select(func.count('*')).select_from(Cliente)
results = connection.execute(stmt_count).fetchall
for result in results:
    print(result)

stmt_where = select(Cliente).where(Conta.id.in_([2]))
results = connection.execute(stmt_where).fetchall()
for result in results:
    print(result)