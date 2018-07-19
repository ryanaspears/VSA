# Name:
# Date:

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# proj08: RSS Feed Filter

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

import string

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: Create class NewsStory by finishing the constructor and get methods

class NewsStory(object):
    """
    A class that stores information about a NewsStory.
    Attributes:
        * guid
        * title
        * subject
        * summary
        * link
    """
    def __init__(self, guid, title, subject, summary, link):
        """
        Returns a NewsStory object with the following attributes
        :param guid: a string that serves as a unique name for this entry 
        :param title: string
        :param subject: string
        :param summary: string
        :param link: string     
        """
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
        return self.link

# Your job is to write functions for the other 4 attributes.


#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError
        # There is no other code for the Trigger object. This is an abstract class - it
        #  is serving as an umbrella for all of the other types of triggers. Start
        # working on problems 2-5 below - do not add code here!

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

# Create a class, WordTrigger, that is a subclass of trigger.

# You will need a constructor (an "init" method). This constructor should take a word
# and save the word as part of itself (just like NewsStory takes a guid and saves it as
#  part of itself).

# You will also need one method: is_word_in. This method will take in one string,
# and it will return True if the word is in the text, False otherwise. This method
# should not be case sensitive.


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def is_word_in(self, text):
        for item in string.punctuation:
            text = text.replace(item, " ")
        text = text.lower()
        text = text.split(" ")
        if self.word in text:
            return True
        else:
            return False


# Each of the three triggers below can be completed in three lines.
# First, define the new class, which is a subclass of WordTrigger.
# You do NOT need a constructor, because this is inherited from WordTrigger.
# Second, create a method "evaluate" that takes a NewsStory object.
# Third, uses "is_word_in" to check to see
#  if the word is in the appropriate part of the story (for example, for title trigger,
# to see if the word is in the title of the story).
# TODO: TitleTrigger


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        title1 = story.get_title()
        # print self.is_word_in(title1)
        return self.is_word_in(title1)

# TODO: SubjectTrigger


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        subject1 = story.get_subject()
        # print self.is_word_in(subject1)
        return self.is_word_in(subject1)

# TODO: SummaryTrigger


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        summary1 = story.get_summary()
        # print self.is_word_in(summary1)
        return self.is_word_in(summary1)

# Composite Triggers
# Problems 6-8

# Each of these triggers should be a subclass of Trigger, NOT WordTrigger.
# That means they will need their own constructor, because they cannot inherit from the
#  class WordTigger.
# They will also need an evaluate method.
# TODO: NotTrigger

0
class NotTrigger(Trigger):
    def __init__(self, t):
        self.t = t

    def evaluate(self, story):
        return not self.t.evaluate(story)

# TODO: AndTrigger


class AndTrigger(Trigger):
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)


# TODO: OrTrigger


class OrTrigger(Trigger):
    def __init__(self, t3, t4):
        self.t3 = t3
        self.t4 = t4

    def evaluate(self, story):
        return self.t3.evaluate(story) or self.t4.evaluate(story)

# Phrase Trigger
# Question 9

# This is also a subclass of Trigger, so it will need a constructor and an evaluate
# method.
# TODO: PhraseTrigger


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return str(self.phrase) in story.get_subject() or str(self.phrase) in story.get_title() or \
               str(self.phrase) in story.get_summary()

#======================
# Part 3
# Filtering
#======================


def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    storylist = []
    for Trigger in triggerlist:
        for story in stories:
            if Trigger.evaluate(story) == True:
                if story not in storylist:
                    storylist.append(story)
    return storylist

#======================
# Extensions: Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Trump")
    t2 = SummaryTrigger("Vanderbilt")
    t3 = PhraseTrigger("Net Neutrality")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line 
    #triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

