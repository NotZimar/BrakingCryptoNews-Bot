This project involves the design and implementation of a Telegram bot that automatically collects cryptocurrency-related news and sends it to a designated Telegram channel.

### Features:
1. **News Search**: Collects cryptocurrency news using the `Search_for_news` function. When new news is detected, its title and link are sent.
2. **Automatic Translation**: Translates news titles into Persian using the `Translate` function.
3. **Importance Scoring**: Rates the importance of news using the `importance_rate` function.
4. **Message Formatting and Delivery**: Sends news with formatted content, including English and Persian titles, importance score, and direct link, to the channel.
5. **User Management**: Monitors user join/leave actions in the channel and updates the SQLite database accordingly.
6. **Data Storage**: Maintains user information in an SQLite database.

### Technologies:
- **Programming Language**: Python
- **Libraries**:
  - `Telethon` for Telegram communication
  - `sqlite3` for database management
  - `asyncio` for handling asynchronous tasks
- Custom functions for news search, translation, and scoring

### Structure:
- The main code includes:
  1. `SendMessage`: Sends messages to the Telegram channel in HTML format.
  2. `Main`: Continuously searches for and posts new news.
  3. `add_user` & `delete_user`: Manages user data in the SQLite database.
  4. `on_chat_action`: Detects user join/leave events in the channel.
  5. `start_bot`: Runs the bot and manages tasks concurrently.

This bot is ideal for cryptocurrency news channels, enabling automatic and efficient news sharing.
