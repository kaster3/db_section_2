from datetime import date as _date
from sqlalchemy import String, func, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db.models.base import Base


class SpimexTradingResult(Base):

    __table_args__ = (CheckConstraint("count >= 0", name="check_count_positive"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    exchange_product_id: Mapped[str] = mapped_column(String(100))
    exchange_product_name: Mapped[str] = mapped_column(String(100))
    oil_id: Mapped[str] = mapped_column(String(4))  # exchange_product_id[:4]
    delivery_basis_id: Mapped[str] = mapped_column(
        String(3)
    )  # exchange_product_id[4:7]
    delivery_basis_name: Mapped[str] = mapped_column(String(200))
    delivery_type_id: Mapped[str] = mapped_column(String(1))  # exchange_product_id[-1]

    volume: Mapped[int] = mapped_column(
        nullable=False
    )  # Объем Договоров в единицах измерения.
    total: Mapped[int] = mapped_column(nullable=False)  # Объем Договоров, руб.
    count: Mapped[int] = mapped_column(nullable=False)  # Количество Договоров, шт.

    date: Mapped[_date] = mapped_column(nullable=False)
    created_on: Mapped[_date] = mapped_column(
        insert_default=func.now(),
        nullable=False,
    )
    updated_on: Mapped[_date] = mapped_column(
        insert_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
