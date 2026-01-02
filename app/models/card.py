import uuid
from decimal import Decimal
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Boolean, String, ForeignKey, Integer, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Card(Base):
    __tablename__ = "cards"
    id_card: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    id_user: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id_user"), nullable=False)
    id_bank: Mapped[uuid.UUID] = mapped_column(ForeignKey("banks.id_bank"), nullable=False)
    id_currency: Mapped[uuid.UUID] = mapped_column(ForeignKey("currency.id_currency"), nullable=False)
    id_card_type: Mapped[uuid.UUID] = mapped_column(ForeignKey("card_types.id_card_type"), nullable=False)

    last_digits: Mapped[int] = mapped_column(Integer, nullable=False)
    alias: Mapped[str] = mapped_column(String, nullable=False)
    current_balance: Mapped[Decimal | None] = mapped_column(Numeric(18, 2), nullable=True)
    credit_limit: Mapped[Decimal | None] = mapped_column(Numeric(18, 2), nullable=True)   # solo crédito
    credit_used: Mapped[Decimal | None] = mapped_column(Numeric(18, 2), nullable=True)   # solo crédito

    cut_day: Mapped[int | None] = mapped_column(Integer, nullable=True)
    payment_due_day: Mapped[int | None] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
