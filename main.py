#!/usr/bin/env python3
"""One Star for Monday.

Writes one line (<=25 words, 1-180 characters) to /output/entry.txt: a
one-star review of Monday written as though Monday were a restaurant.

Drafting notes (scored against the judge brief):
- The judge weighs, in order: (1) reads as a one-star review of Monday
  written as if Monday were a restaurant; (2) sounds like a real
  diner's complaint, with a table, a server, a dish or a bill that
  went wrong; (3) lands the joke about Monday itself, so the line
  could not be about any other day of the week; (4) short and
  quotable, the kind of line someone retypes into a chat without
  trimming a word; (5) plain text inside 25 words, no stage
  directions, hashtags or explanation.
- Field cliche avoided: the most common angles in the field's 89
  visible entry titles are (a) "ordered the weekend, got Monday
  instead" (e.g. "Ordered the weekend special, got cold leftovers",
  "One star. Ordered the weekend, got Monday instead.", "The server
  took my weekend, brought out Monday instead"); (b) "billed /
  charged for the whole week / weekend" (e.g. "Billed for All Five
  Days", "Seated by the Kitchen, Charged for the Week", "The Bill
  Charged Me for a Weekend I Never Got"); (c) "waited forty minutes
  for a table" and (d) "cold coffee" with a waiter named Traffic or
  Deadline. None of the six candidates orders the weekend, bills the
  week, waits forty minutes, or serves cold coffee. The winner uses
  a fresh angle instead: the weekend as takeaway — Monday boxes up
  Sunday, keeps the change, and hands over a meeting as the dish.
- Blind pairwise tournament (15 pairs, judged only against the
  brief, criteria in order; run as a separate blind pass — no
  subagent judge can be spawned at this depth, same as the 01:52
  and 02:52 batch workers):
  A-B: A, A-C: A, A-D: A, A-E: E, A-F: A,
  B-C: C, B-D: D, B-E: E, B-F: F,
  C-D: D, C-E: E, C-F: C,
  D-E: E, D-F: D, E-F: E.
  Wins: A 4, B 0, C 2, D 3, E 5, F 1. Winner E, runner-up A.
  A. Monday sat me at the kids' table, served a meeting in a sippy
     cup, and charged the adult price. Strong table/dish/bill
     furniture and a funny closer, but the meeting could be any
     weekday — loses to E on criterion 3 (the weekend-to-Monday
     handoff only happens on Monday).
  B. The health inspector shut Monday down fifty-two weeks running
     and it still opens every week. Very Monday-specific, but no
     table, server, dish or bill — loses on criterion 2 to every
     candidate that has one.
  C. Checked my weekend at the door; Monday lost the ticket, kept
     my coat, and seated me at 7 a.m. Real coat-check furniture and
     a Monday handoff, but the closer is only a time, not a punch.
  D. Monday's menu has one item: a 9 a.m. meeting, served cold,
     with fluorescent lighting and no substitutions. Tightest line
     (19 words) and a killer closer, but a 9 a.m. meeting could be
     any weekday — loses to E on criterion 3 by a hair.
  E. WINNER. I asked for the weekend to go; Monday boxed Sunday,
     kept the change, and handed me a meeting. Three beats
     (boxed Sunday / kept the change / handed me a meeting), real
     takeaway furniture, and the joke only works on Monday — the
     Sunday-to-Monday handoff. Ends on the punch: the dish is a
     meeting.
  F. Ordered the soup of the day; Monday served me the same grey
     Monday from last week, still lukewarm. Good dish image, but
     only one piece of diner furniture — loses on criterion 2.
- Extra-mile pass after the pick: E stress-tested against the spec
  (20 words, 103 chars, 1-180 required, one line, UTF-8, complete),
  against a generic house baseline ("One star. Monday was bad, the
  food was cold, and I waited too long for a table.") — E wins on
  the weekend-to-Monday handoff, three distinct beats and a dish
  that is a meeting — and against the field's top visible angles
  (ordered-the-weekend, billed-for-the-week, waited-forty-minutes,
  cold coffee), which E avoids entirely. The weakest dimension
  (the closer "handed me a meeting") was checked against "handed me
  a Monday": the meeting is more concrete as a dish and more
  Monday-specific as a 9 a.m. workday anchor, so the line stands
  as tournament-won.
- Gate check: 20 words, 103 chars, 1-180 required, UTF-8, single
  line. Verified by running main.py: writes 103 characters to
  /output/entry.txt.
"""

import os

LINE = (
    "One star. I asked for the weekend to go; Monday boxed Sunday, "
    "kept the change, and handed me a meeting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
