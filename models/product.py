import sqlalchemy

from db import metadata
from models.enums import RoleType

productcat = sqlalchemy.Table(
    "productcat",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255), unique=True),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
)

productsubcat = sqlalchemy.Table(
    "productsubcat",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255)),
    sqlalchemy.Column("category", sqlalchemy.ForeignKey("productcat.id"), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
    sqlalchemy.UniqueConstraint("name", "category", name="uq_name_category")
)


product = sqlalchemy.Table(
    "product",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255), ),
    sqlalchemy.Column("units", sqlalchemy.String(255), ),
    sqlalchemy.Column("price", sqlalchemy.Numeric(precision=10, scale=2),),
    sqlalchemy.Column("discount", sqlalchemy.Numeric(precision=10, scale=2),),
    sqlalchemy.Column("description", sqlalchemy.Text, ),
    sqlalchemy.Column("tax", sqlalchemy.String(255), ),
    sqlalchemy.Column("hsn", sqlalchemy.String(255), ),
    sqlalchemy.Column("brand", sqlalchemy.String(255), ),
    sqlalchemy.Column("category", sqlalchemy.ForeignKey("productcat.id"), nullable=False),
    sqlalchemy.Column("sub_category", sqlalchemy.ForeignKey("productsubcat.id"), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),
    sqlalchemy.UniqueConstraint( "category","sub_category", "brand","name", name="uq_brand_name_sub_category")

)



product_stock = sqlalchemy.Table(
    "product_stock",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(255), ),
    sqlalchemy.Column("quantity", sqlalchemy.Integer, ),
    sqlalchemy.Column("product", sqlalchemy.ForeignKey("product.id"), nullable=False),
    sqlalchemy.Column("supplier", sqlalchemy.ForeignKey("agency.id"), nullable=False),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=sqlalchemy.func.now()),

)