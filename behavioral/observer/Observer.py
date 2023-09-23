from abc import ABCMeta, abstractmethod

class NewsAgency:

    def __init__(self):
        self.__subscribers = []
        self.__last_news = None
    
    def register(self, subscribed) -> bool:
        self.__subscribers.append(subscribed)
        return True
    
    def unsubscribe(self, subscribed) -> bool:

        for subs in self.__subscribers:
            
            if (subs == subscribed):
                self.__subscribers.remove(subs)
        
        return True
    
    def notify_all(self) -> bool:

        for subs in self.__subscribers:
            subs.notify()
    
    def add_news(self, news):
        self.__last_news = news


class Subscription(metaclass=ABCMeta):

    @abstractmethod
    def notify(self) -> bool:
        pass


class SMSSubscription(Subscription):

    def __init__(self, news_agency: NewsAgency):
        self.__news_agency = news_agency
        self.__news_agency.register(self)

    def notify(self) -> bool:
        ...

class EmailSubscription(Subscription):

    def __init__(self, news_agency: NewsAgency):
        self.__news_agency = news_agency
        self.__news_agency.register(self)

    def notify(self) -> bool:
        ...

class CellphoneSubscription(Subscription):

    def __init__(self, news_agency: NewsAgency):
        self.__news_agency = news_agency
        self.__news_agency.register(self)

    def notify(self) -> bool:
        ...


if __name__ == '__main__':

    news_agency: NewsAgency = NewsAgency()

    sms: Subscription = SMSSubscription(news_agency)
    email: Subscription = EmailSubscription(news_agency)
    cellphone: Subscription = CellphoneSubscription(news_agency)

    news_agency.add_news('This is a new news...')
    news_agency.notify_all()

    unsubs: bool = news_agency.unsubscribe(cellphone)

    print(unsubs)