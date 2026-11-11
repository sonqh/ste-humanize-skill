# envsync

envsync is a command-line tool that keeps the `.env` file of a project in sync with the config server. The config server stores one set of environment variables for each project. `envsync pull` downloads those values to your `.env` file. `envsync push` uploads your `.env` file to the server.

## Install

envsync needs Node 20 or newer. It does not start on Node 18.

```
npm install -g envsync-cli
```

envsync works on macOS, Linux, and Windows. On Windows, we tested it only in WSL. It might work in native PowerShell, but we did not test that.

## Set up a project

1. Get a token from the web UI of the config server, under Profile > Tokens.
2. Put the token in the `ENVSYNC_TOKEN` environment variable.
3. Run `envsync init` in the project folder. It asks for the project name and writes `.envsync.json`.
4. Commit `.envsync.json`. It holds only the project name and the server URL, and no secrets.
5. Run `envsync pull` to download the values.

envsync reads the token only from `ENVSYNC_TOKEN`. It does not read `~/.envsyncrc`.

The server URL defaults to the company config server. To use a different server, pass `--server` or change the URL in `.envsync.json`.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json`. |
| `envsync pull` | Downloads the values of the project and writes `.env`. |
| `envsync push` | Uploads your `.env` and replaces the values on the server. |
| `envsync diff` | Shows which keys differ between your `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Puts an earlier version back on the server. |

`--dry-run` works with `pull` and `push`. It prints what would change and writes nothing.

### pull

`envsync pull` writes `.env` with file mode 600, so other users on the machine cannot read it.

If `.env` has local changes that are not on the server, `pull` stops. It changes nothing and exits with code 3. When `pull` seems to do nothing, this conflict is the usual cause. To continue:

1. Run `envsync diff` to see which keys differ.
2. Push your changes, or run `envsync pull --force` to overwrite your local file.

`envsync pull --force` saves the old file as `.env.bak` before it overwrites `.env`.

### push

`envsync push` overwrites the values on the server. It does not merge. Each person on the team gets your values on their next `pull`. Run `envsync diff` before you push.

`push` refuses an empty `.env`.

### diff

`envsync diff` prints key names only, because people share their screens. To print the values too, pass `--show`.

### history and restore

The server keeps the last 20 versions of the values for each project. `envsync history` lists them. `envsync restore <version>` puts one back.

A restore is a push. It overwrites the values that are on the server now.

## Keep a key local

List a key in `.envsyncignore` to keep it on your machine only. `push` never uploads that key, and `pull` never overwrites it. Write one key on each line. Use this file for values that differ between machines, such as local ports.

## Limits

- The server rejects a single value larger than 64 KB. The push fails with exit code 4 and names the key.
- A project can hold 500 keys at most.
- A project has one set of values. You cannot keep different values for each branch.
- envsync reads and writes only the `.env` file in the folder that holds `.envsync.json`. It does not support `.env.local`.

## Use in CI

Use `envsync pull --ci` in CI. With `--ci`, envsync never prompts, and it exits with code 5 if `.envsync.json` is missing.

CI tokens are read-only. A push from CI always fails with exit code 2. We made it fail on purpose.

If your runners sit behind a proxy, set `HTTPS_PROXY`. envsync uses it.

## Exit codes

| Code | Meaning |
|---|---|
| 2 | The token is missing or expired, or a CI token tried to push. With a missing or expired token, envsync prints `not authenticated`. |
| 3 | `pull` found local changes that are not on the server. Nothing changed. |
| 4 | `push` failed because one value is larger than 64 KB. |
| 5 | `pull --ci` did not find `.envsync.json`. |

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## Telemetry

envsync collects no telemetry.

## License

MIT
