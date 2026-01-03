import asyncio
import uuid
from sqlalchemy import select

from app.db.database import AsyncSessionLocal
from app.models.catalogs import TransactionType, CardType, Currency, Bank

async def upsert_by_name(session, model, name_field: str, name_value: str, **extra):
    field = getattr(model, name_field)
    res = await session.execute(select(model).where(field == name_value))
    obj = res.scalar_one_or_none()
    if obj:
        return obj
    obj = model(**extra)
    setattr(obj, name_field, name_value)
    session.add(obj)
    return obj

async def main():
    async with AsyncSessionLocal() as session:
        await upsert_by_name(session, TransactionType, "name", "ingreso", id_transaction_type=uuid.uuid4())
        await upsert_by_name(session, TransactionType, "name", "gasto", id_transaction_type=uuid.uuid4())
        await upsert_by_name(session, TransactionType, "name", "pago", id_transaction_type=uuid.uuid4())

        await upsert_by_name(session, CardType, "type", "credito", id_card_type=uuid.uuid4())
        await upsert_by_name(session, CardType, "type", "debito", id_card_type=uuid.uuid4())

        # currency: usa code como unique
        res = await session.execute(select(Currency).where(Currency.code == "MXN"))
        if not res.scalar_one_or_none():
            session.add(Currency(id_currency=uuid.uuid4(), code="MXN", name="Mexican Peso"))

        res = await session.execute(select(Currency).where(Currency.code == "USD"))
        if not res.scalar_one_or_none():
            session.add(Currency(id_currency=uuid.uuid4(), code="USD", name="US Dollar"))

        await upsert_by_name(session, Bank, "name", "BBVA", id_bank=uuid.uuid4())
        await upsert_by_name(session, Bank, "name", "Santander", id_bank=uuid.uuid4())

        await session.commit()
        print("Seed OK")

if __name__ == "__main__":
    asyncio.run(main())
