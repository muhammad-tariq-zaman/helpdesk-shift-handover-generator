# helpdesk-shift-handover-generator

Turn an open-ticket CSV into a clean Markdown shift-handover note, P1 first, closed tickets excluded.

## How to run

```sh
python3 main.py tickets.csv
```

## Example output

```
# Shift handover

Open tickets: 2

- **T-101** [P1] VPN down
```

Standard library only. Run the tests with `python3 -m unittest discover`.
