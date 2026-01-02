import uuid
from decimal import Decimal
from datetime import datetime, date
from sqlalchemy import ForeignKey, Date, Numeric, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id_transaction: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id_user: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    id_card: Mapped[uuid.UUID] = mapped_column(ForeignKey("cards.id_card"), nullable=False)
    id_category: Mapped[uuid.UUID] = mapped_column(ForeignKey("categories.id_category"), nullable=False)
    id_transaction_type: Mapped[uuid.UUID] = mapped_column(ForeignKey("transaction_type.id_transaction_type"), nullable=False)

    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    transaction_date: Mapped[date] = mapped_column(Date)
    related_transaction_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("transactions.id_transaction"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False
    )
