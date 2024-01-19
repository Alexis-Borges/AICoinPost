import feedparser
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import sqlite3
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

def create_articles_table():
    db_connection = sqlite3.connect("dumpcoinposts.db")
    db_cursor = db_connection.cursor()

    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS blockchainarticles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        content TEXT NOT NULL,
        date DATE
    )
    """)

    db_connection.commit()
    db_connection.close()

def insert_article(title, content, date):
    db_connection = sqlite3.connect("dumpcoinposts.db")
    db_cursor = db_connection.cursor()

    db_cursor.execute("INSERT OR IGNORE INTO blockchainarticles (title, content, date) VALUES (?, ?, ?);", (title, content, date))

    db_connection.commit()
    db_connection.close()

def fetch_feed_entries(feed_link):
    feed = feedparser.parse(feed_link)
    return feed.entries

def filter_entries_by_date(entries, target_date):
    filtered_entries = [entry for entry in entries if datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z").date() == target_date]
    return filtered_entries

def select_top_entries(entries, num_entries):
    sorted_entries = sorted(entries, key=lambda x: datetime.strptime(x.published, "%a, %d %b %Y %H:%M:%S %z"), reverse=True)
    return sorted_entries[:num_entries]

def retrieve_article_content(article_link):
    try:
        response = requests.get(article_link)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        article_title = soup.find('title').get_text(strip=True)

        return article_title

    except Exception as e:
        print(f"Erreur lors de la récupération du contenu de l'article : {e}")
        return None

llm = Ollama(
    model="vicuna",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

create_articles_table()

previous_day = datetime.now().date() - timedelta(days=1)

feed_link = "https://coinacademy.fr/feed/"
num_entries_to_retrieve = 2

entries = fetch_feed_entries(feed_link)
filtered_entries = filter_entries_by_date(entries, previous_day)
selected_entries = select_top_entries(filtered_entries, num_entries_to_retrieve)

for entry in selected_entries:
    entry_title = retrieve_article_content(entry.link)
summarized_content = llm("Fais moi un résumé de cette article : " + entry.link +"n\n")    
insert_article(entry_title, summarized_content, entry.published)