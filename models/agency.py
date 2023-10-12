
import sqlalchemy

from db import metadata
from models.enums import RoleType

agency = sqlalchemy.Table(
    "agency",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(120), unique=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("branch", sqlalchemy.String(255)),
    sqlalchemy.Column("address_1", sqlalchemy.Text),
    sqlalchemy.Column("address_2", sqlalchemy.Text), 
    sqlalchemy.Column("city", sqlalchemy.String(255)), 
    sqlalchemy.Column("district", sqlalchemy.String(255)), 
    sqlalchemy.Column("state", sqlalchemy.String(255)), 
    sqlalchemy.Column("pin", sqlalchemy.String(255)), 
    sqlalchemy.Column("gstin", sqlalchemy.String(255)), 
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
    sqlalchemy.UniqueConstraint("name", "branch", name="uq_name_branch")
)


purchase = sqlalchemy.Table(
    "purchase",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("supplier", sqlalchemy.ForeignKey("agency.id"), nullable=False),
    sqlalchemy.Column("balance", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("total", sqlalchemy.Numeric(precision=10, scale=2),nullable=False),
    sqlalchemy.Column("given", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)


purchaseproducts = sqlalchemy.Table(
    "purchaseproducts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("purchase", sqlalchemy.ForeignKey("purchase.id")),
    sqlalchemy.Column("name", sqlalchemy.String(120)),
    sqlalchemy.Column("description", sqlalchemy.Text),
    sqlalchemy.Column("units", sqlalchemy.String(255)),
    sqlalchemy.Column("quantity", sqlalchemy.Integer),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)

purchasebalancepayment = sqlalchemy.Table(
    "purchasebalancepayment",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("purchase", sqlalchemy.ForeignKey("purchase.id")),
    sqlalchemy.Column("balance", sqlalchemy.Numeric(precision=10, scale=2),nullable=False),
    sqlalchemy.Column("total", sqlalchemy.Numeric(precision=10, scale=2)),
    sqlalchemy.Column("given", sqlalchemy.Numeric(precision=10, scale=2),nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)



state = sqlalchemy.Table(
    "state",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(120)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)



district = sqlalchemy.Table(
    "district",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(120)),
    sqlalchemy.Column("state", sqlalchemy.ForeignKey("state.id"), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)
