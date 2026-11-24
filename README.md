# The Zipper Traffic Jam

[![Everyday Things, Two Lines, Longer Run](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Akhmad045/u-suga-everyday-things-two-lines-longer-run-f8734479/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![Reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Akhmad045/u-suga-everyday-things-two-lines-longer-run-f8734479/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

An entry for the [Everyday Things, Two Lines, Longer Run](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479) bounty on [make.fun](https://make.fun): two lines, at most 400 characters, explaining one everyday thing to a 10-year-old through a concrete analogy, then honestly saying what the analogy maps and what it leaves out.

## The entry

> A traffic jam is a zipper stuck halfway, its car-teeth locked together so none of them can slide past the one in front.
> It maps how the cars lock together tooth by tooth and only crawl forward when the stuck one frees itself, but a real zipper has no drivers, no horns, and no one in a hurry.

The entry was picked from ten drafted candidates by internal pairwise comparison against the judge brief (explains one everyday thing to a 10-year-old, concrete and surprising analogy, one vivid sentence, honest and specific second line). The winner's analogy is a thing a child holds every day — a zipper — joined to traffic in a way that explains the jam's mechanism, not just its look: one stuck tooth holds the whole line still. Its second line names exactly what the analogy maps (the tooth-by-tooth locking, the crawl once the stuck tooth frees itself) and three concrete things it leaves out (drivers, horns, hurry).

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes those two lines — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–400 characters, not only whitespace, exactly two lines, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
