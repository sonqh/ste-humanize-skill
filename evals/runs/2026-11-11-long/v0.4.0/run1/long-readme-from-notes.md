# envsync

envsync is a command-line tool that keeps the `.env` file of a project in sync with the config server. The config server stores one set of environment variables for each project. `envsync pull` downloads those values to your machine, and `envsync push` uploads yours.

A push replaces the values on the server for the whole team. Read [Push](#push) before you run it.

## Install

```sh
npm install -g envsync-cli
```

envsync needs Node 20 or newer. It does not start on Node 18.

envsync works on macOS, Linux, and Windows. On Windows we tested it only in WSL. It may work in native PowerShell, but we did not test that.

## Authenticate

1. Open the config server web UI.
2. Go to Profile > Tokens and get a token.
3. Put the token in the `ENVSYNC_TOKEN` environment variable.

If the token is missing or expired, the command prints `not authenticated` and exits with code 2.

## Configure a project

Run this command in the project folder:

```sh
envsync init
```

The command asks for the project name and writes `.envsync.json`. Commit that file. It holds only the project name and the server URL, and no secrets.

envsync uses the company config server by default. To use a different server, change the URL in `.envsync.json` or pass `--server`.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json`. |
| `envsync pull` | Downloads the values of the project and writes `.env`. |
| `envsync push` | Uploads your `.env` and replaces the values on the server. |
| `envsync diff` | Shows which keys differ between your `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Puts an earlier version back on the server. |

envsync reads and writes only the file named `.env` in the folder that contains `.envsync.json`.

### Pull

```sh
envsync pull
```

- Pull writes `.env` with file mode 600, so other users on the machine cannot read it.
- If `.env` has local changes that are not on the server, pull stops. It changes nothing and exits with code 3. Run `envsync diff` to see the keys that differ.
- `envsync pull --force` overwrites your local file. It first saves the old file as `.env.bak`.
- `envsync pull --dry-run` prints the changes and writes nothing.

### Push

```sh
envsync diff
envsync push
```

Push overwrites the values on the server. It does not merge. Each person on the team gets your values on their next pull, so run `envsync diff` before each push.

- Push refuses an empty `.env`.
- `envsync push --dry-run` prints the changes and writes nothing.

### Diff

`envsync diff` shows key names only. It prints values only when you pass `--show`, because people share their screens.

### History and restore

The server keeps the last 20 versions of the values for each project. `envsync history` lists them. `envsync restore <version>` puts one of them back.

A restore is a push. It overwrites the values that are on the server now, and the team gets them on their next pull.

## Keep a key local

List a key in `.envsyncignore`, one key per line. envsync never pushes a key in that file, and pull never overwrites it. Use the file for values that belong to one machine, such as a local port.

## Limits

- A project can hold 500 keys at most.
- The server rejects a value larger than 64 KB. The push fails with exit code 4 and names the key.
- A project has one set of values. You cannot keep different values for each branch. We may add environments later, but we have no plan for that yet.
- envsync does not read `.env.local` or any file other than `.env`.

## Use envsync in CI

```sh
envsync pull --ci
```

- With `--ci`, pull never prompts. It fails with exit code 5 if `.envsync.json` is missing.
- CI tokens are read-only. A push from CI always fails with exit code 2. This failure is deliberate.
- envsync honors `HTTPS_PROXY`, for runners that sit behind a proxy.

## Exit codes

| Code | Meaning |
|---|---|
| 2 | The token is missing or expired, or a read-only CI token tried to push. |
| 3 | Pull found local changes in `.env` that are not on the server, and changed nothing. |
| 4 | Push failed because one value is larger than 64 KB. |
| 5 | `envsync pull --ci` did not find `.envsync.json`. |

If pull seems to do nothing, the usual cause is exit code 3. Read the message that pull prints, then run `envsync diff`.

## Update

```sh
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## Telemetry

envsync collects no telemetry.

## License

MIT
