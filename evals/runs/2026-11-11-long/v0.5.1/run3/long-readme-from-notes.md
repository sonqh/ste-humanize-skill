# envsync

envsync is a command-line tool that keeps the `.env` file of a project the same on every machine. The config server stores one set of environment variables for each project. `envsync pull` downloads those values into your `.env`, and `envsync push` uploads your `.env` to the server.

## Install

```
npm install -g envsync-cli
```

envsync needs Node 20 or newer. It does not start on Node 18.

## First use

1. Open the web UI of the config server and go to Profile > Tokens. Get a token there.
2. Set the `ENVSYNC_TOKEN` environment variable to that token.
3. Go to the project folder and run `envsync init`. It asks for the project name and writes `.envsync.json`.
4. Commit `.envsync.json`. It holds only the project name and the server URL, and no secrets.
5. Run `envsync pull`. The values of the project are now in `.env`.

Read the section on `push` before you upload anything. A push replaces the values of the whole team.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json` |
| `envsync pull` | Downloads the values of the project and writes `.env` |
| `envsync push` | Uploads your `.env` and replaces the values on the server |
| `envsync diff` | Shows which keys differ between your `.env` and the server |
| `envsync history` | Lists the versions that the server keeps for the project |
| `envsync restore <version>` | Makes an old version the current one on the server |

### pull

`envsync pull` writes `.env` with file mode 600, so other users on the machine cannot read it.

If your `.env` has changes that are not on the server, `pull` stops and changes nothing. It exits with code 3. You then have two options:

- Run `envsync diff` to see which keys differ.
- Run `envsync pull --force` to replace your local values. It first saves the old file as `.env.bak`.

### push

`envsync push` replaces the values on the server with the content of your `.env`. It does not merge. Each person on the team gets your values on their next pull.

Run `envsync diff` before each push, and check that every difference is one you intend.

`push` refuses an empty `.env`.

### diff

`envsync diff` prints only the names of the keys that differ. It does not print values, because you may be sharing your screen. Add `--show` to print the values too.

### history and restore

The server keeps the last 20 versions of the values of each project. `envsync history` lists them. `envsync restore <version>` makes one of them the current version.

A restore is a push. It replaces the values that are on the server now, for the whole team.

### Check a change before you make it

Add `--dry-run` to `pull` or `push`. The command prints what would change and writes nothing.

## Keys that stay on your machine

List a key in `.envsyncignore`, one key per line. envsync never pushes a key in that file, and `pull` never replaces it. Use this file for values that belong to one machine, such as a local port.

## CI

In a CI job, use `envsync pull --ci`.

- With `--ci`, the command never prompts.
- If `.envsync.json` is missing, the command exits with code 5.
- CI tokens are read-only. A push from CI always fails with exit code 2. We designed it this way.
- If your runners are behind a proxy, set `HTTPS_PROXY`. envsync uses it.

## Reference

### Exit codes

| Code | Meaning |
|---|---|
| 2 | The token is missing or expired, or a read-only CI token tried to push. The command prints `not authenticated`. |
| 3 | Conflict. `.env` has local changes that are not on the server. `pull` changed nothing. |
| 4 | The server rejected a value larger than 64 KB. The message names the key. |
| 5 | `.envsync.json` is missing in a `pull --ci`. |

### Limits

- One value can be 64 KB at most. The server rejects a larger value, and the push fails.
- One project can hold 500 keys at most.
- One project has one set of values. You cannot keep different values for each branch. Separate environments may come later, but there is no plan for them yet.
- envsync reads and writes only the `.env` in the folder that holds `.envsync.json`. It does not support `.env.local`.

### Server URL

envsync uses the company config server by default. To use a different server, pass `--server` or change the URL in `.envsync.json`.

### Platforms

envsync works on macOS, Linux, and Windows. On Windows we tested it only in WSL. It may work in native PowerShell, but we did not test that.

### Telemetry

envsync collects no telemetry.

## Problems

- `pull` did nothing. This is usually a conflict. Look for exit code 3 and the conflict message, then run `envsync diff`.
- The command prints `not authenticated`. Check that `ENVSYNC_TOKEN` is set. If it is, the token may have expired. Get a new one under Profile > Tokens.

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## License

MIT
