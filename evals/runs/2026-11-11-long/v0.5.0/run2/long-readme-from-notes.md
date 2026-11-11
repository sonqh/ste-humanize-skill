# envsync

envsync is a command-line tool that keeps the `.env` file of a project the same as the values on the company config server. `envsync pull` downloads the server values to your machine. `envsync push` uploads your values to the server.

```
npm install -g envsync-cli
```

## Before you start

- envsync needs Node 20 or newer. It does not start on Node 18.
- It works on macOS and Linux. On Windows, we tested it only in WSL. It may work in native PowerShell, but we did not test that.
- One project has one set of values. You cannot keep different values for each branch.
- envsync reads and writes only `.env`, in the folder that holds `.envsync.json`. It does not support `.env.local`.
- envsync sends no telemetry.

## Set up a project

1. Open the web UI of the config server and go to Profile > Tokens. Get a token there.
2. Put the token in the `ENVSYNC_TOKEN` environment variable.
3. Go to the project folder and run `envsync init`. The command asks for the project name and writes `.envsync.json`.
4. Commit `.envsync.json`. It holds only the project name and the server URL, and no secrets.
5. Run `envsync pull` to write `.env`.

The server URL defaults to the company server. To use a different server, pass `--server` or change the URL in `.envsync.json`.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json`. |
| `envsync pull` | Downloads the project values and writes `.env`. |
| `envsync push` | Uploads your `.env` and replaces the values on the server. |
| `envsync diff` | Shows the names of the keys that differ between `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Makes an earlier version the current one on the server. |

### pull

`envsync pull` writes `.env` with file mode 600, so other users on the machine cannot read it.

If `.env` has local changes that are not on the server, pull stops. It changes nothing and exits with code 3. To continue:

1. Run `envsync diff` to see which keys differ.
2. If you want to keep your local values, do not pull.
3. If you want the server values, run `envsync pull --force`. It saves the old file as `.env.bak`, then overwrites `.env`.

### push

**Push replaces the values on the server. It does not merge.** Each person on the team gets your values on their next pull. Run `envsync diff` before each push.

Push refuses an empty `.env`.

### diff

`envsync diff` prints key names only. It prints the values only when you pass `--show`. Do not pass `--show` while you share your screen.

### history and restore

The server keeps the last 20 versions of the values for each project. `envsync history` lists them. `envsync restore <version>` makes one of them current again.

A restore is a push. It replaces the values that are on the server now, and the team gets them on the next pull.

### Try a command without changes

Add `--dry-run` to `pull` or `push`. The command prints what it would change and writes nothing.

## Keep a key on your machine only

List the key in a file named `.envsyncignore`, one key per line. envsync never pushes a key in this file, and pull never overwrites it. Use this for values that belong to one machine, such as a local port.

## Limits

- The server rejects a value larger than 64 KB. The push fails with exit code 4 and names the key.
- A project can hold 500 keys at most.

## Use envsync in CI

Run `envsync pull --ci`.

- With `--ci`, the command never prompts.
- It fails with exit code 5 if `.envsync.json` is missing.
- CI tokens are read-only. A push from CI always fails with exit code 2. This is on purpose.
- If your runners are behind a proxy, set `HTTPS_PROXY`. envsync uses it.

## Exit codes

| Code | Meaning | What to do |
|---|---|---|
| 2 | The token is missing or expired, or a read-only token tried to push. For a missing or expired token, the command prints `not authenticated`. | Set a valid token in `ENVSYNC_TOKEN`. |
| 3 | Conflict. `.env` has local changes that are not on the server. Pull changed nothing. | Run `envsync diff`. To replace your local values with the server values, run `envsync pull --force`. |
| 4 | The server rejected a value larger than 64 KB. The message names the key. | Make the value of that key smaller. |
| 5 | `.envsync.json` is missing in a `--ci` run. | Run `envsync init` and commit the file. |

## Common questions

### Why did pull change nothing?

Usually pull found a conflict and exited with code 3. Read the message, then run `envsync diff`.

### Can I have different values for each branch?

No. We may add environments later, but we have no plan for that now.

### Does it read `.env.local`?

No. envsync reads only `.env`.

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## License

MIT
