import sqlalchemy

from db import metadata

customer = sqlalchemy.Table(
    "customer",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("mobile_number", sqlalchemy.Integer, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("email", sqlalchemy.String(255)),
    sqlalchemy.Column("address_1", sqlalchemy.String(255)),
    sqlalchemy.Column("address_2", sqlalchemy.String(255)), 
    sqlalchemy.Column("district", sqlalchemy.String(255)), 
    sqlalchemy.Column("state", sqlalchemy.String(255)), 
    sqlalchemy.Column("pin", sqlalchemy.String(255)), 
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)


sales = sqlalchemy.Table(
    "sales",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("mobile_number", sqlalchemy.Integer),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("customer", sqlalchemy.ForeignKey("customer.id"), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(255)),
    sqlalchemy.Column("invoice", sqlalchemy.String(255)),
    sqlalchemy.Column("balance", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("total", sqlalchemy.Numeric(precision=10, scale=2),nullable=False),
    sqlalchemy.Column("given_amount", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)


sale_products = sqlalchemy.Table(
    "sale_products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("units", sqlalchemy.String(255)),
    sqlalchemy.Column("sales", sqlalchemy.ForeignKey("sales.id")),
    sqlalchemy.Column("product", sqlalchemy.ForeignKey("product.id")),
    sqlalchemy.Column("quantity", sqlalchemy.Integer),
    sqlalchemy.Column("price", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("tax", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)

salesbalancepayment = sqlalchemy.Table(
    "salesbalancepayment",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("sales", sqlalchemy.ForeignKey("sales.id")),
    sqlalchemy.Column("balance", sqlalchemy.Numeric(precision=10, scale=2),nullable=False),
    sqlalchemy.Column("total", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("given_amount", sqlalchemy.Numeric(precision=10, scale=2),nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)