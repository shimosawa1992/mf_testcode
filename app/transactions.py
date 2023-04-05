from db import get_session, engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, func


baseModel = automap_base()

class transactions(baseModel):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)

baseModel.prepare(engine, reflect=True)

# 取引履歴を保存
def save_transaction(params):
    session = get_session()
    transaction = transactions()
    transaction.user_id = params.user_id
    transaction.amount = params.amount
    transaction.description = params.description
    session.add(transaction)
    session.commit()

# ユーザー別の取引額合計を取得
def get_total_transactios(user_id): 
    session = get_session()
    total = session.query(func.sum(transactions.amount)).\
    filter(transactions.user_id == user_id).\
    first()

    if total[0] == None:
        return 0
    else:
        return total[0]