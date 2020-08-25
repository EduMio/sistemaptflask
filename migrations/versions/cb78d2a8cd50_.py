"""empty message

Revision ID: cb78d2a8cd50
Revises: 
Create Date: 2020-08-25 17:01:56.380023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb78d2a8cd50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ej',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('imagem', sa.String(), nullable=True),
    sa.Column('cnpj', sa.String(), nullable=True),
    sa.Column('projetos_meta', sa.Integer(), nullable=True),
    sa.Column('faturamento_meta', sa.Integer(), nullable=True),
    sa.Column('projetos_atual', sa.Integer(), nullable=True),
    sa.Column('faturamento_atual', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cnpj'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('tarefa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.Column('icone', sa.String(), nullable=True),
    sa.Column('prazo', sa.String(), nullable=True),
    sa.Column('ehSolo', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('titulo')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=255), nullable=True),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.Column('urole', sa.String(length=50), server_default='user', nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('active', sa.Boolean(), server_default=sa.text('1'), nullable=True),
    sa.Column('foto_trainee', sa.String(length=120), nullable=True),
    sa.Column('ej_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ej_id'], ['ej.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('login')
    )
    op.create_table('tarefaTrainee',
    sa.Column('id_trainee', sa.Integer(), nullable=False),
    sa.Column('id_tarefa', sa.Integer(), nullable=False),
    sa.Column('atrasada', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['id_tarefa'], ['tarefa.id'], ),
    sa.ForeignKeyConstraint(['id_trainee'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id_trainee', 'id_tarefa')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarefaTrainee')
    op.drop_table('usuario')
    op.drop_table('tarefa')
    op.drop_table('ej')
    # ### end Alembic commands ###