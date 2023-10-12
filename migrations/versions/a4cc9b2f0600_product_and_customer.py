"""product and customer

Revision ID: a4cc9b2f0600
Revises: 1065d00686a9
Create Date: 2023-08-25 10:12:29.602766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4cc9b2f0600'
down_revision = '1065d00686a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('address_1', sa.String(length=255), nullable=True),
    sa.Column('address_2', sa.String(length=255), nullable=True),
    sa.Column('district', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('pin', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile_number')
    )
    op.create_table('state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('district',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('state', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['state'], ['state.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplier', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['supplier'], ['agency.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('customer', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('invoice', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile_number')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('units', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('discount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('tax', sa.String(length=255), nullable=True),
    sa.Column('hsn', sa.String(length=255), nullable=True),
    sa.Column('brand', sa.String(length=255), nullable=True),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.Column('sub_category', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['productcat.id'], ),
    sa.ForeignKeyConstraint(['sub_category'], ['productsubcat.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'sub_category', name='uq_name_sub_category')
    )
    op.create_table('purchaseproducts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('purchase', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('units', sa.String(length=255), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['purchase'], ['purchase.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('product', sa.Integer(), nullable=False),
    sa.Column('supplier', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.ForeignKeyConstraint(['supplier'], ['agency.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sale_products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile_number', sa.Integer(), nullable=True),
    sa.Column('units', sa.String(length=255), nullable=True),
    sa.Column('sales', sa.Integer(), nullable=True),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('tax', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product'], ['product.id'], ),
    sa.ForeignKeyConstraint(['sales'], ['sales.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mobile_number')
    )
    op.drop_constraint('productsubcat_name_key', 'productsubcat', type_='unique')
    op.create_unique_constraint('uq_name_category', 'productsubcat', ['name', 'category'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_name_category', 'productsubcat', type_='unique')
    op.create_unique_constraint('productsubcat_name_key', 'productsubcat', ['name'])
    op.drop_table('sale_products')
    op.drop_table('product_stock')
    op.drop_table('purchaseproducts')
    op.drop_table('product')
    op.drop_table('sales')
    op.drop_table('purchase')
    op.drop_table('district')
    op.drop_table('state')
    op.drop_table('customer')
    # ### end Alembic commands ###