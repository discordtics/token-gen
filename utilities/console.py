import Stats
import time
import Solver


class ConsoleX:
    def titleThread():
        while Stats.ACTIVE:
            elapsed = round(time() - Stats.start, 2)
            try:
                unlocked_rate = round((Stats.unlocked / (Stats.locked + Stats.unlocked)) * 100, 2)
            except:
                unlocked_rate = 0
            system(f"title [ VastGen ] U: {Stats.unlocked} | L: {Stats.locked} | UPM: {round(Stats.unlocked/elapsed,2)} @ {unlocked_rate}% | Elapsed: {elapsed}".replace("|", "^|"))
            sleep(0.1)