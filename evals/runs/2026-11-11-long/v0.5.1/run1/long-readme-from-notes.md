# envsync

envsync is a command-line tool that keeps the `.env` file in your project folder in sync with the config server. The config server stores one set of environment variables for each project. `envsync pull` downloads those values to your `.env` file. `envsync push` uploads your `.env` file to the server.

## Install

envsync needs Node 20 or newer. It does not start on Node 18.

```
npm install -g envsync-cli
```

## First use

1. Get a token from the web UI of the config server, under Profile > Tokens.
2. Put the token in the `ENVSYNC_TOKEN` environment variable.
3. Go to your project folder and run `envsync init`. It asks for the project name and writes `.envsync.json`.
4. Commit `.envsync.json`. It holds only the project name and the server URL, and no secrets.
5. Run `envsync pull`. It downloads the values of the project and writes `.env`.

## Before you push

`envsync push` replaces the values on the server with the values in your `.env` file. It does not merge. Each person on your team gets your values on their next pull.

Run `envsync diff` before each push to see which keys differ. To see what a push would change, run `envsync push --dry-run`. It writes nothing.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json` in the current folder. |
| `envsync pull` | Downloads the values of the project and writes `.env`. |
| `envsync push` | Uploads your `.env` file and replaces the values on the server. |
| `envsync diff` | Shows the names of the keys that differ between your `.env` file and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Puts one of those versions back on the server. |

### pull

- If `.env` has local changes that are not on the server, pull stops with exit code 3 and changes nothing. Run `envsync diff` to see the keys that differ.
- `envsync pull --force` overwrites your local file. It saves the old file as `.env.bak` first.
- Pull writes `.env` with file mode 600, so other users on the machine cannot read it.
- `envsync pull --dry-run` prints what would change and writes nothing.

### push

- Push refuses an empty `.env` file.
- The server rejects a single value larger than 64 KB. The push fails with exit code 4 and names the key.
- `envsync push --dry-run` prints what would change and writes nothing.

### diff

Diff prints key names only, because people share their screens. To print the values too, pass `--show`.

### history and restore

The server keeps the last 20 versions of the values of each project. `envsync history` lists them. `envsync restore <version>` is a push: it replaces the values that are on the server now.

## Keys that stay on your machine

List a key in `.envsyncignore`, one key per line, to keep it local. envsync never pushes a listed key, and pull never overwrites it. Use this file for values that are specific to one machine, such as a local port.

## CI

Use `envsync pull --ci` in CI.

- With `--ci`, pull never prompts.
- With `--ci`, pull fails with exit code 5 if `.envsync.json` is missing.
- CI tokens are read-only. A push from CI always fails with exit code 2. This is intended.
- envsync uses the `HTTPS_PROXY` variable, so it works on runners that are behind a proxy.

## Reference

### Exit codes

| Code | Meaning |
|---|---|
| 2 | The token is missing or expired, or a read-only token tried to push. The command prints `not authenticated`. |
| 3 | Conflict. `.env` has local changes that are not on the server. Pull changed nothing. |
| 4 | The server rejected a value larger than 64 KB. The message names the key. |
| 5 | `.envsync.json` is missing in a `pull --ci` run. |

### Limits

- A single value can be 64 KB at most.
- A project can hold 500 keys at most.
- A project has one set of values. You cannot keep different values for each branch, and no such feature is planned.
- envsync reads and writes only the `.env` file in the folder that holds `.envsync.json`. It does not support `.env.local`.

### Server URL

envsync uses the config server of the company by default. To use a different server, pass `--server` or set the URL in `.envsync.json`.

### Platforms

envsync works on macOS, Linux, and Windows. On Windows, it is tested only in WSL. It may work in native PowerShell, but that is not tested.

### Telemetry

envsync collects no telemetry.

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## If pull seems to do nothing

The usual cause is a conflict: pull stopped with exit code 3. Read the message, then run `envsync diff`. To replace your local file with the server values, run `envsync pull --force`.

## License

MIT
