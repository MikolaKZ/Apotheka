import os,sys
basedir=os.path.abspath(os.path.dirname(__file__))
lib_path=os.path.join(basedir,'..','webapp')
sys.path.append(lib_path)
from model import TelegramChat
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI


def setDBUserPassword(psw, chat_id):
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        print(session.query(TelegramChat).filter_by(id=chat_id))
        telegramChat = session.query(TelegramChat).filter_by(id=chat_id).first() 
        
        if telegramChat:
            telegramChat.psw=psw
            session.commit()
        else:
            telegramChat = TelegramChat(id=chat_id,psw=psw,alarm=True)
            session.add(telegramChat)
            session.commit()
        return True
    except:
        print (sys.exc_info())
        return False
    
    