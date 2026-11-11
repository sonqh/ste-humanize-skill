# envsync

envsync is a command-line tool that keeps the `.env` file of a project in sync with the config server. The config server stores one set of environment variables for each project. `envsync pull` downloads those values to your `.env` file. `envsync push` uploads your `.env` file to the server.

`envsync push` replaces the values on the server and does not merge. Each person on the team gets your values on their next pull.

## Install

```
npm install -g envsync-cli
```

- envsync needs Node 20 or newer. It does not start on Node 18.
- It works on macOS, Linux, and Windows. On Windows, we tested it only in WSL. It might work in native PowerShell, but we did not test that.
- It sends no telemetry.

## Setup

1. Get a token from the web UI of the config server, under Profile > Tokens.
2. Put the token in the `ENVSYNC_TOKEN` environment variable.
3. Run `envsync init` in the project folder. It asks for the project name and writes `.envsync.json`.
4. Commit `.envsync.json`. It holds only the project name and the server URL, and it contains no secrets.
5. Run `envsync pull` to write the `.env` file.

If the token is missing or expired, the command prints `not authenticated` and exits with code 2.

envsync uses the company config server by default. To use a different server, pass `--server` or change the server URL in `.envsync.json`.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json`. |
| `envsync pull` | Downloads the values of the project and writes `.env`. |
| `envsync push` | Uploads your `.env` and replaces the values on the server. |
| `envsync diff` | Shows which keys differ between your `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Puts an earlier version back on the server. |

envsync reads and writes only the file named `.env` in the folder that contains `.envsync.json`. It does not support `.env.local`.

### pull

- If your `.env` has local changes that are not on the server, pull stops and changes nothing. It exits with code 3 (conflict). Run `envsync diff` to see which keys differ.
- `envsync pull --force` overwrites your local file. It first saves the old file as `.env.bak`.
- Pull writes `.env` with file mode 600, so other users on the machine cannot read it.
- `envsync pull --dry-run` prints what would change and writes nothing.

### push

- Push replaces the values on the server. It does not merge. Run `envsync diff` before each push.
- Push refuses an empty `.env`.
- `envsync push --dry-run` prints what would change and writes nothing.

### diff

Diff shows the names of the keys that differ. It prints the values only when you pass `--show`, because people share their screens.

### history and restore

The server keeps the last 20 versions of the values for each project. `envsync history` lists them. `envsync restore <version>` puts one back.

A restore is a push. It replaces the values that are on the server now, and the team gets the restored values on their next pull.

## Keys that stay on your machine

List a key in `.envsyncignore` to keep it local, one key per line. envsync never pushes a listed key, and pull never overwrites it. Use this for values that differ on each machine, such as local ports.

## Limits

- A project can hold 500 keys at most.
- The server rejects a single value larger than 64 KB. The push fails with exit code 4 and names the key.
- A project has one set of values. You cannot keep different values for each branch.

## CI

Use `envsync pull --ci` in CI.

- With `--ci`, envsync never prompts.
- If `.envsync.json` is missing, the command fails with exit code 5.
- CI tokens are read-only. A push from CI always fails with exit code 2, and we designed it that way.
- envsync honors `HTTPS_PROXY`, for runners that are behind a proxy.

## Exit codes

| Code | Meaning |
|---|---|
| 2 | Not authenticated. The token is missing or expired, or a CI token tried to push. |
| 3 | Conflict. Your `.env` has local changes that are not on the server, and pull changed nothing. |
| 4 | A value is larger than 64 KB, and the push failed. |
| 5 | `.envsync.json` is missing in a `pull --ci` run. |

If a pull seems to do nothing, the usual cause is exit code 3. Read the message, then run `envsync diff`.

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## License

MIT
