# envsync

envsync is a command-line tool that keeps the `.env` file on your machine in sync with a project on the config server. The server stores the environment variables of each project. `envsync pull` downloads the latest values. `envsync push` uploads your values.

## Install

```
npm install -g envsync-cli
```

envsync needs Node 20 or newer. It does not start on Node 18.

It works on macOS, Linux, and Windows. On Windows we tested it only in WSL. It might work in native PowerShell, but we did not test that.

envsync collects no telemetry.

## Authenticate

1. Open the config server web UI.
2. Go to Profile > Tokens and get a token.
3. Put the token in the `ENVSYNC_TOKEN` environment variable.

If the token is missing or expired, the command prints `not authenticated` and exits with code 2.

## Set up a project

Run this command in the project folder:

```
envsync init
```

The command asks for the project name and writes `.envsync.json`. Commit that file. It contains only the project name and the server URL, and no secrets.

## Commands

| Command | What it does |
|---|---|
| `envsync pull` | Downloads the values of the project and writes `.env`. |
| `envsync push` | Uploads your `.env` to the server. |
| `envsync diff` | Shows which keys differ between your `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Makes a saved version the current one on the server. |

### pull

`envsync pull` writes `.env` with file mode 600, so other users on the machine cannot read it.

If `.env` has local changes that are not on the server, pull stops. It changes nothing and exits with code 3 (conflict). You then have two options:

- Run `envsync diff` to see which keys differ.
- Run `envsync pull --force` to overwrite your local file. envsync first saves the old file as `.env.bak`.

### push

**Push overwrites the values on the server. It does not merge.** Each person on the team gets your values on their next pull. Run `envsync diff` before you push.

Push refuses an empty `.env`.

### diff

`envsync diff` prints key names only. It prints values only when you pass `--show`. This protects the values when you share your screen.

### history and restore

The server keeps the last 20 versions of the values for each project. `envsync history` lists them. `envsync restore <version>` makes one of them current again.

**A restore is a push. It overwrites the values that are on the server now.**

### Options

- `--dry-run` works on pull and push. It prints what would change and writes nothing.
- `--server <url>` sets the config server URL for one command. The default is the company config server. You can also set the URL in `.envsync.json`.

## Keys that stay local

List a key in `.envsyncignore`, one key per line. envsync never pushes that key, and pull never overwrites it. Use this file for values that belong to one machine, such as local ports.

## Limits

- The server rejects a single value larger than 64 KB. The push fails with exit code 4 and names the key.
- A project can hold 500 keys at most.
- A project has one set of values. You cannot have different values per branch, and this is not planned yet.
- envsync reads and writes only the `.env` file in the folder that contains `.envsync.json`. It does not support `.env.local`.

## Use in CI

```
envsync pull --ci
```

- With `--ci`, envsync never prompts.
- If `.envsync.json` is missing, the command fails with exit code 5.
- CI tokens are read-only. A push from CI always fails with exit code 2. This is intentional.
- envsync honors `HTTPS_PROXY`, for runners behind a proxy.

## Exit codes

| Code | Meaning |
|---|---|
| 2 | Not authenticated. The token is missing, expired, or read-only for a push. |
| 3 | Conflict. `.env` has local changes that are not on the server. |
| 4 | The server rejected a value larger than 64 KB. |
| 5 | `.envsync.json` is missing (with `--ci`). |

If pull seems to do nothing, look at the exit code. The usual cause is code 3.

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## License

MIT
