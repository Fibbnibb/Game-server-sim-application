# Game Server Account Manager

A console application that models a game server's account system: accounts of four
privilege levels can log in, message each other, and be banned or unbanned, with all
activity written to plain-text log files.

**Author:** David Chukwuemeka Enwesi (A00284023)

## Files

| File | Purpose |
|---|---|
| `ScriptingProjectfile.py` | All classes — accounts, server, manager, factories |
| `main.py` | Menu loop and entry point |
| `logfile.txt` | Auto-created activity log (logins, bans, requests) |
| `msg.txt` | Auto-created message store |

Python 3, standard library only (`abc`, `time`, `datetime`).

## Running

```bash
python main.py
```

Menu:

```
1  Add an Account
2  Add a Server
3  Manage Account
4  Manage Server
99 Quit
```

Add a server first, then an account, then manage that account by name. Inside
account management: `sh` info, `li` login, `lo` logout, `oth` role-specific actions.

## Account types

| Privilege | Class | Can do |
|---|---|---|
| 0 | `Guest` | Login / logout only |
| 1 | `Player` | Send messages (`snd`) |
| 2 | `Moderator` | View logs (`log`) and messages (`msg`) |
| 15 | `Admin` | Ban (`bn`), unban (`unbn`), list accounts (`lst`), server log (`log`) |

## Design

- **`Account`** and **`ServerDev`** — abstract base classes defining the interface.
- **`AccFactory`** — factory returning the right account subclass for a privilege number.
- **`AccountManager`** — holds `account_dict` and the server list; drives the management menu.
- **`Server`** — class-level `account_list`, `banned_list`, and log file paths shared by everyone.

Log lines are tab-separated: `timestamp | name | action | privilege`.

## Known issues

1. **`Server` can't be instantiated** — it inherits `ServerDev` but never implements the abstract `Turn_on` / `Turn_off`, so construction raises `TypeError`.
2. **Servers are never created** — `AccFactory.buildServer()` only accepts the literal `1`, so option 2 just appends a name to a list and prints "invalid option".
3. **`find_account()` is broken** — the loop variable shadows the `name` parameter, so `name.name == name` is always true and the first account is always returned.
4. **Ban / unban mismatch** — `account_list` stores name strings but `Ban()` passes the account *object* to `remove_account()`, so removal silently fails; `Unban()` has the same problem in reverse.
5. **Admin log methods are swapped** — `show_server_log()` writes `LOG-REQ` then calls `display_msgs()`, and `show_server_msg()` does the opposite.
6. **`show_palyer_list()`** (typo included) references `Admin.status` and `self.account_list`, neither of which exists → `AttributeError`.
7. **`Player.Logout()` logs `LOGIN`** instead of `LOGOUT`.
8. **Privilege argument is ignored** — every `__init__` takes `priveledge` then hardcodes the value anyway.
9. **"Another action?" prompt** asks yes/no but only accepts `y`; typing `yes` exits the loop.
10. **Menu option 4 does nothing** beyond prompting for a name.
11. **Fragile input handling** — `int(input(...))` on the main menu raises on any non-numeric entry, and the single `try/except ValueError` wraps the *whole* loop, so one bad keystroke ends the program.
12. **Guest has no `oth` branch**, so choosing it silently does nothing.
13. **`ServerFac`** duplicates `AccFactory.buildServer` and is unused.

## Suggested fixes

Implement `Turn_on` / `Turn_off` on `Server`, store account objects (not names) in
`account_list` consistently, move the `try/except` inside the input calls, and rename
`priveledge` → `privilege` throughout.
