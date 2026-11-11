# envsync

envsync is a command-line tool that keeps the `.env` file of a project the same as the values on the config server. `envsync pull` downloads the latest values. `envsync push` uploads your values.

## Install

envsync needs Node 20 or newer. It does not start on Node 18.

```
npm install -g envsync-cli
```

## Authenticate

1. Open the config server web UI.
2. Go to Profile > Tokens and get a token.
3. Put the token in the `ENVSYNC_TOKEN` environment variable.

If the token is missing or expired, each command prints `not authenticated` and exits with code 2.

## Connect a project

Run this command in the project folder:

```
envsync init
```

The command asks for the project name and writes `.envsync.json`. Commit that file. It contains only the project name and the server URL, and no secrets.

envsync uses the company config server by default. To use a different server, pass `--server` or change the URL in `.envsync.json`.

## Commands

| Command | What it does |
|---|---|
| `envsync pull` | Downloads the values of the project and writes them to `.env`. |
| `envsync push` | Uploads your `.env` to the server and replaces the values there. |
| `envsync diff` | Shows which keys differ between your `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Makes an old version the current one on the server. |

`pull` and `push` accept `--dry-run`. With this flag, the command prints what would change and writes nothing.

### pull

If `.env` has local changes that are not on the server, `pull` stops. It changes nothing and exits with code 3 (conflict). When a pull seems to do nothing, this conflict is the usual cause.

- Run `envsync diff` to see which keys differ.
- Run `envsync pull --force` to overwrite your local file. envsync first saves the old file as `.env.bak`.

`pull` writes `.env` with file mode 600, so other users on the machine cannot read it.

### push

**`push` overwrites the values on the server. It does not merge.** Each person on the team gets your values on their next pull. Run `envsync diff` before each push.

`push` refuses an empty `.env`.

### diff

`diff` prints key names only, because people share their screens. To print the values too, pass `--show`.

### history and restore

The server keeps the last 20 versions of the values of each project. `envsync history` lists them. `envsync restore <version>` makes one of them current again.

A restore is a push. It overwrites the values that are on the server now.

## Keep a key local

List a key in `.envsyncignore`, one key per line. envsync never pushes a listed key, and `pull` never overwrites it. Use this file for values that belong to one machine, such as a local port.

## Limits

- One project has one set of values. You cannot have different values for each branch.
- envsync reads and writes only `.env`, in the folder that contains `.envsync.json`. It does not support `.env.local`.
- A project can have 500 keys at most.
- One value can be 64 KB at most. The server rejects a larger value. The push then fails with exit code 4 and names the key.
- envsync runs on macOS, Linux, and Windows. On Windows, we tested it only in WSL. Native PowerShell may work, but we did not test it.

## Use in CI

Use this command in CI:

```
envsync pull --ci
```

- With `--ci`, the command never prompts.
- If `.envsync.json` is missing, the command fails with exit code 5.
- CI tokens are read-only. A push from CI always fails with exit code 2. This behavior is deliberate.
- envsync honors `HTTPS_PROXY` if your runners are behind a proxy.

## Exit codes

| Code | Meaning |
|---|---|
| 2 | Not authenticated. The token is missing, expired, or read-only for a push. |
| 3 | Conflict. `.env` has local changes that are not on the server. |
| 4 | The server rejected a value larger than 64 KB. |
| 5 | `.envsync.json` is missing (with `--ci`). |

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## Telemetry

envsync collects no telemetry.

## License

MIT
