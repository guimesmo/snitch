# coding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, Text, String, DateTime, ForeignKey, Boolean)
from sqlalchemy.orm import relationship
from alchimia import TWISTED_STRATEGY

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_email = Column(String(50))
    user_passwd = Column(String(50))
    user_full_name = Column(String(50))
    user_is_active = Column(Boolean(1))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                         self.name, self.fullname, self.password)


class WebSite(Base):
    __tablename__ = 'website'

    website_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class News(Base):
    __tablename__ = 'news'

    news_id = Column(Integer, primary_key=True)

    url = Column(String(800), nullable=False)
    title = Column(String(300), nullable=False)
    body = Column(Text(), nullable=False)  # Must preserve the pharagraphs
    post_date = Column(DateTime, nullable=False)
    author = Column(String(50), nullable=False)

    website_id = Column(Integer, ForeignKey('website.website_id'))
    website = relationship(WebSite, lazy='joined')


class Source(News):
    __tablename__ = 'source'

    source_id = Column(Integer, primary_key=True)

    url = Column(String(800), nullable=True)
    title = Column(String(300), nullable=True)
    body = Column(Text(), nullable=True)
    post_date = Column(DateTime, nullable=True)
    author = Column(String(50), nullable=True)

    news_id = Column(Integer, ForeignKey('news.news_id'))
    news = relationship(News, lazy='joined')


class SocialImpact(Base):
    __abstract__ = True

    class Meta:
        abstract = True

    @property
    def news_id(self):
        raise NotImplementedError

    @property
    def news(self):
        raise NotImplementedError


class FacebookImpact(SocialImpact):
    __tablename__ = 'facebook_impact'

    facebook_impact_id = Column(Integer, primary_key=True)
    like_qty = Column(Integer, nullable=False)
    share_qty = Column(Integer, nullable=False)

    news_id = Column(Integer, ForeignKey('news.news_id'))
    news = relationship(News, lazy='joined')


class GPlusImpact(SocialImpact):
    __tablename__ = 'gplus_impact'

    gplus_impact_id = Column(Integer, primary_key=True)
    plus_one_qty = Column(Integer, nullable=False)

    news_id = Column(Integer, ForeignKey('news.news_id'))
    news = relationship(News, lazy='joined')


class TwitterImpact(SocialImpact):
    __tablename__ = 'twitter_impact'

    twitter_impact_id = Column(Integer, primary_key=True)
    tweet_qty = Column(Integer, nullable=False)

    news_id = Column(Integer, ForeignKey('news.news_id'))
    news = relationship(News, lazy='joined')


class FeedToCheck(Base):
    __tablename__ = 'feed_to_check'

    feed_to_check_id = Column(Integer, primary_key=True)

    url = Column(String(800), nullable=False)

    website_id = Column(Integer, ForeignKey('website.website_id'))
    website = relationship(WebSite, lazy='joined')


class UrlToCheck(Base):
    __tablename__ = 'url_to_check'

    url_to_check_id = Column(Integer, primary_key=True)

    url = Column(String(800), nullable=False)

    website_id = Column(Integer, ForeignKey('website.website_id'))
    website = relationship(WebSite, lazy='joined')


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    description = Column(String(100), nullable=False)


class Comment(SocialImpact):
    __tablename__ = 'comment'

    comment_id = Column(Integer, primary_key=True)

    description = Column(Text(), nullable=False)

    news_id = Column(Integer, ForeignKey('news.news_id'))
    news = relationship(News, lazy='joined')


class NewsPic(Base):
    __tablename__ = 'news_pic'

    news_pic_id = Column(Integer, primary_key=True)

    url = Column(String(800), nullable=False)
    label = Column(String(300), nullable=True)

    news_id = Column(Integer, ForeignKey('news.news_id'))
    news = relationship(News, lazy='joined')


class NewsStructure(Base):
    __tablename__ = 'news_structure'

    news_structure_id = Column(Integer, primary_key=True)


class RegexType(Base):
    __tablename__ = 'regex_type'

    regex_type_id = Column(Integer, primary_key=True)
    description = Column(String(50), nullable=False)

    news_structure_id = Column(Integer, ForeignKey('news_structure.news_structure_id'))
    news_structure = relationship(NewsStructure, lazy='joined')


class SiteRegex(Base):
    __tablename__ = 'website_regex'

    website_regex_id = Column(Integer, primary_key=True)

    description = Column(String(50), nullable=False)
    expression = Column(String(50), nullable=False)

    website_id = Column(Integer, ForeignKey('website.website_id'))
    website = relationship(WebSite, lazy='joined')
    regex_type_id = Column(Integer, ForeignKey('regex_type.regex_type_id'))
    regex_type = relationship(RegexType, lazy='joined')


class NewsSubject(Base):
    __tablename__ = 'news_subject'

    news_id = Column(Integer, ForeignKey('news.news_id'), primary_key=True)
    news = relationship(News, lazy='joined')
    subject_id = Column(Integer, ForeignKey('subject.subject_id'), primary_key=True)
    subject = relationship(Subject, lazy='joined')
